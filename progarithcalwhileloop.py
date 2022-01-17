#Arithmetic Calcualtor using while loop
while True:
    print("1: Sum")
    print("2: Subtraction")
    print("3: Multiplication")
    print("4: Quotient")
    print("5: Integer quotient")
    print("6: Remainder")
    print("7: Exit")
    
    
    choice=int(input("Enter Choice"))
    if choice ==1:
        num1=int(input("Enter num1="))
        num2=int(input("Enter num2="))
        print("Sum=",num1+num2)
    elif choice==2:
        num1=int(input("Enter num1="))
        num2=int(input("Enter num2="))
        if num1>num2:
            print("Difference=",num1-num2)
        else:
            print("Difference=",num2-num1)
    elif choice==3:
        num1=int(input("Enter num1="))
        num2=int(input("Enter num2="))
        print("Multiplication=",num1*num2)
    elif choice==4:
        num1=int(input("Enter num1="))
        num2=int(input("Enter num2="))
        print("Quotient=",num1/num2)
    elif choice==5:
        num1=int(input("Enter num1="))
        num2=int(input("Enter num2="))
        print("Integer quotient=",num1//num2)
    elif choice==6:
        num1=int(input("Enter num1="))
        num2=int(input("Enter num2="))
        print("Remainder=",num1%num2)
    elif choice==7:
        break
    else:
        print("Invalid Choice")
 
