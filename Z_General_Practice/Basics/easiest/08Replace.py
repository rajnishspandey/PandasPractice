#Replace all NaN values in the DataFrame with a specific value, e.g., 0.

import pandas as pd

df = pd.read_csv('titanic.csv')
#print(df)

df.fillna(0,inplace=True)
print(df)
