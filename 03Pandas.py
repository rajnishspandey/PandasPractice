#Creating Pandas dataframe using list of lists

#importing pandas
import pandas as pd

#creatin data
data = [['DS', 'Linked_list', 10], ['DS', 'Stack', 9], ['DS', 'Queue', 7],
        ['Algo', 'Greedy', 8], ['Algo', 'DP', 6], ['Algo', 'BackTrack', 5], ]

#creating data frame with the column name
df = pd.DataFrame(data, columns=["Categiry","DS Type","Marks"])

#output

print(df)

