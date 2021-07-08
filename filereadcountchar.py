'''
Reading from a file
read() - read() functions reads byte(character) from a file.
readline() - readline() function returns a line from a file.
readlines() - readlines() function returns all lines from a file and stores in
list.
'''
#WAP to count number of characters in a file
#count is a read operation in a file
myfile=open("file1.txt","r")
data=myfile.read()
#print(data)
count=0
for c in data:
    count=count+1
print("Number of characters in a file: ",count)
myfile.close()

