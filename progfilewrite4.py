#Write a program to explain use of writelines() method
#writelines() function is used to write lines in a file i.e. list to a file.
file1=open("file5.txt","w")
weekdays=["Sunday\n","Monday\n","Tuesday\n","Wednesday\n","Thursday\n",
          "Friday\n","Saturday"]
file1.writelines(weekdays)
file1.close()

#gpt4
