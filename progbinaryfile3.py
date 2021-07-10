#WAP to store and read from/in binary file
import pickle
books={1:"Python",2:"C++",3:"C",4:"Java",5:"Node js"}
file1=open("Binaryfile2","wb")
pickle.dump(books,file1)
file1.close()
file2=open("Binaryfile2","rb")
d1=pickle.load(file2)
print(d1)
file2.close()
