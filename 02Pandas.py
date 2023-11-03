#Creating DataFrame from dict of narray/lists
#importing pandas
import pandas as pd

#data initialization
data = {
    'Category':['Array', 'Stack', 'Queue'],
    'Marks':[20, 21, 19]
}

#creating DataFrame
df = pd.DataFrame(data)
#output
print(df)

#check the transpose of the output
print(df.T)

print(df[:2].T)

#changing the index value
df.index = [1,2,3]
print(df)

print(df[0:])