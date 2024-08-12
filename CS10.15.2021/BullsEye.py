# Author: Tahjae Jackson
# Date: October 15, 2021
# Purpose: Class for Bulls eye

from Class_Objects import *
from random import *

class Bullseye:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size

        self.c1 = Circle(x, y, size, 1, 0, 0)
        self.c2 = Circle(x, y, 2*size, 0, 1, 0)
        self.c3 = Circle(x, y, 3*size, 0, 0, 1)

    def update(self):
        vx = randint(-5,5)
        vy = randint(-5,5)

        self.c1.update_self(vx,vy)
        self.c2.update_self(vx, vy)
        self.c3.update_self(vx, vy)

    def draw(self):
        self.c3.draw()
        self.c2.draw()
        self.c1.draw()




