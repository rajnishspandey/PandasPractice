import pandas as pd

data1 = {
    "ID":[1,2,3],
    "Name":["Rajnish","Manish","Ajay"]
}
data2 = {
    "ID":[1,2,5],
    "Name":["Rajnish","Prince","Pramod"]
}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

print(df1, end="\n\n")
print(df2, end="\n\n")


#union all by single col
unionAll = pd.concat([df1["Name"],df2["Name"]],ignore_index=True)
print(unionAll, end="\n\n")

#union all by all col
unionAll = pd.concat([df1,df2],ignore_index=True)
print(unionAll, end="\n\n")

#union by single col
#union all by single col
union1 = pd.concat([df1["Name"],df2["Name"]],ignore_index=True).drop_duplicates()
print(union1, end="\n\n")

#union all by all col
union1 = pd.concat([df1,df2],ignore_index=True).drop_duplicates()
print(union1, end="\n\n")