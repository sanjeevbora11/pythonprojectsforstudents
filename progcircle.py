'''
Write a program calculate area of circle and circumference using
functions(You have to define functions for both).
Area of circle=pi*r*r
pi=3.14
Circumference of circle=2*pi*r
'''
def AreaOfCircle(radius):
    area=3.14*radius*radius
    return area
def CircumofCircle(radius):
    c=2*3.14*radius
    return c
print(AreaOfCircle(5))
print(CircumofCircle(5))
r=int(input("Enter radius of Circle= "))
print(AreaOfCircle(r))
