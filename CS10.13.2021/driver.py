#Author: Vasanta
#Date: 10/13/2021
#Purpose: Demo driver file

from Lec14_1.ball import Ball
from cs1lib import *

b1 = Ball(200, 300)
b2 = Ball(100, 200)

def maindraw():
    b1.draw(1, 0, 0)
    b2.draw(0, 1, 0)

start_graphics(maindraw)
