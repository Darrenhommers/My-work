# This program prints out a random fruit.
# Author: Darren Miller

import  random
fruits= ('Apple', 'Orange', 'Banana', 'Pear')
index= random.randint (0,len(fruits)-1)

fruit= fruits[index]

print ("A random fruit: {}".format(fruit))
