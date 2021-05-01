num=10 #global variable
def func2():
   print("Inside func2(): ",num)
   
   #num=num+20 #Python interpreter is treating this num as local variable
   #print(num)
  
func2()
print("Outside func2(): ",num)
