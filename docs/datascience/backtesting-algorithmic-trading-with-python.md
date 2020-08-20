---
author: ''
category: Datascience
date: '2017-10-23'
summary: ''
title: Backtesting Algorithmic Trading With Python
---
# Backtesting algorithmic trading with Python

Backtesting is the research process of applying a trading strategy idea to historical data in order to ascertain past performance

Backtesting can always take more and more factors into account and are hardly ever finished

## Types of Backtesting Systems

* Research based - Used to find out if a strategy works. Speed of development > speed of execution (matlab, R, python)
* Event-based - Carried out in the trade-execution cycle, modeling 
real world scenario. Speed of execution > speed of development (c, c++, java)

## Intial Backtester

Required parts:

* Strategy - reveives bars (Open, High, Low, CLose) on a time basis. It will produce signals (1, 0, -1) for (long, hold and short)
* Portfolio - Receives the signals from Strategy, creating positions allocated against cash. It keeps track of fees and trades and forms an `equity curve`
* Performance - Takes the portfolio object and returns useful stats about the performance. Risk return, Sharpe, Drawdown etc.

#### Source

* [Research backtesting with python in pandas](https://www.quantstart.com/articles/Research-Backtesting-Environments-in-Python-with-pandas)