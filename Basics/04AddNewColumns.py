#Add a new column, "City," to the DataFrame with values "New York," "Los Angeles," and "Chicago."

import pandas as pd

df = pd.read_csv('titanic.csv')
#print(ds)

# Define the list of city names
city_names = ["New York", "Los Angeles", "Chicago"]

# Create a new column "City" with NaN values
df['City'] = ""

# Set the values for the specified city names
df.loc[:len(city_names) - 1, 'City'] = city_names

print(df)
