# Author: Tahjae Jackson
# Date: October 13, 2021
# Purpose: question 4


from Class_Objects import Ball
from cs1lib import *

# When you create a class, python automatically creates a constructor function

b1 = Ball(200, 300) #b1 is an object which is an address
b2 = Ball(100, 200)

#self tells you which physical object to update.
# when you have self . smth, what is on the left is the address of something
b1.update_self()
b2.update_self()
s = str(b1) + " " + str(b2)
print(s)

def maindraw():
    b1.draw(1, 0, 0)
    b2.draw(0, 1, 0)

start_graphics(maindraw)