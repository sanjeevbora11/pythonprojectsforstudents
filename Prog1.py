'''
1.	Gurukulam Academy is transforming its result processing unit
into computerized “Student Management System”. Help the institution to develop
an integrated solution using concepts of Python list for adding new students
to the existing list of students on the basis of marks obtained by them.
(we assume the marks of ten students in the class.)
The entire processing system should support adding of updated marks, deleting
the marks of students who have left the institution, followed by generating a
report by arranging the marks of all the students in both ascending and descending
order. 
It should also include insertion and deletion of students’ marks at desirable
position. Develop a Python program for the above scenario-based implementation. 

'''
marksList=[63,64,78,92,90,99]
choice=0
while True:
    print("1: Add marks of new student")
    print("2: Delete Marks")
    print("3: Display Marks")
    print("4: MarksList in Ascending order")
    print("5: Marks List in Descending order")
    print("6: Modify marks")
    print("7: Exit")
    choice=int(input("Enter Choice: "))
    if choice==1:
        stumarks=int(input("Enter Marks of student: "))
        marksList.append(stumarks)
        print("The marks have been successfully added to the marksList")
    elif choice==2:
        m=int(input("Enter the marks of student to be delete: "))
        if m in marksList:
            marksList.remove(m)
    elif choice==3:
        print("MarksList")
        print(marksList)
    elif choice==4:
        print("Marks in Ascending order")
        marksList.sort()
        print(marksList)
    elif choice==5:
        print("Marks in Descending order")
        marksList.sort(reverse=True)
        print(marksList)
    elif choice==6:
        m1=int(input("Enter index of marks "))
        print(marksList[m1])
        newMarks=int(input("Enter new marks: "))
        marksList[m1]=newMarks
            
    elif choice==7:
        break
    else:
        print("Invalid Choice")
        
