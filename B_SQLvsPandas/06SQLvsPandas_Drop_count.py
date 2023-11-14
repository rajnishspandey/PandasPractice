import pandas as pd

data = {
    "ID":[1,2,1,3],
    "Name":["Rajnish","Manish","Rajnish",""],
    "Rank":[1,2,1,3],
}

student = pd.DataFrame(data)
print(student, end="\n\n")

#count of unique values
countVal = student.value_counts()
print(countVal, end="\n\n")

#drop row -  all duplicate columns
dropped = student.drop_duplicates()
print(dropped, end="\n\n")


#drop row -  all duplicate key columns
dropped = student.drop_duplicates(subset=["ID"])
print(dropped, end="\n\n")

#add single column

student["test"] = [1,2,3,1]

print(student, end="\n\n")

#rename single column
# student.rename(columns={"test":"Test"}, inplace=True)
# print(student, end="\n\n")

#rename mutli column
student.rename(columns={"test":"Test", "Rank":"Rankers"}, inplace=True)
print(student, end="\n\n")

#drop single column
# student.drop(["Test"], axis=1, inplace=True)
# print(student, end="\n\n")

# drop multi column
student.drop(["Test","ID"], axis=1, inplace=True)
print(student, end="\n\n")

