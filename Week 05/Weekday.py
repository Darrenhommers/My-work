# A program that outputs whether or not today is a weekday.
# Author: Darren Miller

import datetime # this function outputs what the current date/day are based on numbers 0-6.

DayNo= datetime.datetime.today().weekday()
if DayNo < 5:
    print ("Yes, unfortunately today is a weekday.")

# Days no from 0-4 are weekdays; Days no 5 and 6 are weekend days
else:    
    print ("Its the weekend, yay")