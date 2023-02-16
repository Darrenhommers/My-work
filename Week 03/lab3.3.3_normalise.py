# This program reads in a string and strips
# any leading or trailing spaces.
# It also converts all the letters to lower case.
# It then outputs the lengths of the original string
# and the normalised one.

# Author: Darren Miller

rawString= input("Please enter a string: ")
normalisedString= rawString.strip().lower()

lengthofRawString= len(rawString)
lengthofNormalised= len(normalisedString)

print(f"That String normalised is: {normalisedString}")
print(f"we reduced the input string from {lengthofRawString} to {lengthofNormalised} characters")

