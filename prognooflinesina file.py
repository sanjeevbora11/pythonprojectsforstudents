#WAP to count number of lines in a file. for this readlines() function is used
myfile=open("file6.txt")
lines=myfile.readlines()
print("File data")
print(lines)
print("Number of lines in a file: ",len(lines))
