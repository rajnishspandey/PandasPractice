#Replace values in Pandas dataframe using regex

import pandas as pd

# Let's create a Dataframe
df = pd.DataFrame({'City':['New York', 'Parague', 'New Delhi', 'Venice', 'new Orleans'],
                    'Event':['Music', 'Poetry', 'Theatre', 'Comedy', 'Tech_Summit'],
                    'Cost':[10000, 5000, 15000, 2000, 12000]})

# Let's create the index
index_ = [pd.Period('02-2018'), pd.Period('04-2018'),
          pd.Period('06-2018'), pd.Period('10-2018'), pd.Period('12-2018')]

#set index 
df.index = index_

print(df)

# replace the matching strings
df_updated = df.replace(to_replace ='[nN]ew', value = 'New_', regex = True)

print("Updated DataFrame :\n")
print(df_updated)