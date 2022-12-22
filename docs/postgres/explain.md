---
author: ''
category: postgres
date: '2022-12-05'
summary: ''
title: Postgres - Explaining EXPLAIN
---

## Postgres Explain

How to reading and analyse an explain statement?

### What is Explain?

`EXPLAIN` is a postgres SQL command to show the execution plan of a statement

* The execution plan shows how the table(s) referenced by the statement will be scanned — by plain sequential scan, index scan, etc.
* The most critical part of the display is the estimated statement execution cost, which is the planner's guess at how long it will take to run the statement (measured in cost units that are arbitrary, but conventionally mean disk page fetches).
* The `ANALYZE` option causes the statement to be actually executed, not only planned

> Only the ANALYZE and VERBOSE options can be specified, and only in that order, without surrounding the option list in parentheses

A typical explain:

    EXPLAIN (ANALYZE, COSTS, VERBOSE, BUFFERS, FORMAT JSON) <SQL here>

* `ANALYSE` - Carry out the command and show actual run times and other statistics.
* `COSTS` - Include information on the estimated startup and total cost of each plan node, as well as the estimated number of rows and the estimated width of each row
* `VERBOSE`
* `BUFFERS` - Include information on buffer usage. Shared block hits, read, dirtied and written (and temp). A hit means that a read was avoided because the block was found already in cache when needed. Shared blocks contain data from regular tables and indexes; local blocks contain data from temporary tables and indexes. Temporary blocks contain short-term working data used in sorts, hashes, Materialize plan nodes, and similar cases. 
* `FORMAT JSON` - Can be TEXT, XML, JSON, or YAML. Default to TEXT.

### EXPLAIN Basics

* The structure of a query plan is a tree of plan nodes.
* Nodes at the bottom level of the tree are scan nodes: they return raw rows from a table
* Different scan nodes for different access methods: sequential scans, index scans, and bitmap index scans
* If the query requires joining, aggregation, sorting, or other operations on the raw rows, then there will be additional nodes above the scan nodes to perform these operations
* There are also non-table row sources, such as `VALUES` clauses and set-returning functions in `FROM`, which have their own scan node types.

Example 1. Simple select

    EXPLAIN SELECT * FROM article;

    Seq Scan on article  (cost=0.00..151.07 rows=10407 width=4)

* `Seq Scan on article`: Since this query has no WHERE clause, it must scan all the rows of the table, so the planner has chosen to use a simple sequential scan plan
* `cost=0.00..151.07 rows=10407 width=4`:
    - `0.00` - Estimated start-up cost - sorting - none in this case
    - `151.07` - Estimated total cost - assumption of running to completion - all available rows returned
    - `rows=10407` - Estimated number of rows output by this plan node - if run to completion
    - `width=4` - Estimated average width of rows output by this plan node (in bytes).

About costs and rows:

* The costs are measured in arbitrary units determined by the planner's cost parameters
* Traditional practice is to measure the costs in units of disk page fetches; that is, `seq_page_cost` is conventionally set to `1.0`
* The cost of an upper-level node includes the cost of all its child nodes
* The cost does not consider the time spent transmitting result rows to the client - only what the planner cares about
* The rows value is a little tricky because it is not the number of rows processed or scanned by the plan node, but rather the number emitted by the node.

The rows can be derived by running:

    SELECT relpages, reltuples FROM pg_class WHERE relname = 'article';

    relpages, reltuples
    46, 10186

    estimated_cost = (disk pages read * seq_page_cost) + (rows scanned * cpu_tuple_cost).
    By default, seq_page_cost is 1.0 and cpu_tuple_cost is 0.01
    estimated_cost = (46 * 1) + (10186 * 0.01) = 147.86 (quite close to the 151)

Example 2. Simple condition

    EXPLAIN SELECT * FROM article WHERE article_num < 700000;

    Seq Scan on article  (cost=0.00..177.09 rows=6333 width=4)
      Filter: (article_num < 700000)

