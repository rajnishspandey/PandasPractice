"""
Create a DataFrame from a dictionary with information about students (Name, Age, Grade). 
Select and display only the "Name" and "Grade" columns.
"""

import pandas as pd

students = {"Name":["Rajnish","Manish","Amit","Prince"],
            "Age":[29,27,26,25],
            "Grade":['A','B','B','B+']
            }

df = pd.DataFrame(students)
print(df, end="\n\n")

selected_columns = df[["Name","Grade"]]
print(selected_columns)