#WAP to count number of lines starting with "H" in the file para.txt
myfile1=open("para.txt")
data=myfile1.readlines()
count=0
print(data)
for line in data:
    if line[0]=="H":
       count=count+1
       print(line)
print("Number of lines starting with H: ",count)
'''
data variable stores lines from a file in list.
'''
