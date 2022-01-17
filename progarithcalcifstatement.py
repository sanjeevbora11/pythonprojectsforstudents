#Arithmetic Calcualtor
operator=input("Enter operator: ")
num1=int(input("Enter num1="))
num2=int(input("Enter num2="))
if operator=="+":
    print("Sum=",num1+num2)
elif operator=="-":
    if num1>num2:
        print("Difference=",num1-num2)
    else:
        print("Difference=",num2-num1)
elif operator=="*":
    print("Multiplication=",num1*num2)
elif operator=="/":
    print("Quotient=",num1/num2)
elif operator=="%":
    print("Remainder=",num1%num2)
elif operator=="//":
    print("Integer quotient=",num1//num2)
else:
    print("Invalid operator")
input()
