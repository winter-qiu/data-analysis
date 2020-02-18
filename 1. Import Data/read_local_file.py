# Python has in-built functions to create and manipulate files. No need to import.

##############################################################################
# Read an txt file
# Import an file object 
my_file = open("myLocalFile.txt", mode="a+", encoding="utf-8")

#Character: Function
# Useful ones 
#r: Open file for reading only. Starts reading from beginning of file.
#w: Open file for writing only.
#a: Open a file for appending. Starts writing at the end of file.

# Less useful ones 
#r+: Open file for reading and writing.
#w+: Same as 'w' but also alows to read from file.
#wb+: Same as 'wb' but also alows to read from file.
#a+: Same a 'a' but also open for reading.
#ab+: Same a 'ab' but also open for reading.

# Read the whole file
file_content = my_file.read()

# Read the each line of the object
for line in my_file:
    print(line)

# or 
line1 = my_file.readline()
line2 = my_file.readline()

# Close the file object
my_file.close()

##############################################################################
# Read a csv file
import csv

input_file = "myLocalFile.csv"

# read csv into a list of list
with open(input_file) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for line in csv_reader:
        # line is a list
        print(line)

# read csv into a list of dictionary
with open(input_file, mode='r', encoding='utf-8-sig') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for line in csv_reader:
        # line is a OrderedDict, and we just conver it to regular dict
        print(dict(line))

# read csv into a pandas DataFrame       
import pandas as pd
df = pd.read_csv(input_file)

##############################################################################
# Read a JSON file
import json

input_file = "json_file.json"

# regular JSON format
with open(input_file,"r") as f:
    jsondata=json.load(f)

# NJSON format
for line in open(input_file):
    line = eval(line)