* This means that the plan node checks the condition for each row it scans, and outputs only the ones that pass the condition
* The estimate of output rows has been reduced because of the WHERE clause
* The scan will still have to visit all 10000 rows, so the cost hasn't decreased
* Cost has gone up a bit (by 10000 * cpu_operator_cost, to be exact) to reflect the extra CPU time spent checking the WHERE condition
* The estimate can change after each ANALYZE command, because the statistics produced by `ANALYZE` are taken from a randomized sample of the table

Example 3. More restictive condition

    EXPLAIN SELECT * FROM article WHERE article_num < 130000;

    Index Only Scan using article_pkey on article  (cost=0.29..20.72 rows=479 width=4)
      Index Cond: (article_num < 130000)

* the child plan node visits an index to find the locations of rows matching the index condition

> Fetching rows separately is much more expensive than reading them sequentially, but because not all the pages of the table have to be visited, this is still cheaper than a sequential scan.

Example 4. Multiple condition where clause

    EXPLAIN SELECT * FROM tenk1 WHERE unique1 < 100 AND stringu1 = 'xxx';

                                    QUERY PLAN
    -------------------------------------------------------------------​-----------
    Bitmap Heap Scan on tenk1  (cost=5.04..229.43 rows=1 width=244)
        Recheck Cond: (unique1 < 100)
        Filter: (stringu1 = 'xxx'::name)
        ->  Bitmap Index Scan on tenk1_unique1  (cost=0.00..5.04 rows=101 width=0)
                Index Cond: (unique1 < 100)

* The output rows can decrease but cost stay the same as it still needs to visit the same amount of rows
* The filter cannot be applied to an index condition - as the index is only 1 column

The index sometimes already applies the requested ordering so the query plan will be the same ordered as unorder.
Rows are acquired in index order.

Example 5. Ordering

    EXPLAIN SELECT * FROM catalogue_category ORDER BY category_id;

    Sort  (cost=71.69..74.03 rows=938 width=92)
      Sort Key: category_id
      ->  Seq Scan on catalogue_category  (cost=0.00..25.38 rows=938 width=92)

* Ordering is implicit (with index order) or explicitly above

Example 6. Incremental sort

    EXPLAIN SELECT * FROM catalogue_category ORDER BY category_id, parent_id LIMIT 100;

    Limit  (cost=0.40..16.17 rows=100 width=92)
      ->  Incremental Sort  (cost=0.40..148.30 rows=938 width=92)
          Sort Key: category_id, parent_id
          Presorted Key: category_id
            ->  Index Scan using category__category_id_partner_unique on catalogue_category  (cost=0.28..106.09 rows=938 width=92)

* Sorting incrementally allows returning tuples before the entire result set has been sorted, which particularly enables optimizations with LIMIT queries
* It may also reduce memory usage and the likelihood of spilling sorts to disk, but it comes at the cost of the increased overhead of splitting the result set into multiple sorting batches.

Example 7. AND or OR on combination of indexes

```
EXPLAIN SELECT * FROM tenk1 WHERE unique1 < 100 AND unique2 > 9000;

                                     QUERY PLAN
-------------------------------------------------------------------​------------------
 Bitmap Heap Scan on tenk1  (cost=25.08..60.21 rows=10 width=244)
   Recheck Cond: ((unique1 < 100) AND (unique2 > 9000))
   ->  BitmapAnd  (cost=25.08..25.08 rows=10 width=0)
         ->  Bitmap Index Scan on tenk1_unique1  (cost=0.00..5.04 rows=101 width=0)
               Index Cond: (unique1 < 100)
         ->  Bitmap Index Scan on tenk1_unique2  (cost=0.00..19.78 rows=999 width=0)
               Index Cond: (unique2 > 9000)
```

Example 8. Joins

