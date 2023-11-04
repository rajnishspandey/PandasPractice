"""
Create a Series with a list of your favorite fruits and another Series with the 
number of each fruit you have. Calculate the total number of fruits you have
"""
import pandas as pd

fruits = ["Apple","Banana","Lichi","Graps","Mango"]
Quanity = [2,12,3,40,6]

series = pd.Series(Quanity, index=fruits)
print(series)
total_quantity = series.sum()
print(total_quantity)
