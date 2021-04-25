#Nested loop using for loop
'''
To print the following pattern
1
12
123
1234
12345
'''
#using for loop
for i in range(1,6):  #Outer loop will execute 5 times
    for j in range(1,i+1):#inner loop will execute 15 times
        print(j,end='')
    print()
#using while loop
i=1
while i<6:
    j=1
    while j<i+1:
        print(j,end="")
        j=j+1
    i=i+1
    print()
