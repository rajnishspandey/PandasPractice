"""
Create a DataFrame with sales data, including columns for "Date," "Product," and "Revenue." 
Filter the DataFrame to show sales data for a specific date.
"""

import pandas as pd

data = {
    'Date': ['2023-11-01', '2023-11-01', '2023-11-02', '2023-11-02', '2023-11-03'],
    'Product': ['Product A', 'Product B', 'Product A', 'Product C', 'Product B'],
    'Revenue': [100.0, 75.0, 120.0, 50.0, 90.0]
}

df = pd.DataFrame(data)
print(df,end="\n\n")

specific_date_data = df[df["Date"]=="2023-11-01"]

print(specific_date_data)