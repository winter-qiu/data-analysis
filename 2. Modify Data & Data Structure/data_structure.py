# There are plenty of types of data in python, here I will only talk about 
# few ones that are used the most.

##############################################################################
# 1. Types of variables 
a = 1 # int
b = 1.1 #float
c = "123" # str
d = [1,2,3] # list 
e = (1, "second") # tuple: 'tuple' object does not support item assignment
f = {"first": 1, "second": 2} # dict
g = [{"first": 1, "second": 2}, {"first": 3, "second": 4}] # list of dicts

##############################################################################
# 2. Get sub-data from data

# Get data from a list
d[0] # = 1
d[1] # = 2

# Get data from a tuple
e[0] # = 1
e[1] # = "second"

# Get data from a dict
f['first'] # = 1
f['second'] # = 2

# Get data from a list of dict
for x in g:
    print(x['first'])
    print(x['second'])