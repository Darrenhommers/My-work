# Dividing the first number by the second number
# Author: Darren Miller

x= int(input("Enter first number: "))
y= int(input("Enter second number: "))
answer= int(x//y)
remainder= x%y

print ("{} divided by {} is {} with remainder {}".format (x, y, answer, remainder))
