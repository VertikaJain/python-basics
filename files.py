# Python has functions for creating, reading, updating, and deleting files.

#  open/create a file

myFile = open("myFile.txt", "w")

# get file info.
print("name: ", myFile.name)  # file name
print("Is closed: ", myFile.closed)  # is closed or not
print("opening mode: ", myFile.mode)  # read/write modes

# write to file
myFile.write("Learning python...")
myFile.write("and reactJS...") # does NOT overwrite. Appends to end of file
myFile.close()

# append to a file
myFile = open("myFile.txt", "a")
myFile.write("Also learning Machine learning!")
myFile.close()

# read from a file
myFile = open("myFile.txt", "r+")
print(myFile.read(10)) # will read the first 10 characters
print(myFile.read()) # will read the whole file after the cursor