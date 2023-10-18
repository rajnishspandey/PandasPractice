#Group the DataFrame by the "Fare"

import pandas as pd

df = pd.read_csv('titanic.csv')

#print(df)
pd.options.display.max_columns = None #to dispaly all the columns values in the screen

grouped = df.groupby(by ="Fare",dropna=False).sum()
print(grouped)
