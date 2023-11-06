"""
Create a DataFrame with information about cities (City Name, Population, Area). 
Add a new column "Population Density" calculated as Population/Area.
"""

import pandas as pd

data = {
    'City Name': ['City A', 'City B', 'City C', 'City D'],
    'Population': [100000, 250000, 180000, 300000],
    'Area': [50, 75, 60, 90]
}

df = pd.DataFrame(data)
print(df,end="\n\n")

df["Population Density"] = df["Population"]/df["Area"]
print(df)