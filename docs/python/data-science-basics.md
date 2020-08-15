---
author: ''
category: Python
date: '2017-09-11'
summary: ''
title: Data Science Basics
---
# Data Science Basics

Moving data from its raw form into a consumable form

Preparing the data into data samples, then making charts and reports

## Workflow

1. Ask the right questions
2. Frame thw question to define what needs measuring
3. Select the appropriate data for measurement and cleaning up
4. Find the patterns to extract key points

Better to select data after you have defined what you are looking to measure, to avoid over collecting or under collecting. Also depends if you want a ballpark figure or very accurate info.

* Data must contain a representative sample of all factors you are looking for
* decide whether:
    * quantities data - numeric
    * qualitative data - descriptions, smells, quality
* Decided between primary and secondary source

## Sampling Methods

* Simple Random Sampling - numbers in a hat (whole population equal chance)
* Stratified Sampling - population grouped by characterists (eg. Age) one person per group
* Cluster Sampling - groups based on characteristic
* Systematic sampling

## Libraries

        pip install matplotlib
        pip install numpy

## Numpy

Numeric Python extensions built in 2005, to increase speed and flexibility in working with larger datasets

### Built in list functions

* `sort(<list>)` - sort items of a list in-place
* `reverse(<list>)` - reverse elements in-place
* `list.count(x)` - counts number of times x appears in list
* `list.append(x)` - add item to end of list

### Filtering

Only showing records that satisfy a specified condition

### Grouping

Seperating rows with common attributes into groups

## Using Excel

Sometimes forced to use excel

        pip install openpyxl

## MatPLotLib

* Line charts - known as `plots`

### Creating a line chart

        from excel import *

        import matplotlib.pyplot as plt

        def create_line_chart(data_sample, title, exported_figure_filename):
            fig = plt.figure()
            ax = fig.add_subplot(1, 1, 1)

            prices = (sorted(map(float, data_sample)))

            x_axis_ticks = list(range(len(data_sample)))
            ax.plot(x_axis_ticks, prices, linewidth=2)
            ax.set_title(title)
            ax.set_xlim([0, len(data_sample)])
            ax.set_ylabel('Tie Price ($)')
            ax.set_xlabel('Number of Ties')

            fig.savefig(exported_figure_filename)

        create_line_chart([x[2] for x in gucci_ties[1:]], "Distribution of prices for gucci ties", 'data/line-chart.png')

## Styling

End goal of data analysis is to share your findings

## Creating PDF

1. Import PdfPages module
2. Create a new object of PdfPages with a filename
3. Save figure(s)
4. Close the object

### Code

        from matplotlib.backends.backend_pdf import PdfPages
        pp = PdfPages('foo.pdf')
        pp.savefig()
        pp.close()

## Documentation

Check the docs on:

* [Matplotlib](https://matplotlib.org/)
* [NumPy](http://www.numpy.org/)
* [Pandas](http://pandas.pydata.org/)

