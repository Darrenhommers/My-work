# Prompts the user to enter any positive integer.
# The program outputs the successive values of a calculation
# At each step take the current value and if it is even, divide by 2.
# If it is odd, multiply by 3 and add 1.
# Have the program end if the current value is one.

# Author: Darren Miller

def collatzSequence(number):

    if (number % 2) == 0: # if the number is even
        number= number//2
    else: 
        number= ((number*3)+1) # if it's odd

    print (number)
    return (number)

n = int(input('Please enter a positive integer: '))
while (n != 1):
    n = collatzSequence(n)




