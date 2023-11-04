#Construct a DataFrame in Pandas using string data

import pandas as pd
from io import StringIO

# wrap the string data in StringIO function
StringData = StringIO("""Date;Event;Cost
    10/2/2011;Music;10000
    11/2/2011;Poetry;12000
    12/2/2011;Theatre;5000
    13/2/2011;Comedy;8000
    """)

# let's read the data using the Pandas
df = pd.read_csv(StringData,sep=';')
print(df)

#or we can also use clipboard function as well
#copy the below string and see the output
StringData ="""Date;Event;Cost
    10/2/2011;Music;10000
    11/2/2011;Poetry;12000
    12/2/2011;Theatre;5000
    13/2/2011;Comedy;8000
    """

df = pd.read_clipboard(sep=';')
print("\n",df)