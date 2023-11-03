#Create a Pandas DataFrame from List of Dicts

#importing pandas
import pandas as pd

# Initialise data to lists. 
data = [{'Pandas': 'dataframe', 'For': 'using', 'Pandas': 'list'},
        {'Pandas':10, 'For': 20, 'Pandas': 30}] 

df = pd.DataFrame(data, index=[1,2])
print(df)

#using from_reocrds
print("using from_records")
df = pd.DataFrame.from_records(data, index=[3,4])
print(df)
#using from_dict

print("using from_dict")
df = pd.DataFrame.from_dict(data)
print(df)