#Default parameters
def sum(a=0,b=0,c=0):
    return a+b+c
print(sum(2,3))#Here value of a is 2, b is 3 and c is 0
print(sum())#Here value of a,b,c is 0
print(sum(3,5,6))#Here value of a is 3,b is 5, c is 6
num1=10
num2=20
num3=40
print(sum(num1,num2))
'''
Rules for passing default parameters/arguments
Default parameters are passed from right side in function parenthesis.
Ex:
def si(p,r=5,t=1):#correct
def si(p=5000,r,t):#Incorrect because p is default parameter and after default
parameter every parameter should be default.
'''
