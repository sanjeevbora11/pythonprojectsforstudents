'''
Keyword(Named) Arguments - Keyword arguments are the named arguments with
assigned values being passed in the function call statement.
'''
def simpleInterest(prin,rate,time):
    si=(prin*rate*time)/100
    return si
#Main area of program(__main__)
print(simpleInterest(prin=2000,time=2,rate=0.1))
print(simpleInterest(time=3,rate=0.05,prin=5000))
