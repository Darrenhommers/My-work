# Program tells the user if their guess is 
# too high or too low
# Author: Darren Miller

number_to_guess= 45
guess= int(input("Please guess the number: "))
while guess != number_to_guess:
    if guess < number_to_guess:
        print ("too low")
    else:
        print ("too high")
    guess= int(input("Please guess again: "))

print ("Well done! Yes the number was", number_to_guess)