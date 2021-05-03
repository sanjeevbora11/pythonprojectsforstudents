def func2(var1):
    var1=var1+20
    print("Inside function value of var1= ",var1)
num=20
print("Value of num= ",num)
func2(num) #var1 and num are referring different memory location
print("Value of num after calling function=",num)
