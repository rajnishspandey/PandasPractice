"""
Create a DataFrame with information about products (Product Name, Price, Quantity). 
Add a new column "Total Price" that represents the product of Price and Quantity for each product.
"""

import pandas as pd

data = {
    'Product Name': ['Product A', 'Product B', 'Product C', 'Product D'],
    'Price': [10.99, 5.49, 8.95, 12.50],
    'Quantity': [20, 15, 30, 10]
}

df = pd.DataFrame(data)

print(df, end="\n\n")
df["Total"] = df["Price"] * df["Quantity"]
print(df)