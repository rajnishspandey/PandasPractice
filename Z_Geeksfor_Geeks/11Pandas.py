#Mapping external values to dataframe values in Pandas

import pandas as pd

initial_data = {'First_name': ['Ram', 'Mohan', 'Tina', 'Jeetu', 'Meera'],
        'Last_name': ['Kumar', 'Sharma', 'Ali', 'Gandhi', 'Kumari'],
        'Age': [42, 52, 36, 21, 23],
        'City': ['Mumbai', 'Noida', 'Pune', 'Delhi', 'Bihar']}

df =  pd.DataFrame(initial_data)

print(df)

print("\n########")

df= pd.DataFrame(initial_data,columns=['First_name', 'Last_name','Age', 'City'])
# Create new column using dictionary
new_data = { "Ram":"B.Com",
            "Mohan":"IAS",
            "Tina":"LLB",
            "Jeetu":"B.Tech",
            "Meera":"MBBS" }

# combine this new data with existing DataFrame
df["Qualification"] = df["First_name"].map(new_data)

print(df, end ="\n\n")
#or using replace

# Create new column using dictionary
new_data2 = { "Ram":"Shyam",
            "Tina":"Riya",
            "Jeetu":"Jitender" }

df = df.replace({"First_name":new_data2})
print(df, end ="\n\n")


#or using update
# Create new column using dictionary
new_data3 = { 0:"Shyam",
            1:"Riya",
            2:"Jitender" }
 
# combine this new data with existing DataFrame
df["First_name"].update(pd.Series(new_data3))
print(df)

