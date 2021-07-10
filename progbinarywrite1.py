#WAP to store list in a binary file
import pickle
l1=[23,45,45,67,78]
file1=open("Binfile1.dat","wb") #wb means to write data into binary file
pickle.dump(l1,file1)
file1.close()
print("The data is written into binary file")#this statement checks that data is

                                             #written into file or not
file2=open("Binfile1.dat","rb")#rb means read binary file
l2=pickle.load(file2)
print("File Data")
print(l2)
file2.close()
