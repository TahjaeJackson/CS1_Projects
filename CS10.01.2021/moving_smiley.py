from cs1lib import *

WIDTH = 400
HEIGHT = 400

bx = WIDTH // 2
by = HEIGHT //2
bsize = 100
mpressed = False
gpressed = False
spressed = False

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

def main_draw():
    global bsize
    #clear the bg
    set_clear_color(1, 1, 1)
    clear()

    #Draw the big fellow
    smiley_draw(bx, by, bsize, 0, 1, 1)

    if gpressed == True and bsize < 300:
        bsize = bsize + 10

    if spressed == True and bsize > 10:
        bsize = bsize - 10


def my_mpress(mx, my):
    global mpressed
    mpressed = True

def my_mrelease(mx, my):
    global mpressed
    mpressed = False

def my_mmove(mx, my):
    global bx, by

    if  mpressed == True:#not mpressed
        bx = mx
        by = my

def my_kpress(value):
    global gpressed, spressed

    if value == "g":
        gpressed = True

    if value == "s":
        spressed = True


def my_krelease(value):
    global gpressed, spressed

    if value == "g":
        gpressed = False

    if value == "s":
        spressed = False



start_graphics(main_draw, width=WIDTH, height=HEIGHT, mouse_press=my_mpress, \
               mouse_release=my_mrelease, mouse_move=my_mmove,\
               key_press=my_kpress, key_release=my_krelease)