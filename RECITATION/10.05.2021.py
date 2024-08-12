# Author: Tahjae Jackson
# Date: October 5, 2021
# Purpose:

# Purpose: Use tools  in CS1LIB to draw a red circle of radius = 20, on the centre of graphics window.
#            1.If "L" is pressed, moves ball left
#            2. If "r" is pressed, moves right
#            3. If both are pressed, nothing moves
# Parameters:


from cs1lib import *


RAD = 20
WIDTH = 400
HEIGHT = 400
centre_x = 200
centre_y = 200
MOVE = 20


#Purpose: To check if a certain key is pressed
#Parameters: A character value called key that stores the value that is pressed

def m_press (key):
    global left, right

    if key == "l":
        left = True

    if key == "r":
        right = True

#Purpose: To check if a certain key is released
#Parameters: A character value called key that stores the value that is released

def my_krelease(key):
    global left, right

    if key == "l":
        left = False

    if key == "r":
        right = False

#Purpose: To set the background colour of the window
#Parameters: There are no none

def background():
    set_clear_color(1,1,1)
    clear()


#Purpose: To draw a circle
#Parameters: There are none

def circle():
    global centre_x, centre_y, left, right
    set_stroke_color(1, 0 ,0)
    enable_stroke()
    set_fill_color(1,0,0)
    if left:
        centre_x = centre_x - MOVE
    if right:
        centre_x = centre_x + MOVE
    draw_circle(centre_x,centre_y, RAD)


#Purpose: The main function to be called in the star graphics
#Parameters: There are none
def main_draw():
     background()
     circle()

left = False
right = False

start_graphics(main_draw, width = WIDTH, height = HEIGHT,key_press= m_press, key_release=my_krelease)


