#Filter and display rows where the "Age" is greater than 30

import pandas as pd

df = pd.read_csv('titanic.csv')
#print(df)

#to display all the column names with data
pd.options.display.max_columns = None
#print(df)

df = df[df.Age>30]
print(df)

#select only the column names of DataFrame
print(df.columns.tolist())
