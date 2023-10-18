#Find the number of rows and columns in a DataFrame.

import pandas as pd

df = pd.read_csv('titanic.csv')

num_rows, num_columns = df.shape
print(f'Number of rows: {num_rows} and columns: {num_columns}')
