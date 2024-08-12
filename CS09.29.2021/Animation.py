# Author: Tahjae Jackson
# Date: September 29, 2021
# Purpose: To use cs1lib to create an animation


from cs1lib import *

def smiley_draw(x,y,size,r,g,b):
    set_fill_color(r,g,b)
    disable_stroke()
    draw_circle(x,y,size)

    draw_eye
