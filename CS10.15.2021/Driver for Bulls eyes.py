# Author: Tahjae Jackson
# Date: October 15, 2021
# Purpose: driver for Bulls eye

from BullsEye import *
from cs1lib import *
from random import *

H = 1000
W = 1000
N = 100

blist=[]

for i in range (N):
    x = randint(0, 1000)
    y = randint(0,1000)
    size = randint(10, 30)
    b = Bullseye(x, y, size)
    blist.append(b)

def main_draw():
    set_clear_color(1,1,1)
    clear()

    for b in blist:
        b.update()
        b.draw()


start_graphics(main_draw,width= W, height= H)


