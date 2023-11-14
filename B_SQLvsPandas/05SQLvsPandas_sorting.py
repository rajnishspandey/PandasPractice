import pandas as pd

data = {
    "ID":[1,2,1,3],
    "Name":["Rajnish","Manish","Rajnish",""],
    "Rank":[1,2,1,3],
}

student = pd.DataFrame(data)
print(student, end="\n\n")

#sorted by single column - descending order
sortedVal = student.sort_values(by="ID", ascending=False)
print(sortedVal, end="\n\n")

#sorted by single column - Ascending order
sortedVal = student.sort_values(by="ID", ascending=True)
print(sortedVal, end="\n\n")

#sort by multiple column
#sorted by single column - descending order
sortedVal = student.sort_values(by=["Name","ID"])
print(sortedVal, end="\n\n")