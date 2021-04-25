'''
void form of function- If function doesn't use return statment to return
value of variable then such type of function is called as void functions in
Python.
But in Python function returns by default None type value.
it returns None.
'''
def myfunc(num1,num2):
    s=num1+num2
    print("Sum of two numbers = ",s)
print(myfunc(3,4))
result=myfunc(10,20)
print("Value of result= ",result)
