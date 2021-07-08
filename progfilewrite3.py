#To write data into a file
file1=open("F:\\Files\\file2.txt","w")#w is used for write mode and default mode is r
file1.write("List of Subject of Class XII\n")
file1.write("Computer Science\n")
file1.write("English\n")
a=90
file1.write(str(a))
file1.close()
