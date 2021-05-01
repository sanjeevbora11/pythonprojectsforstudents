#To change the value of global variable inside a function

def func3():
    global num #num is a global variable here
    print(num)
    num=10
    print(num)
num=20
print(num)
func3()
print(num)
