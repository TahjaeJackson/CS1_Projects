# Author: Tahjae Jackson
# Date: October 14, 2021
# Purpose: question 4


from cs1lib import *


class Circle: #This is how we define a class. We always use an upper case first letter
    def __init__(self, gx, gy, radius,r, g, b): #this is the definition of a method which is very similar to a function
        self.x = gx
        self.y = gy
        self.radius = radius
        self.r = r
        self.g = g
        self.b = b

    def update_self(self, vx, vy):
        self.x = self.x + vx
        self.y = self.y + vy

    def draw(self):
        set_fill_color(self.r, self.g, self.b)
        draw_circle(self.x, self.y, self.radius)

    def __str__(self):
        return str(self.x) + " " + str(self.y)
        # this is the str method. You never call them explicitly and they have a fixed format. This
        # specific double underscore cannot take any other parameter besides self and it must return a string
        # Whenever this class is called, instead of printing the address, it will print the string because of the __str__