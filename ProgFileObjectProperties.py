"""
The purpose of this program to explain various properties of File Object.
"""
f1=open("file1.txt","r")
print("File Name: ",f1.name)
print("File Mode: ",f1.mode)
print("File Encoding: ",f1.encoding)
print("Is File closed: ",f1.closed)
f1.close()
print("Is File Closed: ",f1.closed)
"""
Output of this program:
File Name:  file1.txt
File Mode:  r
File Encoding:  cp1252
Is File closed:  False
Is File Closed:  True
"""

