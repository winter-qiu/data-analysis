a = 1 # int
b = 1.1 # float
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

# find all the data in a column that matches one criteria 
df[df["colName1"]=="1234"] 
# or with regex
df[df["colName1"].str.contains("1234", na=False)] 
# or does not match the criteria
df[~df["colName1"].str.contains("1234", na=False)] 


##############################################################################
# Format 

# Decimals 
a = round(a, 2) # 1.00
b = int(b) # 1

# Date 
import datetime

x = datetime.datetime.now() # x = datetime.datetime(2020, 5, 17)

MonthName = x.strftime("%B") # YYYY-MM-DD: %Y-%m-%d

date = x.date() # only date, no time

# convert string to date
datetime_str = "2020-02-20"
datetime_object = datetime.datetime.strptime(datetime_str, '%Y-%m-%d')

# From date to age
def calculateAge(birthDate): 
    today = datetime.date.today() 
    age = today.year - birthDate.year - (
        (today.month, today.day) < (birthDate.month, birthDate.day)
        ) 

    return age 

birthday = datetime.datetime(1993, 12, 20)

age = calculateAge(birthday)

##############################################################################
#  
