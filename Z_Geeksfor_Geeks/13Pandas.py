#How to iterate over rows in Pandas Dataframe
# importing pandas
import pandas as pd
 
# list of dicts
input_df = [{'name':'Sujeet', 'age':10},
            {'name':'Sameer', 'age':11},
            {'name':'Sumit', 'age':12}]
df = pd.DataFrame(input_df)
print('Original DataFrame: \n', df)

print('\nRows iterated using iterrows() : ')
for index, row in df.iterrows():
    print(row['name'], row['age'])

print('\nRows iterated using itertuples() : ')
for rows in df.itertuples():
    print(getattr(rows, 'name'), getattr(rows, 'age'))