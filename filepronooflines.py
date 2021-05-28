#WAP to count number of lines in a file
fileObj=open("file1.txt",'r')
count=0
lines=fileObj.readlines()
for l in lines:
    count=count+1
print("Number of lines in a file: ",count)
fileObj.close()
