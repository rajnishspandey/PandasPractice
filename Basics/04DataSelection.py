#Data Selection: Select all records where the Age is greater than a threashold Age

import pandas as pd

df = pd.read_csv('titanic.csv')

print(df)

pd.options.display.max_columns = None
df = df[df['Age']>30]
print(df)


