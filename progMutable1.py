
def func1(l1):
    l1[0]=l1[0]+10
    l1.append(30)
    
myList=[2,3,4,5,6]
print(myList)#Displays element of myList before calling function func1
func1(myList)#l1 and myList are referring same memory location
print(myList)#Displays element of myList after calling function func1
