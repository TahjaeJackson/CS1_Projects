from cs1lib import *

WIDTH = 400
HEIGHT = 400
sx = WIDTH // 2
sy = HEIGHT // 2
SSIZE = 50

bx = WIDTH // 2
by = HEIGHT // 2
BSIZE = 100


#Purpose: Draw a rolling eye
#Parameters:x, y are positive integers for location of the eye and
#size is a positive integer for radius of the eye
def draw_eye(x, y, size):
    #draw the outer circle
    set_fill_color(1, 1, 1)
    enable_stroke()
    set_stroke_color(0, 0, 0)
    set_stroke_width(1)
    draw_circle(x, y, size)

    #draw outer circle
    set_fill_color(0, 0, 0)
    draw_circle(x, y - 0.5*size, 0.5*size)

#Purpose:Draw a rooling eyes smiley
#Parameters:x and y are positive integers that indicate the location of smiley
#r, g, b are floating point numbers between 0 and 1 and define the
#color of the smiley.

def smiley_draw(x, y, size, r, g, b):
    #Face
    set_fill_color(r, g, b)
    disable_stroke()
    draw_circle(x, y, size)

    #draw eyes
    draw_eye(x - 0.3*size, y - 0.3*size, 0.2*size)
    draw_eye(x + 0.3*size, y - 0.3*size, 0.2*size)

    #draw mouth
    set_stroke_color(1, 0 , 0)
    set_stroke_width(2)
    draw_line(x - 0.3*size, y + 0.3*size, x + 0.3*size, y + 0.3*size)


def mydraw():
    #set the background
    set_clear_color(1, 1, 1)
    clear()

    #Draw the little fellow
    smiley_draw(sx, sy, SSIZE, 1, 1, 0)

    #Draw the big fellow
    smiley_draw(bx, by, BSIZE, 0, 1, 1)

def my_mpress(mx, my):
    global sx, sy, bx, by

    sx = bx
    sy = by
    bx = mx
    by = my


def my_mrelease(mx, my):
    print("In mouse release", mx, my)

def my_mmove(mx, my):
    print("In mouse move", mx, my)

start_graphics(mydraw, width=WIDTH, height=HEIGHT, mouse_press=my_mpress, \
               mouse_release=my_mrelease, mouse_move=my_mmove)