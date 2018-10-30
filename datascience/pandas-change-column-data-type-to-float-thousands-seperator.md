# Pandas: How to change a column datatype to float from string when it has a thousands comma seperator

Given the dataframe `betting`

    betting['Stake'] = betting.Stake.str.replace(',', '')
    betting['Stake'] = betting.Stake.astype('float')