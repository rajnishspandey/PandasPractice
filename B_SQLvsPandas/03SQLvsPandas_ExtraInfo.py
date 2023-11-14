import pandas as pd

import pandas as pd

data = {
    "ID":[1,2,3,1],
    "Name":["Rajnish","Manish","Ajay",""],
    "Rank":[1,2,3,4],
}

student = pd.DataFrame(data)
#select * from student
print(student, end="\n\n")