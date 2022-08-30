---
author: ''
category: Datascience
date: '2018-10-30'
summary: ''
title: Pandas Change Column Data Type To Float Thousands Separator
---

Given the dataframe `df`

    df['Stake'] = df.Stake.str.replace(',', '')
    df['Stake'] = df.Stake.astype('float')
