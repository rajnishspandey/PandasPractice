#Select and display the first five rows of a DataFrame.

import pandas as pd

df = pd.read_csv('titanic.csv')
print(df)


#read the first 5 rows of DataFrame
top5 = df.head(5)
print(top5)
