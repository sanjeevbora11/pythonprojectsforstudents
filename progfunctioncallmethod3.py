#Explain the flow of execution of statements of following program
def increment(x):   #1
    x=x+1           #2
x=3                 #3
print(x)            #4
increment(x)        #5
print(x)            #6
#Flow of Execution 1->3->4->5->1->2->5->6
