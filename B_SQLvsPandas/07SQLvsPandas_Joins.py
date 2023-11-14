import pandas as pd

data1 = {
    "ID":[1,2,3],
    "Name":["Rajnish","Manish","Ajay"]
}
data2 = {
    "ID":[1,2,5],
    "Rank":[1,2,3]
}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

print(df1, end="\n\n")
print(df2, end="\n\n")

#inner join (default)
innerJoin = pd.merge(df1,df2, on="ID", how="inner") #where df1.ID=df2.ID
print(innerJoin, end="\n\n")

#left join
lefJoin = pd.merge(df1,df2, on="ID",how="left")
print(lefJoin, end="\n\n")

#right join
rightJoin = pd.merge(df1,df2, on="ID",how="right")
print(rightJoin, end="\n\n")

#full/outer join
fullJoin = pd.merge(df1,df2, on="ID", how="outer")
print(fullJoin)

#cross join
crossJoin = pd.merge(df1,df2, how="cross") #on is not required in cross join 
print(crossJoin)