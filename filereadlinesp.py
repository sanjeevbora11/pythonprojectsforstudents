'''
Write a method in Python to read lines
from a text file DIARY.TXT, and display those lines,
which are starting with an alphabet ‘P’. Write program for this.
'''
def fileread():
    fobj=open("Diary.txt","r")
    lines=fobj.readlines()
    i=0
    while i<len(lines):
        if lines[i][0]=='P':
            print(lines[i])
        i=i+1
    fobj.close()
fileread()
