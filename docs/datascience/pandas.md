---
author: ''
category: Datascience
date: '2020-06-14'
summary: ''
title: Pandas
---
# Pandas Notes

## Getting Started

Install [Anaconda](https://www.anaconda.com/download/) has packages that you need for datascience. It helps people that are not software developers.

* numpy
* pandas
* matplotlib
* cborne
* jupyter

## Jupyter Notebooks

Let you create and share documents that have live code, explanatory text and visualisations.

Open jupyter from anaconda navigator or use `jupyter notebook` from your cli.

Once in jupyter click `File -> New -> Notebook -> Python3`

Some important shortcuts:

* `Esc + m`: Turns a cell into markdown mode
* `Shift + Enter`: Turns a cell into code mode
* `Esc + b`: Insert empty code cells below current code cell
* `Esc + a`: Insert empty code cells above current code cell

> When you are within the paramteres of a function you can hit `Shift + Tab` and it will show you documentation.

## Using Pandas

Use

    import pandas

or

    # Accepted shortening
    import pandas as pd

### View versions

View version of pandas and dependencies

    pandas.show_versions()

To view just the pandas versions:

    pandas.__version__

### View help

To view the help on any function use:

    pd.<function_name>?

Eg.

    pd.read_csv?

## Dataframes

A dataframe is like a 2 dimensional array, a table with rows and columns.

Read and show the first few rows with:

    olympic_data = pd.read_csv('data/olympics.csv', skiprows=4)
    olympic_data.head()

## Series

A series is a 1 deimensional array of indexed data

* Supports integer and label based indexing

### Accessing a single series can use either square bracket or dot notation

    data_frame['series_name']

or

    data_frame.series_name

Dot notation will not work if there is a space in the series name

### Accessing multiple series

    data_frame[['series_name1', 'series_name2']]

## Tips

Check if you are working with a series or dataframe

    type(data_frame)
    pandas.core.frame.DataFrame

    type(data_frame.series_name)
    pandas.core.series.Series

    type(data_frame[['series_name1', 'series_name2']])
    pandas.core.frame.DataFrame

## Data Input and Validation

Reading data:

* read_excel()
* read_json()
* read_sql_table()
* read_csv()

## Shape

The shape attribute returns a tuple representing the dimensionality of the data

    olympic_data.shape
    (29216, 10)

It returns (`rows`, `columns`)

Get just rows

    olympic_data.shape[0]
    29216

Get just columns

    olympic_data.shape[1]
    10

## Head and Tail

Show the first `n` rows at the start and the end, by default 5.

It is the first thing you should do, examine the data.

    olympic_data.head()

and

    olympic_data.tail()

## Info()

Shows entries, data type and number of non-null entries for each series

For real world usage there will be missing data

    olympic_data.info()
    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 29216 entries, 0 to 29215
    Data columns (total 10 columns):
    City            29216 non-null object
    Edition         29216 non-null int64
    Sport           29216 non-null object
    Discipline      29216 non-null object
    Athlete         29216 non-null object
    NOC             29216 non-null object
    Gender          29216 non-null object
    Event           29216 non-null object
    Event_gender    29216 non-null object
    Medal           29216 non-null object
    dtypes: int64(1), object(9)
    memory usage: 2.2+ MB

## Basic Analysis

### value_count()

Returns a series object counting all the unique values.
The first value is the most frequently occuring element, to reverse set the `ascending` to True.
The missing data values (`NA`) will be dropped by default, with `dropna=True`

To view the nubmer of medals given out per edition:

    olympic_data.Edition.value_counts()

    2008    2042
    2000    2015
    2004    1998
    1996    1859
    1992    1705
    1988    1546
    1984    1459
    ...

To count the number of medals per gener

    olympic_data.Gender.value_counts()

    Men      21721
    Women     7495
    Name: Gender, dtype: int64

## sort_values()

Sorts values in a series. You are sorting by asceding order by default, by default the missing data is added at the end.

    athletes = olympic_data.Athlete.sort_values()

To sort by two rows, say the earlist edition and names from A to Z.

    olympic_data.sort_values(by=['Edition', 'Athlete'])

## Boolean Indexing

Boolean vectors can be used to filter data. 

* `AND` will use `&`
* `OR` will use `|`
* `NOT` will use `~`

Multiple conditions must be grouped in brackets

View all records that got a gold medal

    olympic_data.Medal == 'Gold'

Returns

    0         True
    1        False
    2        False
    3         True
    4        False
    5        False
    6         True
    7        False

To select a dataframe where all the athletes won gold

    olympic_data[olympic_data.Medal == 'Gold']

Multiple conditions

    olympic_data[(olympic_data.Medal == 'Gold') & (olympic_data.Gender == 'Women')]

## String Handling

Using python's `str` there are a number of built-in methods like `str.contains()`, `str.startswith()` and `str.isnumeric()`

Finding **Flo Jo** we search for florence:

    olympic_data.Athlete.str.contains('Florence')

this gives us a boolean series, which we must plug into the dataframe

    olympic_data[olympic_data.Athlete.str.contains('Florence')]

## Basic Plotting

[Matplotlib](https://matplotlib.org/) makes easy things easy and hard thing possible. You can generate plots, histograms, bar charts, error charts with a few lines of code.

### Importing

    import matplotlib.pyplot as plt

the merger command: `%matplotlib inline` allows the output of the matplotlib command to be executed within the jupyter notebook. The resulting plots are also stored in the notebook.

You will want to explicitly set the axis or figure objects that you will be using on more complex plots.
The shorter method is the `pyplot` method of `matplotlib`

### Plot types

By default the plot is a link

    plot(kind='line')
    plot(kind='bar')
    plot(kind='barh')
    plot(kind='pie')

**plot(kind='line')**

Tracking changes over a period of time
Easier to compare changes with different groups and small changes

**plot(kind='bar')**

Track changes over time over different groups. Best when changes are large over time.

**plot(kind='barh')**

Horizontal bar graph, axis rotated.

**plot(kind='pie')**

Best for comparing parts of a whole. Don't show changes over time.

#### Example

    first_olympics.Sport.value_counts().plot(kind='line');

**Add the `;` to the end of that line to suppress: `<matplotlib.axes._subplots.AxesSubplot at 0x117bf6da0>`**

### Plot Colours

You can set the colour as keyword arguments to the `plot()` command

Eg.

    plot(color='red')

More information on [matplotlib colours](https://matplotlib.org/gallery/index.html#color-examples)

### Figure Size

Tuple given as keyword argument to `plot()` to specify the width and height


Eg.

    first_olympics.Sport.value_counts().plot(figsize=(15, 3));

Apparently the numbers represent inches (great news!)

### Colourmaps

Find a good representation of your data. Is there an intuitive colour scheme?
Eg. Gold, Silver and Bronze for medal winners. Blue for male, pink for female.

Classes of colur maps:

* sequential - representing ordered data
* diverging  - information deviates around a middle value
* Qualitative - No ordering or relationship (miscellaneous)

Eg.

    first_olympics.Sport.value_counts().plot(kind='pie', colormap='Pastel1')

_The `color` parameter for pie charts does not exist_

## Seaborn

Visualisation library based on `matplotlib`

Why:

* Attractive statistical plots
* A complement and not a substitute to matplotlib
* Integrates well with pandas

Take a look at the [seaborn examples](https://seaborn.pydata.org/examples/)

### Countplot()

    seaboard.countplot(
        data=source_dataframe,
        hue=categorical_variable_colours,
        order=sequence_of_categorical_variables,
        palette=colors_for_levels
    )

### Seaborn vs Matplotlib

* Matplotlib - Short scripts with pyplot with simple plot types
* Seaborn - Statistical or categorical data needing advanced plots

### Importing 

    import seaborn as sns

## Indexing

* The index is an immutable array (that is it cannot be changed in place and will need to be recreated)
* Indexing allows you to access a row or column using a label

    type(olympic_data.index)
    pandas.core.indexes.range.RangeIndex

Immutable

    olympic_data.index[100] = 5
    TypeError: Index does not support mutable operations

### setindex()

Which of series is the index

    olympic_data.set_index('Athlete')

You can change the index inplace with

    olympic_data.set_index('Athlete', inplace=True)

or

    athlete_index_df = olympic_data.set_index('Athlete')

### Reset the index

Return the dataframe to the integer index

    olympic_data.reset_index(inplace=True)

### sort_index()

Speeds up data access on large datasets. Sort objects by a label along the axis.

    athlete_index_df.sort_index(inplace=True)
    athlete_index_df.head()

Descending order:

    athlete_index_df.sort_index(inplace=True, ascending=False)
    athlete_index_df.head()

### loc[]

Label based index, selecting via the label.

Raises a `KeyError` when the items are not found

    olympic_data.loc['BOLT, Usain']

**The index has to be the type you are searching**

Although the two below are synonymous:

    olympic_data[olympic_data.Athlete == 'BOLT, Usain']
    olympic_data.loc[olympic_data.Athlete == 'BOLT, Usain']

### iloc[]

Integer based indexing

Allows for traditional pythonic slicing

View an item:

    olympic_data.iloc[1700]
    Athlete         RABOT, Pierre
    City                   London
    Edition                  1908
    Sport                 Sailing
    Discipline            Sailing
    NOC                       FRA
    Gender                    Men
    Event                      6m
    Event_gender                X
    Medal                  Bronze
    Name: 1700, dtype: object

Return multiple items:

    olympic_data.iloc[[1542, 2390, 6001, 15000]]

Show 2nd to 5th:

    olympic_data.iloc[1:4]

## Group by

* Split a dataframe into groups based on some criteria
* Applies a function to each group independently
* Combines the results into a dataframe

Creating a group by object only verifies that you have passed a valid mapping

The group by object is not a dataframe but a group of dataframes in a dict-like structure

    type(olympic_data.groupby('Edition'))
    pandas.core.groupby.groupby.DataFrameGroupBy

View the group by as a list:

    list(olympic_data.groupby('Edition'))

### Iterate through a Group

Each group is a dataframe

    for key, group in olympic_data.groupby('Edition'):
        print(key)

### Groupby Computations

* `GroupBy.size()`
* `GroupBy.count()`
* `GroupBy.first()`, `GroupBy.last()`
* `GroupBy.head()`, `GroupBy.tail()`
* `GroupBy.mean()`
* `GroupBy.max()`, `GroupBy.min()`

`agg()` allows multiple statistics in one calculation per group

Eg.

    olympic_data.loc[olympic_data.Athlete == 'LEWIS, Carl'].groupby('Athlete').agg({'Edition': ['min', 'max', 'count']})

## Reshaping

Stack function allows you to set inner columns as rows

If you have grouped by data and want to view it like the original data frame use:

    g = mw.groupby(['NOC', 'Gender', 'Discipline', 'Event']).size()

### Stack

Returns a dataframe or series, by default `dropna=True` so you won't have any missing values

A stack returns a dataframe or series with a new innermost layer of rows

**Stack returns a taller dataframe**

    df.stack(['Event'])

### unstack

Returns a dataframe or series

Sometimes it makes sense for `NA` values to be 0. Meaning no medals are won for that event.

**Returns a wider dataframe**

    df.unstack('Gender')

## Data Visualisations

    sns.heatmap(sorted_medal_data)

### Create our own colourmaps

    from matplotlib.colors import ListedColormap

Seaborn uses palette.
View the current colour palette:

    sns.color_palette()

View it on a plot:

    sns.palplot(sns.color_palette())

Gold silver bronze:

    gold_silver_bronze = ['#dbb40c', '#c5c9c7', '#a87900']
    sns.palplot(gold_silver_bronze)

Create the colourmap:

    gsb_colourmap = ListedColormap(sns.color_palette(gold_silver_bronze))
    top_5.plot(kind='bar', figsize=(20, 10), colormap=gsb_colourmap);

## Example Adding a column

    most_medals = us_medals.groupby(['Edition', 'Athlete', 'Medal']).size().unstack('Medal', fill_value=0)
    most_medals['Total'] = most_medals['Gold'] + most_medals['Silver'] + most_medals['Bronze']

### Sort by group

    # Reset index
    most_medals.reset_index(inplace=True)
    for year, group in most_medals.groupby('Edition'):
        print(group.sort_values('Total', ascending=False)[:1])

    # Create a list and then create a dataframe
    tu = [group.sort_values('Total', ascending=False)[:1] for year, group in most_medals.groupby('Edition')]
    tu
    top = pd.DataFrame()
    for element in tu:
        top = top.append(element)
    top

Source: [Lynda Pandas for Datascience](https://www.lynda.com/Data-Science-tutorials/pandas-Essential-Training/636129-2.html)