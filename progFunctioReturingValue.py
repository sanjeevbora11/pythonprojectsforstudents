#Function returning value
def func1():
    return 5 #returns integer literal 5
def func2():
    return 6+4
def sum(a,b):
    return a+b
#Unreachable function satement: statement of function doesn't execute when
#we use them after return statement
def multiply(num1,num2):
    return num1*num2  #control jumps from this statement to print(multiply(4,5)
    print("Sum of num1 and num2=",num1+num2)#Unreachable statement
def multiply1(num1,num2):
    print("Sum of num1 and num2=",num1+num2)
    return num1*num2  

print(func1())
print(func2())
print(sum(5,4)>6)
print(sum(2,3)>10)
print(multiply(4,5))
print(multiply1(4,5))
