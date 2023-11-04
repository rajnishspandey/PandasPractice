#Select any row from a Dataframe using iloc[] and iat[] in Pandas

import pandas as pd 
   
# Create the dataframe 
df = pd.DataFrame({'Date':['10/2/2011', '11/2/2011', '12/2/2011', '13/2/11'], 
                    'Event':['Music', 'Poetry', 'Theatre', 'Comedy'], 
                    'Cost':[10000, 5000, 15000, 2000]}) 
 
# Create an empty list 
Row_list =[] 

for i in range((df.shape[0])): 
   
    # Using iloc to access the values of  
    # the current row denoted by "i" 
    Row_list.append(list(df.iloc[i, :])) 
   
# Print the first 3 elements 
print(Row_list[:3]) 

