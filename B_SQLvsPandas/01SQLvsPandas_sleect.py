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

#filter - select name from student where id = 2
filtered = student[student["ID"]==2]["Name"].values[0]
print(filtered,end="\n\n")

#select * from student where id = 1
filtered = student[student["ID"]==1]
print(filtered,end="\n\n")

#select * from student where limit = 1
filtered = student.head(1)
print(filtered,end="\n\n")

#select distinct values
filtered = student.ID.unique() #or#student["ID"].unique()
print(filtered,end="\n\n")

#select count of distinct values
filtered = student.ID.nunique()
print(filtered,end="\n\n")

#size (total values in table row*cl)
filtered = student.size
print(filtered,end="\n\n")

