#WAP to count number of digits in a file
myfile=open("file6.txt")
data=myfile.readlines()
countdigit=0
for lines in data:
    words=lines.split()
    for s in words:
        for letter in s:
            if letter.isdigit():
                countdigit=countdigit+1
print("Number of digits in a file: ",countdigit)
        
