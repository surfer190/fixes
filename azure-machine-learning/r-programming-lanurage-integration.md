# The R Programming Lanuage and integrating it with Microsoft Azure Machine Learning

## What is R?

R is an open source statistical programming language

CRAN The comprehensive R Archive Network is the repo for tools and libraries

## Using with Azure Machine Learning Studio

There is a module called `Execute R Script`

You can write `R` code directly in the module

The module allows 2 input datasets, an R Script and an optional zipped set of R scripts

### Principal Component Analysis (PCA)

A `Dimensionality reduction technique`: it finds a new set of variables, principal components, that are linear combinations of the original dataset and are uncorrelated with all other variables

**Note on Trained Models**: You can only visualise the results of R algorithms, you cannot use results as input to other machine learning or save as trained models

### Time Series

You can use `R Auto-ARIMA` or `R K-Nearest Neighbor` for time series data
