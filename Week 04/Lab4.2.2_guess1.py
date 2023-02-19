# Prompts user to guess a number
# Program keeps prompting until the user gets it right
# Author: Darren Miller

number_to_guess= 45
guess= int(input("Please guess the number: "))
while guess != number_to_guess:
    print ("Wrong")
    guess= int(input("Please guess again: "))

print ("Well done! Yes the number was", number_to_guess)
