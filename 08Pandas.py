#Creating a dataframe from Pandas series

import pandas as pd

# Creating a list
author = ['Jitender', 'Purnima', 
          'Arpit', 'Jyoti']

df = pd.DataFrame(author)
print(df,"\n:##############\n")
print(type(df))

df= pd.Series(author)
print(df)
print(type(df))