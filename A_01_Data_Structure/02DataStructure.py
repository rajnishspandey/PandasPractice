#Create a Series containing the ages of a group of people and an index of their names. 
#Select and display the ages of individuals who are older than 30.

import pandas as pd

ages = [35, 28, 42, 31, 45]
names = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']

df= pd.Series(ages)
print(df,end="\n\n")

df = pd.Series(ages,index=names)
print(df[df>30], end="\n\n") #values

print(df>30) #True or False