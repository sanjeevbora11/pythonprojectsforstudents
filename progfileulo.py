'''
Write a program that reads characters from the keyboard
one by one. All lower case characters get stored inside the file Lower.txt
and all upper case characters get stored inside the file Upper.txt and all
other characters get stored
inside the others.txt.
'''
fileread=open("poem.txt","r")
filelower=open("lower.txt","w")
fileupper=open("upper.txt","w")
fileothers=open("others.txt","w")
data=fileread.read()
i=0
while i<len(data):
    if data[i].islower():
        filelower.write(data[i])
    elif data[i].isupper():
        fileupper.write(data[i])
    else:
        fileothers.write(data[i])
    i=i+1
filelower.close()


fileupper.close()
fileothers.close()
fileread.close()
