# Create a program that puts 10 random numbers into a queue
# The program shoult output the values in the queue and
# take the numbers one at a time, print it and the current
# numbers still in the queue.
# Author: Darren Miller

import random
queue = []
numberOfNumbers=10
rangeTo=100
for n in range(0,numberOfNumbers):
    queue.append(random.randint(0,rangeTo))
print (f"queue is {queue}")
while len(queue) != 0:
    currentNumber = queue.pop(0)
    print (f"current Number is {currentNumber} and the queue is {queue} ")
print ("the queue is now empty")


