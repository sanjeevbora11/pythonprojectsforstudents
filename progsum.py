'''
WAp to print the sum of series 1+2+...20.
'''
#using for loop
sum=0
for i in range(1,21):
    sum=sum+i
print("Sum of series using for loop= ",sum)
#using while loop
sum1=0
j=1#start of loop counter variable
while j<21: #condition of loop
    sum1=sum1+j
    j=j+1   #step or increment value of loop
print("Sum of series using while loop = ",sum1)

