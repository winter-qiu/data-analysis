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
# Read a JSON file
import json

input_file = "json_file.json"
# regular JSON format
with open(input_file,"r") as f:
    jsondata=json.load(f)

# NJSON format
for line in open(input_file):
    line = eval(line)