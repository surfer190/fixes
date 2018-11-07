# How to make column values into the column index with pandas?

I have the following data:

     	    dt 	        cls 	    cd
    0 	    1999-10-25 	845.0 	DSY
    1 	    1999-10-26 	830.0 	DSY
    2 	    1999-10-27 	830.0 	DSY
    ...
    4759 	2015-02-05 	25633.0 	MRP
    4760 	2015-02-06 	25670.0 	MRP
    4761 	2015-02-09 	25892.0 	MRP
    ...
    9261 	1991-03-06 	2.59 	USDZAR
    9262 	1991-03-07 	2.59 	USDZAR
    9263 	1991-03-08 	2.60 	USDZAR

I would like to transpose (if that is the correct word) the data on the `dt` index:

     	    dt 	        DSY 	    MRP   USDZAR
    0 	    1999-10-25 	845.0   NaN   Nan
    1 	    1999-10-26 	830.0   NaN   Nan
    2 	    1999-10-27 	830.0   Nan   Nan
    ...
    4759 	2015-02-05 	25633.0 	MRP
    4760 	2015-02-06 	25670.0 	MRP
    4761 	2015-02-09 	25892.0 	MRP
    ...
    9261 	1991-03-06 	2.59 	USDZAR
    9262 	1991-03-07 	2.59 	USDZAR
    9263 	1991-03-08 	2.60 	USDZAR


There are various ways of doing this:

Make a note on what you want your **index** to be, in my case I want the date column `dt` to be the index.
Make a note of what you want the **value** of the columns to be, in my case `cls`
Make a note of the **column** you want to use to be the the names of new columns in my case the `cd`.

Using `pivot_table`:

    df = df.pivot_table(values='cls', index=df.dt, columns='cd', aggfunc='first')

Using `pivot`:

    df = df.pivot(index=df.dt, columns='cd')['cls']

> Note there must be no duplicates for this to work

#### Source:

[StackOverflow pandas column values to columns](https://stackoverflow.com/questions/26255671/pandas-column-values-to-columns)