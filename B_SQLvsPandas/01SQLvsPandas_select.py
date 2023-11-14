import pandas as pd

data = {
    "ID":[1,2,3,1],
    "Name":["Rajnish","Manish","Ajay",""],
    "Rank":[1,2,3,4],
}

student = pd.DataFrame(data)
#select * from student
print(student, end="\n\n")

#select single Column
selected_student = student["Name"]
print(selected_student, end="\n\n")

#select multiple columns
mul_selected_columns = student[["Name","ID"]]
print(mul_selected_columns, end="\n\n")



