'''
How statements executes in a Program when we use functions.
Control flow mechanism in a program that contains user defined functions.
Program excutes from top to bottom.
When Python interpreter gets function  header it ignores function body(statments of function)
and the
control jumps to the __main__ part of program.
1->4->5->6->1->2->3->6->7

'''
def calcSum(x,y): #1. function header
    s=x+y         #2. statment1
    return s      #3. statment2
num1=float(input("Enter first number: "))  #4. statment3
num2=float(input("Enter second number: ")) #5. statment4
sum=calcSum(num1,num2)                      #6. statement5
print("Sum of two given number is: ",sum)   #7. statement6
