# How to read/write from files in python

from sys import argv

# open(fileName, mode)
f = open("read.txt", "w+")

# Read the contents of the file
print(f.read())

# Write to a file 
f.write("Oh hai there\n")

# Read again
print(f.read())

f.close()