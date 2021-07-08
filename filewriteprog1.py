'''
with statement- with statement is used for file handling and with statement does
not require close() function
'''
with open("file6.txt","w") as file1: #file1=open("file6.txt","w")
    file1.write("Sunday\n")
    file1.write("Monday\n")
    file1.write("Tuesday\n")
    file1.write("Wednesday\n")
    file1.write("Thursday\n")
    file1.write("Friday\n")
    file1.write("Saturday\n")
    #Here close() function executes automatically
print("Data is written into a file")
