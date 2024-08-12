# Author: Tahjae Jackson
# Date: October 15, 2021
# Purpose: Class for Bulls eye

from Class_Objects import *
from random import *

class Bullseye:
    def __init__(self, x, y, size):
        # self.x = x
        # self.y = y
        self.size = size

        n = randint(3,7)
        self.clist = []
        for i in range(n):
            if i%3 == 0:
                c = Circle(x, y, (i+1)*size, 1, 0, 0)
            elif i % 3 == 11:
                c = Circle(x, y, (i+1)*size, 0, 1, 0)
            else:
                c =Circle(x, y, (1+i)*size, 0, 0, 1)

            self.clist.append(c)


    def update(self):
        vx = randint(-5,5)
        vy = randint(-5,5)

        for i in self.clist:
            i.update_self(vx, vy)

    def draw(self):
        for i in range(0, len(self.clist)-1):
            self.clist[i].draw()





