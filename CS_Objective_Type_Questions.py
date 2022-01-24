#convert the following while loop into for loop:
x=5
while (x<10):
    print(x+10)
    x+=2 #x=x+2

#For loop format of above while loop
for x in range(5,10,2):
    print(x+10)
#Convert the following for loop into while loop
for k in range(10,20,5):
    print(k)
#while loop format
k=10
while k<20:
    print(k)
    k=k+5
'''
Find error(s) in the following code(if any) and correct it by rewriting
the code and underline the corrections:

'''
#a
x=int(input("Enter value for x:"))
for y in range(0,11):
    if x==y:
        print (x+y)
    else:
        print (x-y)
#b
MaxSpeed=50
Alter='N'
MySpeed=int(input())
if MySpeed>MaxSpeed:
    Alter='Y':
print(Alter)
#c
A=int(input("Enter a value: "))
count=0
while A != 0:
    count=count+1#uninitialized value of count
    if count<A:
        print(count)
    else:
        print(count+A)
    A=A+1
#Find the ouput of following code:
#(a)
x=3
if x>2 or x<5 and x==6:
    print("ok")
else:
    print("no output")
#Ouput
#3>2 or 3<5 and 3==6
#True or True and False
#True or False
#True
#output ok
#priority of and operator is more than or operator. logical operators are binary
#(b)
x,y=2,4
if (x+y==10):
    print("True")
else:
    print("False")
#output will be False
#(c)
x=10
y=0
while x>y:
    x=x-4
    y+=4
    print(x,end=" ")
'''
Dry Run
x      y   condition   print
10     0     10>0
6   4                  6
            6>4
2   8                  2
            2>8
6 2

'''
#(d)
i=0
while i<10:
    i=i+1
    if i==5:
        break
    print(i,end=" ")
'''
Dry Run
i      print
0
1      1
2      2
3      3
4      4
5
1 2 3 4
'''
#(e)
for x in range(2):
    for y in range(2):
        print(x,y,x+y)
'''
x    y       print
0    0       0 0 0
     1       0 1 1
1    0       1 0 1
     1       1 1 2

final output
0 0 0
0 1 1
1 0 1
1 1 2
'''
#(f)
x=2
y=3
for i in range(y*2-x):
    print(i,end=' ')
'''
Dry Run
x=2
y=3
y*2-x=3*2-2=6-2=4
for i in range(4):
   print(i,end=' ')
0 1 2 3
'''
#(g)
for z in range(-100,200,100):
    print("*",z,end="")
'''
* -100 * 0 * 100
'''























