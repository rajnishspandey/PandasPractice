#Make a Pandas DataFrame with two-dimensional list
#importing pandas

import pandas as pd
#list1
list1 = [
    ["KEyboard",28],["xylophone",26],["Guitat",1],["Piano",2]
]
#crating the DataFrame
df = pd.DataFrame(list1)
print(df)

#lets give the column name here for each column
df.columns=["Instrument","Numnbers"]
print(df)
