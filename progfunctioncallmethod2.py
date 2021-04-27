#Trace (or Explain) the flow of execution of following program statements
def power(b,p):                   #1
    y=b**p                        #2
    return y                      #3
def calcSquare(x):                #4
    a=power(x,2)                  #5 
    return a                      #6
n=5                               #7
result=calcSquare(n) + power(3,3) #8
print(result)                     #9
#execution of program statements
#1->4->5->7->8->4->5->1->2->3->5->6->8->1->2->3->8->9
