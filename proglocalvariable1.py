#Program to explain local variables
a=3
b=4
def func1(num1,num2):
    s=num1+num2
    n=20 #n is a local variable
    
    return s
sum1=func1(a,b)
print(n)#Error because n is not defined
print("Sum of a and b is ",sum1)
