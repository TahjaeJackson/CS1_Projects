# Name: Tahjae Jackson
# Date: October 17, 2021
# Purpose: Using classes and objects to create a functioning timer. This class is specifically for counting down

from Question1 import *
from random import *
from cs1lib import *

W = 400
H = 400

def background():

    set_clear_color(1, 1, 1)
    clear()


def maindraw():

    background()
    x = randint(100,350)
    y = randint(100, 350)
    bubble = Bubble(x, y)
    bubble.draw()
    bubble.update()
    bubble.is_popped(W,H)


# for i in range(0,len(list)-1):
#     li

start_graphics(maindraw, width= W, height=H)