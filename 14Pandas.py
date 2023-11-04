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

for ind in df.index:
    print(df['Name'][ind], df['Stream'][ind])

for i in range(len(df)):
    print(df.loc[i, "Name"], df.loc[i, "Age"])