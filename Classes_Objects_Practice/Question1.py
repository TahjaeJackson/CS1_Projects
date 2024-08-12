# Name: Tahjae Jackson
# Date: October 17, 2021
# Purpose: Using classes and objects to create a functioning timer. This class is specifically for counting down


# Define a Bubble class that has instance variables to store the x and y coordinates of
# the center of a bubble, size of the bubble and a boolean value popped to indicate if
# the bubble has popped. Your Bubble class must support the following methods:
# 1. (4 points) __init__(self, x, y): This method must initialize the instance
# variables x, y, size and popped. The size of the bubble can be initialized to
# any random value between 5 and 15 using the randint function. The popped
# variable must be initialized to False.
# 2. (4 points) draw(self): This method should draw a circle with instance
# variables x and y as center and size as the radius. The draw method should
# only draw the bubble if it has not been popped. In the example video I have used
# red = 0.6, green = 0.8 and blue = 1 to define the color of all the bubbles. You can
# use any color that you prefer.
# 3. (5 points) update(self): This method should do the following:
# a. update the x and y positions of the bubble using random velocity for x and
# y directions that are created locally in the method using randint function.
# Make sure the random values generated for velocity in y direction only
# makes the bubble to move up. The bubble can move horizontally in any
# direction.
# b. A bubble must be marked as popped if its center is out of the boundaries
# of the graphics window.

from random import *
from cs1lib import *



class Bubble:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = randint(10, 20)
        self.popped = False

    def draw(self):
        red = 0.6
        green = 0.8
        blue = 1
        if self.popped == False:
            set_fill_color(red, green, blue)
            draw_circle(self.x, self.y, self.size)


    def update(self):
        vx = randint(-2, 2)
        vy = randint(-3, -1)
        self.x = self.x + vx
        self.y = self.y + vy
        self.draw()


    def is_popped(self,width, height):
        if self.x <= 0 or self.x >= width:
            self.popped = True
        elif self.y <= 0 or self.y >= height:
            self.popped = True

        return self.popped



