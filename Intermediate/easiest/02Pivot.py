#Pivot the DataFrame

import pandas as pd

df = pd.read_csv('titanic.csv')

print(df)

pivot_table = df.pivot_table(columns="Fare", values="Age", aggfunc="sum")
print(pivot_table)
