'''
Write a method countM() in Python to read lines from a text file ‘MYSTORY.TXT’, and display
those lines, which are starting with the alphabet ‘M’.
If the “MYSTORY.TXT” contents are as follows:
My first journey to america
Myself vinayak.
Ensure to come first
Aware the things.
Mild think over it
The output of the function should be:
Count of lines starting with M is: 3
'''
def countM():
    myfile=open("mystory.txt","r")
    count=0
    data=myfile.readlines()#data is a list of lines.
    print(data)
    for filedata in data: #filedata is an individual line of list
        if filedata[0]=='M':
           count+=1
    print(count)
    myfile.close()
countM()
    
            