```
EXPLAIN SELECT *
FROM tenk1 t1, tenk2 t2
WHERE t1.unique1 < 10 AND t1.unique2 = t2.unique2;

                                      QUERY PLAN
-------------------------------------------------------------------​-------------------
 Nested Loop  (cost=4.65..118.62 rows=10 width=488)
   ->  Bitmap Heap Scan on tenk1 t1  (cost=4.36..39.47 rows=10 width=244)
         Recheck Cond: (unique1 < 10)
         ->  Bitmap Index Scan on tenk1_unique1  (cost=0.00..4.36 rows=10 width=0)
               Index Cond: (unique1 < 10)
   ->  Index Scan using tenk2_unique2 on tenk2 t2  (cost=0.29..7.91 rows=1 width=244)
         Index Cond: (unique2 = t1.unique2)
```

* Nested loop join node with 2 table scans as inputs
* There is an outer scan with the filter condition
* Columns from the outer scan are plugged into the inner scan

Example 9. Materialize

```
EXPLAIN SELECT *
FROM tenk1 t1, tenk2 t2
WHERE t1.unique1 < 100 AND t1.unique2 = t2.unique2;

                                        QUERY PLAN
-------------------------------------------------------------------​-----------------------
 Hash Join  (cost=230.47..713.98 rows=101 width=488)
   Hash Cond: (t2.unique2 = t1.unique2)
   ->  Seq Scan on tenk2 t2  (cost=0.00..445.00 rows=10000 width=244)
   ->  Hash  (cost=229.20..229.20 rows=101 width=244)
         ->  Bitmap Heap Scan on tenk1 t1  (cost=5.07..229.20 rows=101 width=244)
               Recheck Cond: (unique1 < 100)
               ->  Bitmap Index Scan on tenk1_unique1  (cost=0.00..5.04 rows=101 width=0)
                     Index Cond: (unique1 < 100)
```

* The Materialize node saves the data in memory as it's read, and then returns the data from memory on each subsequent pass
* hash join - rows of one table are entered into an in-memory hash table

Example 10. Merge join

```
EXPLAIN SELECT *
FROM tenk1 t1, onek t2
WHERE t1.unique1 < 100 AND t1.unique2 = t2.unique2;

                                        QUERY PLAN
-------------------------------------------------------------------​-----------------------
 Merge Join  (cost=198.11..268.19 rows=10 width=488)
   Merge Cond: (t1.unique2 = t2.unique2)
   ->  Index Scan using tenk1_unique2 on tenk1 t1  (cost=0.29..656.28 rows=101 width=244)
         Filter: (unique1 < 100)
   ->  Sort  (cost=197.83..200.33 rows=1000 width=244)
         Sort Key: t2.unique2
         ->  Seq Scan on onek t2  (cost=0.00..148.00 rows=1000 width=244)
```

* Merge join requires its input data to be sorted on the join keys
* **Sequential-scan-and-sort frequently beats an index scan for sorting many rows - because of the nonsequential disk access required by the index scan**

`EXPLAIN` is all about what the planner thinks is best

### EXPLAIN ANALYZE

* With this option, EXPLAIN actually executes the query.
* Displays the true row count and true run time along with the estimates
* Note that the `actual time` values are in milliseconds of real time - cost is arbitary so they are unlikely to match up.

```
EXPLAIN ANALYZE SELECT *
FROM tenk1 t1, tenk2 t2
WHERE t1.unique1 < 10 AND t1.unique2 = t2.unique2;

                                                           QUERY PLAN
-------------------------------------------------------------------​--------------------------------------------------------------
 Nested Loop  (cost=4.65..118.62 rows=10 width=488) (actual time=0.128..0.377 rows=10 loops=1)
   ->  Bitmap Heap Scan on tenk1 t1  (cost=4.36..39.47 rows=10 width=244) (actual time=0.057..0.121 rows=10 loops=1)
         Recheck Cond: (unique1 < 10)
         ->  Bitmap Index Scan on tenk1_unique1  (cost=0.00..4.36 rows=10 width=0) (actual time=0.024..0.024 rows=10 loops=1)
               Index Cond: (unique1 < 10)
   ->  Index Scan using tenk2_unique2 on tenk2 t2  (cost=0.29..7.91 rows=1 width=244) (actual time=0.021..0.022 rows=1 loops=10)
         Index Cond: (unique2 = t1.unique2)
 Planning time: 0.181 ms
 Execution time: 0.501 ms
```

