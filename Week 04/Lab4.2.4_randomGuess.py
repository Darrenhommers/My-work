# Generate a number at random between 0 and 100.
# Create a program to guess the number
# Program tells the user if the guess is too high or too low.
# Author: Darren Miller

import random
number= random.randint(0,100)

# print ("The random number is: {}" .format (number))

number_to_guess= number
guess= int(input("Please guess the number: "))
while guess != number_to_guess:
    if guess < number_to_guess:
        print ("too low")
    else:
        print ("too high")
    guess= int(input("Please guess again: "))

print ("Well done! Yes the number was", number_to_guess)