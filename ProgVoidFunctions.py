def greet():
    print("Good Morning")
def quote():
    print("Stay Hungry, Stay Foolish")
    return #return returns None value and return statement supplies by Python
           # Interpreter by default
def Sum(a,b,c):
    s=a+b+c
    print("Sum of a,b,c is ",s)
    return
    
greet() #Function Calling statement
#() parenthesis
print(greet)#This statement will print address of function greet()
print(greet())#greet() is an inner function and it prints Good Morning then
#it returns None to print() i.e. outer function
quote() #function quote() is called here
print(quote())
Sum(2,3,4)
