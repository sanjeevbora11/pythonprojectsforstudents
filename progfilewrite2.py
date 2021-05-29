#Program to write numeric data to a text file
fileObj=open("file3.txt","w")
fileObj.write("English\t")
eng=90
fileObj.write(str(eng) + "\n")
fileObj.write("Hindi\t")
hin=98
fileObj.write(str(hin))
fileObj.close()
