import pandas as pd

data = {
    "ID":[1,2,3],
    "Name":["Rajnish","Manish","Kanha"],
    "Profession":["Engineer","Engineer","CEO"]
}

df = pd.DataFrame(data)
print(df, end="\n\n")

#update single column single row
df.loc[df["ID"]==3,"Name"]=["Shivay"]
print(df, end="\n\n")

#update multiple columns single row
df.loc[df["ID"]==3,["Name","Profession"]]==["Atharv","CEO and CFO"]
print(df, end="\n\n")

#update single column multiple row
df.loc[df["Profession"] == "Engineer"]="Computer Scientist"
print(df, end="\n\n")

#update multiple columns multiple row
df.loc[df["Profession"] == "Engineer",["Name","Profession"]]==["Atharv","CEO and CFO"]
print(df, end="\n\n")

#update single column all row
df["ID"] = 1
print(df)
