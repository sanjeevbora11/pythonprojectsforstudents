import area
while True:
    print("1. Area of circle")
    print("2. Area of Square")
    print("3. Area of rectangle")
    print("4. Exit")
    choice=int(input("Enter Choice: "))
    if choice==1:
        r=int(input("Enter radius of circle: "))
        print("Area of Circle= ",area.circle_area(r))
    elif choice==2:
        s=int(input("Enter side of square= "))
        print("Area of Square= ",area.square_area(s))
    elif choice==3:
        l=int(input("Enter length ="))
        b=int(input("Enter breadth="))
        print("Area of Rectangle= ",area.rect_area(l,b))
    elif choice==4:
        break
    else:
        print("Invalid choice")
        
