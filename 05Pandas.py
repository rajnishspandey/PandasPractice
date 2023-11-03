#Create a Pandas DataFrame from List of Dicts

#importing pandas
import pandas as pd

# Initialise data to lists. 
data = [{'Pandas': 'dataframe', 'For': 'using', 'Pandas': 'list'},
        {'Pandas':10, 'For': 20, 'Pandas': 30}] 

df = pd.DataFrame(data)
print(df)