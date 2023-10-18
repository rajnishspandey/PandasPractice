#Data Inspection: Inspect the data by displaying data types, summary statistics, and checking for missing values.

import pandas as pd

df = pd.read_csv('titanic.csv')
#print(df)

#print the data type of the columns
print('Data types of the columns :\n',df.dtypes)

#print the statistics using describe
print('Description :\n',df.describe())

#checking the missing values
print('missing values :\n',df.isnull().sum())
