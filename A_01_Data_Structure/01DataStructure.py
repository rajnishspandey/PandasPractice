"""
Create a Pandas Series with the following data: [5, 10, 15, 20, 25] and an index of your choice. 
Find the sum of the values in the Series.
"""
import pandas as pd

data = [5, 10, 15, 20, 25]
index = [3,4,5,6,7]

df = pd.Series(data, index=index)
print(df)

sum_of_value = df.sum() #or sum(df)
print(sum_of_value)

#we can check the tpye as well
print(type(df))