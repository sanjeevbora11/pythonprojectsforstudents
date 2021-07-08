#WAP to count number of words in a file
myfile=open("file4.txt","r")
data=myfile.readlines()
print(data)
count=0
#print(type(data[4]))
for lines in data:
    words=lines.split()
    for s in words:
       count=count+1
print(type(words))
print(type(s))
print("Number of words in a file: ",count)
myfile.close()
#split() is a string function that splits string into words and
                        #stores in list
'''
Dry run
first for loop is used to access each line from data variable.
words variable is used to separate each word from a line using split() function
of string.
separated word will store in list named words.
nested for loop is used to access each word from words variable.
'''
    
