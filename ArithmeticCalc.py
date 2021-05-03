#ARITHMETIC CALCULATOR
print("Here some choices of arithmetic operations for you")
while True:
    
    print("1- ADDITION")
    print("2- SUBTRACTION")
    print("3- MULTIPLY")
    print("4- DIVIDE")
    print("5- EXIT")
    choice=int(input("Enter choice_"))
               
    if choice ==1:
        a=int(input("Enter 1st Number_"))
        b=int(input("Enter 2nd Number_"))
        S=a+b
        print("SUM=",S)
    elif choice == 2:
        a=int(input("Enter 1st Number_"))
        b=int(input("Enter 2nd Number_"))
        if a>b:
              SUBT=a-b
        elif b>a:
            SUBT=b-a
        print("SUBTRACTION=",SUBT)
    elif choice == 3:
        a=int(input("Enter 1st Number_"))
        b=int(input("Enter 2nd Number_"))
        P=a*b
        print("PRODUCT=",P)
    elif choice == 4:
        a=int(input("Enter 1st Number_"))
        b=int(input("Enter 2nd Number_"))
        D=a//b
        print("DIVISION=",D)
              
    elif choice==5:
        print("THANKS FOR USING.")
        break
    else:
        print("Invalid choice")
        
