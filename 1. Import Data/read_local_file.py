# Python has in-built functions to create and manipulate files. No need to import.
# Import an file object 
my_file = open("myLocalFile.txt", mode="a+", encoding="utf-8")

#Character	Function
# r	 - Open file for reading only. Starts reading from beginning of file.
#rb	 - Open a file for reading only in binary format. 
#r+	 - Open file for reading and writing. 
# w	 - Open file for writing only. 
#wb	 - Same as 'w' but opens in binary mode.
#w+	 - Same as 'w' but also alows to read from file.
#wb+ - Same as 'wb' but also alows to read from file.
# a	 - Open a file for appending. Starts writing at the end of file. 
#ab	 - Same as 'a' but in binary format. 
#a+  - Same a 'a' but also open for reading.
#ab+ - Same a 'ab' but also open for reading.

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