import pandas as pd

data = {
    "ID":[1,2,3,1],
    "Name":["Rajnish","Manish","Ajay",""],
    "Rank":[1,2,3,4],
}

student = pd.DataFrame(data)
#select * from student
print(student, end="\n\n")

#get the structure of the table 
#describe tableName

print(student.info(), end="\n\n")

#get the statistics of the table columns
print(student.describe(), end="\n\n")