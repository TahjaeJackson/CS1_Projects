# Author: Tahjae Jackson
# Date: October 4, 2021
# Purpose: Short Assignment 4

from cs1lib import *

bg = 0
#Purpose: To create the black background
#Parameters: There are none

def background():
    global bg
    if bg == 0:
        set_clear_color(0,0,0)
        clear()
        bg = 1

#Purpose: To get the location of the mouse when it is pressed on the window
#Parameters: Two values that will store the pixel location of the mouse

def m_press(mx,my):
    global mouse_select, old_x, old_y
    mouse_select = True
    old_x = mx
    old_y = my


#Purpose: To determine if the mouse is released so it can stop drawing and get the location of the mouse
#Parameters: There are two variables that will store the location of the mouse

def m_release(mx,my):
    global mouse_select
    mouse_select = False

#Purpose: To update the current position of the mouse as it moves
#Parameters: two values to store the coordinates of the mouse location

def m_move(mx, my):
    global new_x, new_y
    new_x = mx
    new_y = my

#Purpose: To update the stroke colour when a certain key is pressed
#Parameters: The character that inputed from the keyboard

def my_kpress(colour):
    global r, g, b, y, w

    if colour == "r":
        r = 1
        g = 0
        b = 0

    if colour == "g":
        r = 0
        g = 1
        b = 0

    if colour == "b":
        r = 0
        g = 0
        b = 1

    if colour == "y":
        r = 1
        g = 1
        b = 0

    if colour == "w":
        r = 1
        g = 1
        b = 1


#Purpose: Calls all the function necessary for the final product
#Parameters: There are none

def main_draw():
    global old_x, old_y, new_x, new_y
    background()
    if mouse_select:
        # enable_stroke()
        set_stroke_width(2)
        set_stroke_color(r, g, b)
        draw_line(old_x, old_y, new_x, new_y)
        old_x = new_x
        old_y = new_y

old_x = 0
old_y = 0
new_x = 0
new_y = 0
mouse_select = False
r = 1
g = 1
b = 1

start_graphics(main_draw, mouse_release=m_release, mouse_press=m_press,mouse_move=m_move, key_press=my_kpress)