# importing pandas as pd
import pandas as pd

# Read the csv file and construct the 
# dataframe
df = pd.read_csv('nba.csv')

# Visualize the dataframe
print(df.head(15))

# Print the shape of the dataframe
print(df.shape)

# Filter all rows for which the player's
# age is greater than or equal to 25
df_filtered = df[df['Age'] >= 25]

# Print the new dataframe
print(df_filtered.head(15))

# Print the shape of the dataframe
print(df_filtered.shape)

# delete all rows with column 'Age' has value 30 to 40 
indexAge = df[ (df['Age'] >= 20) & (df['Age'] <= 25) ].index
df.drop(indexAge , inplace=True)
df.head(8)
