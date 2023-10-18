#Load Data: Read a CSV file (e.g., "titanic.csv") into a pandas DataFrame and display the first 5 rows.

import pandas as pd

df =  pd.read_csv('titanic.csv')

df = df.head(5)
print(df)
