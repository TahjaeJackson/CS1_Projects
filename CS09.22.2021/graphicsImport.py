# Author: Tahjae Jackson
# Date: 09/22/2021
# Purpose: Demo of importing Graphics from cs1lib

from cs1lib import *

WIDTH = 400
HEIGHT = 400
sx = WIDTH//2
sy = HEIGHT//2
SSIZE = 50

bx = WIDTH//2
by = HEIGHT//2
BSIZE = 100

def draw_eye (x,y,size):


    # OUTER CIRCLE
    enable_stroke()
    set_stroke_color(0,0,0)
    set_stroke_width(1)
    set_fill_color(1,1,1)
    draw_circle(x,y,size)

    #INNER CIRCLE
    set_fill_color(0,0,0)
    draw_circle(x,y-0.5*size, 0.5*size)




#Purpose: To draw an emoji that rolls its eyes
#Parameters: None

def smiley_draw (x,y,z,r,g,b):  #anything that I would like to drawn should be called within this function

    #SET THE BACKGROUND COLOUR
    set_clear_color(1,0,0) # this is used to change the background colour of the window that will be presented. To change the colour, we adjust the numbers in the brackets (red, green, blue)
    clear()

    #DRAW THE FACE
    set_fill_color(1,1,0)
    disable_stroke() #removes the border around the circle
    draw_circle(X,Y,SIZE)

    #DRAW EYES
    draw_eye(X-0.3* SIZE, Y-0.3*SIZE, 0.2*SIZE)
    draw_eye(X + 0.3 * SIZE, Y - 0.3 * SIZE, 0.2 * SIZE)

    #DRAW MOUTH
    set_stroke_color(1,0,0)
    set_stroke_width(2)
    draw_line(X-0.3*SIZE, Y+0.3*SIZE, X+0.3*SIZE,Y+0.3*SIZE)


def my_draw():
    #Set background
    set_clear_color(1,1,1)
    clear()

    #Draw the little fellow
    smiley_draw(sx,sy,SSIZE,1,1,0

    #Draw the big fellow
    smiley_draw(bx,by,BSIZE,0,1,1)


def my_mmove(mx,my):
    global sx, sy, bx, by
    sx = bx
    sy = by
    bx = mx
    by = my
    print("In mouse press:", mx, my)

def my_mrelease(mx,my):
    print("In mouse release", mx,my)

def my_move(mx,my):
    print("In mouse move", mx, my)

start_graphics(my_draw, width=WIDTH, height=HEIGHT, mouse_press=mypress, mouse_release=my_mrelease, mouse_move=my_move)