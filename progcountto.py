#Program to count word "to" in a file
myfile1=open("file2.txt","r") 
data=myfile1.readlines()
count=0
for lines in data:
    s=lines.split()
    for word in s:
        if word=="to":
            count=count+1
print(count)

'''
data variable is used to store lines of file.
count variable use to count number of occurrences of word "to"
Outer loop is used to process each line of variable data.
lines.split() - it splits the line into words in variable s
inner for loop processes each word from a variable s(list of words)

'''

