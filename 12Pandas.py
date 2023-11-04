#Reshape a pandas DataFrame using stack,unstack and melt method

import pandas as pd

df = pd.read_csv("nba.csv")

print(df)

## reshape the dataframe using stack() method
"""
Stck()
it returns a DataFrame with an index with a new inner-most level of row labels. 
It changes the wide table to a long table
"""
df_stack = df.stack()
print(df_stack.head())

"""
unstack()
The unstack is similar to stack method, 
It also works with multi-index objects in dataframe, 
producing a reshaped DataFrame with a new inner-most level of column labels.
"""

df_unstack = df.unstack()
print(df_unstack.head())

"""
melt()
The melt in pandas reshape dataframe from wide format to long format. 
It uses the “id_vars[‘col_names’]” to melt the dataframe by column names.
"""

# it takes two columns "Name" and "Team"
df_melt = df.melt(id_vars =['Name', 'Team']) 
print(df_melt.head())