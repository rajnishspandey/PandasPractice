#Data Cleaning: Handle missing values by either removing rows or filling them with appropriate values.

import pandas as pd

df = pd.read_csv('titanic.csv')

#print(df)
"""
#drop the rows where vlaue is missing in any column
df.dropna(inplace = True)
print(df)"""

#replace the value where value is null

df.fillna(0,inplace = True)
print(df)
