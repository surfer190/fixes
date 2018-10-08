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


