import pandas as pd

data = {
    "ID":[1,2,1,3],
    "Name":["Rajnish","Manish","Rajnish",""],
    "Rank":[1,2,1,3],
}

student = pd.DataFrame(data)
#select * from student
print(student, end="\n\n")

result = student.groupby("Name").sum()
print(result)