#Select only the "Survived" column from the DataFrame.

import pandas as pd

df = pd.read_csv('titanic.csv')
#print(df)

#one way to select column
df = df.Survived
print(df)

"""
#nother way to select the column
name_column = df['Survived']
print(name_column)
"""
