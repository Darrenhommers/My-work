# This program reads in a students
# percentage and prints out the 
# corresponding grade
# Author: Darren Miller

percentage= float(input("Enter the percentage: "))
# print (percentage)

if percentage <0 or percentage >100:
    print("Please enter a number between 0 and 100")
elif percentage < 40:
    print ("Fail")
elif percentage < 50:
    print   ("Pass")
elif percentage <60: 
    print ("Merit 1")
elif percentage <70:
    print  ("Merit 2")
else: # the only option left is between 70 and 100
    print ("Distinction")

    