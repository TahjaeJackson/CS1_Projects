# Author: Tahjae Jackson
# Date: September 27, 2021
# Purpose: Draw a Bull's-eye w/ blue our circle, green middle circle and red inner circle. Use a separate function for each circle
from cs1lib import *
CENTRE_X = 400
CENTRE_Y = 400
RADIUS = 100

def outer_circle ():
    set_fill_color(0,0,1)
    draw_circle(CENTRE_X,CENTRE_Y,RADIUS)

def middle_circle ():
    set_fill_color(0,1,0)
    draw_circle(CENTRE_X,CENTRE_Y,RADIUS-20)

def inner_circle ():
    set_fill_color(1,0,0)
    draw_circle(CENTRE_X,CENTRE_Y,RADIUS-40)

def bullseye():
    set
    clear()
    outer_circle()
    middle_circle()
    inner_circle()

start_graphics(bullseye,width=800,height=800)

