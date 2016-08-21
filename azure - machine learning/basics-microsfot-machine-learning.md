# 4 Pillars of analytics

* Description (what happened)
* diagnostic analysis (why things happened)
* predictive (what will happen in the future)
* prescriptive (what should we do)

As you move lower **difficulty** and **value** increases

# Why is Big Data so Big?

* Data is a Competitive advantage
* New insights for smarter decision
* Traditional BI gives backward insights
* More data everyday
* More computing power

# Datascience Process

1. Define a business problem
2. Acquire and prepare the data
3. Develop model
4. Deploy model
5. Monitor model performance

## Azure Algorithms

Algorithms are baked into the modules

Difficult part is choosing which algorithm to apply in different scenarios

# Azure Studio

* Experiments - experiments saved as drafts
* Web Services - exposed by AML
* Notebooks - visualise data
* Trained models - completed models

## Module or dataset view

RHS: properties
LHS: Datasets and modules

# Components of an experiment

Creating a model creates an experiment
Experiment: Dataset + modules

# Four step model creation

1. Get Data
2. Clean Data (Preparation usually takes the longest)
3. Choose and apply learning model
4. Predict over new data

# Confusion matrix

A table used to describe the performance of a classification model where end values are known

True positive: we predict yes, and they do
True negative: we predict no, and they don't
False postive: we predict yes, but don't have disease
False negative: we predict no, but they have disease

* accuracy - how often classifier is correct
* precision - when yes, how often is it correct

# Machine learning

Class of algorithms that is Data driven
Data will define the good answer

Supervised - examples are labelled
Unsupervised - unlabelled (it clusters data into groups)

# Anomaly detection

Predicting credit card transactions has a huge number of legit ones,
and very few fraudulent.

# Classification

Supervised learning

Predicting whether a client will buy a product from us

Classification categorises into buckets, regression predicts values on a continuium.

Classifier types:
2 class classifiers - two options
multi-class classifier - three or more categories

# Binary Classification

Simplist form of machine learning


# Azure Machine Learning

You can click the little dot under a block and `visualise the data`

`Missing Values scrubber` makes sure there are no missing values

Adding an removing columns is called `projecting columns` now called `Select columns from dataset`

Sometimes you can't visualise data until you have run the experiment

`Split data` used to create 2 sets of data. One that has been trained by the machine and one that hasn't.

`Trained Model` an important module, basically you tell the algorithm what you are trying to predict

`Score Model` and `Evaluate Model` are modules that visualises ho well the model works

# Top Tips

When uploading a `csv` that is `;` semicolon seperated, you need to change it to a `,`, American style cSV otherwise Azure gives shit.
