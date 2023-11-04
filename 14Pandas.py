#Different ways to iterate over rows in Pandas Dataframe

# import pandas package as pd
import pandas as pd
 
# Define a dictionary containing students data
data = {'Name': ['Ankit', 'Amit',
                 'Aishwarya', 'Priyanka'],
        'Age': [21, 19, 20, 18],
        'Stream': ['Math', 'Commerce',
                   'Arts', 'Biology'],
        'Percentage': [88, 92, 95, 70]}

df = pd.DataFrame(data)
print(df)

print("\nIterating over rows using index attribute :\n")
for ind in df.index:
    print(df['Name'][ind], df['Stream'][ind])

print("\nIterating over rows using loc function :\n")
for i in range(len(df)):
    print(df.loc[i, "Name"], df.loc[i, "Age"]) #index and lable

print("\nIterating over rows using iloc function :\n")
 
# iterate through each row and select
# 0th and 2nd index column respectively.
for i in range(len(df)):
    print(df.iloc[i, 0], df.iloc[i, 2]) #index of row and index of column

print("\nIterating over rows using iterrows() method :\n")
 
# iterate through each row and select
# 'Name' and 'Age' column respectively.
for index, row in df.iterrows():
    print(row["Name"], row["Age"])

print("\nIterating over rows using itertuples() method :\n")
# iterate through each row and select
# 'Name' and 'Percentage' column respectively.
for row in df.itertuples(index=True, name='Pandas'):
    print(getattr(row, "Name"), getattr(row, "Percentage"))

print("\nIterating over rows using apply function :\n")
 
# iterate through each row and concatenate
# 'Name' and 'Percentage' column respectively.
print(df.apply(lambda row: row["Name"] + " " +
               str(row["Percentage"]), axis=1))