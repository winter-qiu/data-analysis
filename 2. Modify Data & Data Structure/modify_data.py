a = 1 # int
d = [1,2,3] # list 
f = {"first": 1, "second": 2} # dict
g = [{"first": 1, "second": 2}, {"first": 3, "second": 4}] # list of dicts

##############################################################################
# Basic data

# assign a single value 
a = 2

# assign a value to an element in a list
d[1] = 4 # d = [1,4,3]

# assign a value to a value in dict: {key: value}
f["first"] = 5 # f = {"first": 5, "second": 2}

# change a key in dict: {key: value}
f["third"] = f.pop("first")

# assign values to a list of dict
for x in g:
    x["first"] = 5
# g = [{"first": 5, "second": 2}, {"first": 5, "second": 4}] 

##############################################################################
# Pandas
input_file = "myLocalFile.csv"

import pandas as pd
df = pd.read_csv(input_file)

# access a value in a cell
# loc: using row or col names
df.loc["rowName1","colName1"] = 100 # rowName1 coordinate with index name
# iloc: using index
df.iloc[0,0] = 100 # access value through index

# access a whole column or row
df.loc[:,"colName1"] # whole column
df.iloc[0,:] # whole row

