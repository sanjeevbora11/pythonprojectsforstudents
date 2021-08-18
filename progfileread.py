'''
Write a method in python to read the content from a text
file story.txt line by line and display the same on screen.
Write program for this.
'''
def fileread():
    fobj=open("story.txt","r")
    lines=fobj.readlines()
    for l1 in lines:
        print(l1)
    fobj.close()
filread()