* The thing that's usually most important to look for is whether the estimated row counts are reasonably close to reality

Extra info on sort and hash nodes:

* The Sort node shows the sort method used (in particular, whether the sort was in-memory or on-disk) and the amount of memory or disk space needed.
* The Hash node shows the number of hash buckets and batches as well as the peak amount of memory used for the hash table.

```
EXPLAIN ANALYZE SELECT *
FROM tenk1 t1, tenk2 t2
WHERE t1.unique1 < 100 AND t1.unique2 = t2.unique2 ORDER BY t1.fivethous;

                                                                 QUERY PLAN
-------------------------------------------------------------------​-------------------------------------------------------------------​------
 Sort  (cost=717.34..717.59 rows=101 width=488) (actual time=7.761..7.774 rows=100 loops=1)
   Sort Key: t1.fivethous
   Sort Method: quicksort  Memory: 77kB
   ->  Hash Join  (cost=230.47..713.98 rows=101 width=488) (actual time=0.711..7.427 rows=100 loops=1)
         Hash Cond: (t2.unique2 = t1.unique2)
         ->  Seq Scan on tenk2 t2  (cost=0.00..445.00 rows=10000 width=244) (actual time=0.007..2.583 rows=10000 loops=1)
         ->  Hash  (cost=229.20..229.20 rows=101 width=244) (actual time=0.659..0.659 rows=100 loops=1)
               Buckets: 1024  Batches: 1  Memory Usage: 28kB
               ->  Bitmap Heap Scan on tenk1 t1  (cost=5.07..229.20 rows=101 width=244) (actual time=0.080..0.526 rows=100 loops=1)
                     Recheck Cond: (unique1 < 100)
                     ->  Bitmap Index Scan on tenk1_unique1  (cost=0.00..5.04 rows=101 width=0) (actual time=0.049..0.049 rows=100 loops=1)
                           Index Cond: (unique1 < 100)
 Planning time: 0.194 ms
 Execution time: 8.008 ms
```

Another type of extra information is the number of rows removed by a filter condition:

```
EXPLAIN ANALYZE SELECT * FROM tenk1 WHERE ten < 7;

                                               QUERY PLAN
-------------------------------------------------------------------​--------------------------------------
 Seq Scan on tenk1  (cost=0.00..483.00 rows=7000 width=244) (actual time=0.016..5.107 rows=7000 loops=1)
   Filter: (ten < 7)
   Rows Removed by Filter: 3000
 Planning time: 0.083 ms
 Execution time: 5.905 ms
```

* These counts can be particularly valuable for filter conditions applied at join nodes

> The planner may think that a sample table is too small to bother with an index scan and do a sequential

#### BUFFERS

```
EXPLAIN (ANALYZE, BUFFERS) SELECT * FROM tenk1 WHERE unique1 < 100 AND unique2 > 9000;

                                                           QUERY PLAN
-------------------------------------------------------------------​--------------------------------------------------------------
 Bitmap Heap Scan on tenk1  (cost=25.08..60.21 rows=10 width=244) (actual time=0.323..0.342 rows=10 loops=1)
   Recheck Cond: ((unique1 < 100) AND (unique2 > 9000))
   Buffers: shared hit=15
   ->  BitmapAnd  (cost=25.08..25.08 rows=10 width=0) (actual time=0.309..0.309 rows=0 loops=1)
         Buffers: shared hit=7
         ->  Bitmap Index Scan on tenk1_unique1  (cost=0.00..5.04 rows=101 width=0) (actual time=0.043..0.043 rows=100 loops=1)
               Index Cond: (unique1 < 100)
               Buffers: shared hit=2
         ->  Bitmap Index Scan on tenk1_unique2  (cost=0.00..19.78 rows=999 width=0) (actual time=0.227..0.227 rows=999 loops=1)
               Index Cond: (unique2 > 9000)
               Buffers: shared hit=5
 Planning time: 0.088 ms
 Execution time: 0.423 ms
```

