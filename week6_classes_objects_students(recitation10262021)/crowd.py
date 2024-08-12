# Name:
# Date:
# Purpose:
#
# 1. Define a class (crow.py) that works with the crowd_driver.py file.
#
# 2. The output of crowd_driver.py should be: n face objects, drawn at random positions on the screen, whose eyes follow the user's screen
# (you don't have to code for the eye movement, it's in .lookat())

from random import *
from face import Face

class Crowd:

    def __init__(self,n):
        self.crowd_list = []
        for i in range(0, n):
            x = randint(0, 300)
            y = randint(0, 300)
            size = randint(50, 100)
            z = Face(x, y, size)
            self.crowd_list.append(z)


    def draw(self):
        for i in range(0,len(self.crowd_list)):
            self.crowd_list[i].draw()


    def lookat(self, mx, my):
        for i in range(0, len(self.crowd_list)):
            self.crowd_list[i].lookat(mx,my)



