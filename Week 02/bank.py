# bank.py
# Prompt user to enter 2 amounts in cent
# Add the 2 amounts
# Print the answer with a euro sign and decimal point
# Author: Darren Miller
# Week 02 task

amount1= float (input("Enter amount 1 (in cent):  "))
amount2= float (input("Enter amount 2 (in cent):  "))
Total= (float(amount1 + amount2)/100)

print(f"The sum of these two values is: €{Total: .2f}")



