'''
Write a program to find the grade of a student when grades are allocated as given in
the table below:
Percentage of Marks                      Grade
Above 90%                                A
80% to 90%                               B
70% to 80%                               C
60% to 70%                               D
Below 60%                                E
'''
per=float(input("Enter Percentage: "))
if per>90:
    print("Grade A")
elif per>=80 and per<90:
    print("Grade B")
elif per>=70 and per<80:
    print("Grade C")
elif per>=60 and per<70:
    print("Grade D")
elif per<60:
    print("Grade E")
else:
    print("Invalid input")
