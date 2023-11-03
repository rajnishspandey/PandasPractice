#Creating a Pandas dataframe using list of tuples

#importing pandas
import pandas as pd

# data in the form of list of tuples
data = [('Peter', 18, 7),
        ('Riff', 15, 6),
        ('John', 17, 8),
        ('Michel', 18, 7),
        ('Sheli', 17, 5) ]

df = pd.DataFrame(data, columns=["Name","Ages","Score"])
print(df)

#using from_records
print("for records")
df = pd.DataFrame.from_records(data,columns=["Name","Ages","Score"])
print(df)