> The numbers provided by `BUFFERS` help to identify which parts of the query are the most I/O-intensive

Remember `ANALYSE` will run the query so best to rollback for queries that change data:

```
BEGIN;

EXPLAIN ANALYZE UPDATE tenk1 SET hundred = hundred + 1 WHERE unique1 < 100;

                                                           QUERY PLAN
-------------------------------------------------------------------​-------------------------------------------------------------
 Update on tenk1  (cost=5.08..230.08 rows=0 width=0) (actual time=3.791..3.792 rows=0 loops=1)
   ->  Bitmap Heap Scan on tenk1  (cost=5.08..230.08 rows=102 width=10) (actual time=0.069..0.513 rows=100 loops=1)
         Recheck Cond: (unique1 < 100)
         Heap Blocks: exact=90
         ->  Bitmap Index Scan on tenk1_unique1  (cost=0.00..5.05 rows=102 width=0) (actual time=0.036..0.037 rows=300 loops=1)
               Index Cond: (unique1 < 100)
 Planning Time: 0.113 ms
 Execution Time: 3.850 ms

ROLLBACK;
```

#### Caveats

* EXPLAIN results should not be extrapolated to situations much different from the one you are actually testing; for example, results on a toy-sized table cannot be assumed to apply to large tables. 
* Since no output rows are delivered to the client, network transmission costs and I/O conversion costs are not included
* On a table that only occupies one disk page, you'll nearly always get a sequential scan plan whether indexes are available or not

## Glossary

### Scan Operations

* Sequential Scan - reads the rows from a table in order - the fastest way of getting rows (read sequentially)
    * Postgres9.6 and onwards - can run in parrellel (Parallel Seq Scan)
* Index Scan - scans the index for rows which match a particular condition, then reads them from the table.
    * Index scan is very efficient if you only need a small proportion of the rows
    * You will see them in query plans as a result of rows being removed by a WHERE clause or rows being looked up one at a time due to a JOIN statement.
    * slower than a sequential scan if you need all rows in no particular order
* Index-Only Scan - when all the information needed is contained in the index - an index-only scan can read all the data from it, without referring to the table.

### Join Operations

More info at [pgmustard](https://www.pgmustard.com/docs/explain)

Example:

```
"Bitmap Heap Scan on public.catalogue  (cost=600.39..39634.17 rows=546 width=20) (actual time=136.990..164.021 rows=1 loops=1)"
"  Output: catalogue_key"
"  Recheck Cond: (((catalogue.store_code)::text = 'OR70'::text) AND (catalogue.catalogue_version = 662))"
"  Filter: (417 = ANY (catalogue.taxonomy_parents))"
"  Rows Removed by Filter: 9419"
"  Heap Blocks: exact=755"
"  Buffers: shared hit=205 read=658"
"  I/O Timings: read=3844.232"
"  ->  Bitmap Index Scan on ix_multi_catalogue_version_store_code_taxonomy_parents  (cost=0.00..600.26 rows=11170 width=0) (actual time=122.228..122.228 rows=9420 loops=1)"
"        Index Cond: (((catalogue.store_code)::text = 'OR70'::text) AND (catalogue.catalogue_version = 662))"
"        Buffers: shared hit=4 read=104"
"        I/O Timings: read=118.668"
"Query Identifier: -3481533847414450327"
"Planning Time: 0.150 ms"
"Execution Time: 164.061 ms"
```

Buffers: shared hit means from cache, read=104

## Sources

* [Postgres docs: EXPLAIN](https://www.postgresql.org/docs/current/sql-explain.html)
* [Postgrs docs: Using EXPLAIN](https://www.postgresql.org/docs/current/using-explain.html)
* [Dalibo: Online explain visualiser](https://explain.dalibo.com/)
* [PgMustard: Explain Glossary](https://www.pgmustard.com/docs/explain)
