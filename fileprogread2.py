myfile1=open("file1.txt","r")#To open a file
r1=myfile1.read(8) #reads 8 characters from a file 
print(r1)
r2=myfile1.read(7)
print(r2)
print(myfile1.read(3))
myfile1.close()
