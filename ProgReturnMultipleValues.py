'''
Returning Multiple values by Function
'''
def Calculator(num1,num2):
    return num1+num2,num1-num2,num1*num2,num1/num2,num1//num2,num1%num2
#When we use tuple type variable to store return values of function
t1=Calculator(10,3)
print(t1)
print(type(t1))
#When we use Multiple variables to store return values of function
sum,subt,mult,sdiv,idiv,rem=Calculator(20,7)
print("Sum = ",sum)
print("Subtraction= ",subt)
print("Multiplication= ",mult)
print("Simple Division Result= ",sdiv)
print("Integer Division Result= ",idiv)
print("Remainder = ",rem)
