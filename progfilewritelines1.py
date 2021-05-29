#Program to explain the use of writelines() method
myfile=open("file4.txt","w")
lines=["Computer Science\n","Phyics\n","Chemistry\n","Mathematics\n","English"]
myfile.writelines(lines)
myfile.close()
