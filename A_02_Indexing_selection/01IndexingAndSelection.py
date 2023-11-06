"""
Create a DataFrame from a dictionary with information about employees (Name, Age, Department). 
Use indexing to select and display the details of an employee by their name.
"""

import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [30, 35, 28, 32, 27],
    'Department': ['HR', 'Engineering', 'Sales', 'Marketing', 'IT']
}

# Create a DataFrame from the dictionary with employee information
df = pd.DataFrame(data)

# Set the "Name" column as the index
df.set_index('Name', inplace=True)
print(df,end="\n\n")

# Select and display the details of an employee by their name
employee_name = 'Bob'  # Replace with the name of the employee you want to display
employee_details = df.loc[employee_name]

print(employee_details)
