#Clean the string data in the given Pandas Dataframe
import pandas as pd

data =  {'Date':['10/2/2011', '11/2/2011', '12/2/2011', '13/2/2011'],
                   'Product':[' UMbreLla', '  maTtress', 'BaDmintoN ', 'Shuttle'],
                   'Updated_Price':[1250, 1450, 1550, 400],
                   'Discount':[10, 8, 15, 10]}

df = pd.DataFrame(data)
print(df)

#creating function
def Format_data(df):
	#  over all the iteraterows
	for i in range(df.shape[0]):

		# reassign the values to the product column
		# we first strip the whitespaces using strip() function
		# then we capitalize the first letter using capitalize() function
		df.iat[i, 1]= df.iat[i, 1].strip().capitalize()
		

# Let's call the function
Format_data(df)

# Print the Dataframe
print(df)

#or
# Using the df.apply() function on product column
df['Product'] = df['Product'].apply(lambda x : x.strip().capitalize())
 
# Print the Dataframe
print(df)