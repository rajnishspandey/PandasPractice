#Create a simple DataFrame with two columns, "Name" and "Age," containing three rows of data.
##Create a DataFrame from a dictionary where the keys are column names and the values are lists of data.
import pandas as pd

data = {
        "Name":['Alice', 'Bob', 'Charlie'],
        "Age" :[25, 30, 35]
    }
df = pd.DataFrame(data)
print(df)
