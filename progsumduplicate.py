'''
WAP to calculate sum of non repeatitive elements of a list.
Repeatitive elements will count only once
'''
L1=[4,5,6,7,8,9,10,21,4,5,6,1,2,4,7,8,21,12,13,14,4,5,6,7,8,100,11,199]
sum1=0
n=0
'''
s1=set(L1)#set() function converts list into set and set stores only unique
            #values
s1=list(s1)
print(s1)
print(sum(s1))
'''
#in and not in operators are iterable. These can be used for list, string, tuple
count=0
elements=[] 
for num in L1: #This loop accesses all elements of list. 
    if num not in elements:
        elements.append(num)
        sum1=sum1+num
print(elements)
print(sum1)
        
    

