#Sort the DataFrame by the "Age" column in descending order.

import pandas as pd

df = pd.read_csv('titanic.csv')
#print(df)

pd.options.display.max_columns = None
print(df)

#sorting ascending order
asc_sorted_data = df.sort_values(by='Age', ascending=True)
print('ascending order DataFrame :',asc_sorted_data)

#sorting descending order
desc_sorted_data = df.sort_values(by='Age', ascending=False)
print('descending order DataFrame :',desc_sorted_data)
