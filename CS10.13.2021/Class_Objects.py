# Author: Tahjae Jackson
# Date: October 14, 2021
# Purpose: question 4

from random import *
from cs1lib import *
R = 20

class Ball: #This is how we define a class. We always use an upper case first letter
    def __init__(self, gx, gy): #this is the definition of a method which is very similar to a function
        self.x = gx
        self.y = gy
        self.vx = randint(-2, 3)
        self.vy = randint(-3, 2)

    def update_self(self):
        self.x = self.x + self.vx
        self.y = self.y + self.vy

    def draw(self, r, g, b):
        set_fill_color(r, g, b)
        draw_circle(self.x, self.y, R)

    def __str__(self):
        return str(self.x) + " " + str(self.y)
        # this is the str method. You never call them explicitly and they have a fixed format. This
        # specific double underscore cannot take any other parameter besides self and it must return a string
        # Whenever this class is called, instead of printing the address, it will print the string because of the __str__