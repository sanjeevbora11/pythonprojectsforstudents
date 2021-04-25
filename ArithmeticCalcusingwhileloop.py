#Menu based programming using while loop
#Arithmetic calculator
while True:
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    choice=int(input("Enter Choice: "))
    if choice==1:
        num1=int(input("Enter num1= "))
        num2=int(input("Enter num2= "))
        s=num1+num2
        print("Sum =",s)
    elif choice==2:
        num1=int(input("Enter num1= "))
        num2=int(input("Enter num2= "))
        if num1>num2:
            subt=num1-num2
        elif num2>num1:
            subt=num2-num1
        print("Subtraction of num1 and num2=",subt)
    elif choice==3:
        num1=int(input("Enter num1= "))
        num2=int(input("Enter num2= "))
        m=num1*num2
        print("Multiplication of num1 and num2=",m)
    elif choice==4:
        num1=int(input("Enter num1= "))
        num2=int(input("Enter num2= "))
        d=num1//num2
        print("Division of num1 and num2=",d)
    elif choice==5:
        break
    else:
        print("Invalid choice")
    
    
