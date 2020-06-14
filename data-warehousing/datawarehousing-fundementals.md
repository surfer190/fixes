# Datawarehousing Fundementals

Data mining - showing unknown trends
If insights are not correlated they are useless

BI - reporting, analytics, management information, based on facts
BI - Gain insights and make trusted decisions

Advanced analytics - extracts fact

Operational data store / data lake - a staging area
Data warehouse purpose - enhance rate of knowledge acquisition and answering management questions

Can't do it on an operational system - must be done on a data warehouse.

Don't want to disturb operational data

Can't do both.
Operations must be independent.

Quick wins with data sceince scripts after a while it will use more resources.

* Components of a data warehouse?
* Mananging relationship and syncing of operational database to Datawarehousing - data duplication.

Single source of truth

KPI: COst of Capital, Headcount, Earnings per share, Cost per Unit

Users in BI:

* Strategic - Executive make more decisions
* Tactical - Data scienctists, make some decisions.
* Operational - Little to no decision.

Data warehouse Enterprise Informatin Managment Framework - Data sources, Integration, Derived Information, Semantics (Presentaiton Logic), Deliver / Manipulation / Consumption

Cube is a precalcilated values stored in memory

Star schema: A fact and dimensions around it
Fact: Quantity, cost, total
Dimensions: Time, Customer, Product, Branch

Delta processing

Surrogate key is an extra key for delta processing and seeing changed records