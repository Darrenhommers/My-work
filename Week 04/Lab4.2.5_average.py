# This program reads in numbers until the user enters 0
# It will print them back out again and their average
# Author: Darren Miller

numbers= []
# first number then we check if it is 0 in the while loop
number= int(input("Enter number (0 to quit): "))

while number != 0:
    numbers.append(number)

# read the next number and check if 0
number= int(input("enter another (0 to quit): "))

for value in numbers:
    print (value)

# I want the average to be a float
average= float(sum(numbers)) / len(numbers)
print (f"The average is {average}")
