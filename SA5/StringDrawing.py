# Author: Tahjae Jackson
# Date: October 11, 2021
# Purpose: To create a string drawing using the two lines and strings as well as the functions from cs1lib.

from cs1lib import *


STICK_WIDTH = 3
STRING_WIDTH = 1


# Purpose: To draw string art
# Parameters: The x and y coordinates of one end of stick A,
# the x and y coordinates of the other end of stick A,
# the x and y coordinates of one end of stick B,
# the x and y coordinates of the other end of stick B,
# the number of strings.

# Return: None


def string_draw(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2, n_of_strings):
    global r, g, b
    background()
    blueviolet()
    set_stroke_color(r, g, b)
    set_stroke_width(STICK_WIDTH)
    draw_line(ax1, ay1, ax2, ay2)
    draw_line(bx1, by1, bx2, by2)
    set_stroke_width(STRING_WIDTH)
    count = 0
    fraction = 0
    range = 1/(n_of_strings-1)
    r = 1
    g = 0
    b = 1

    while count <= n_of_strings:
        set_stroke_color(r, g, b)
        x1 = ax1 + fraction * (ax2 - ax1)
        x2 = bx1 + (1.0 - fraction) * (bx2 - bx1)
        y1 = ay1 + fraction * (ay2 - ay1)
        y2 = by1 + (1.0 - fraction) * (by2 - by1)
        draw_line(x1, y1, x2, y2)
        fraction = fraction + range
        count = count + 1
        b = b - range
        g = g + range






# Purpose: The main function to be called
#Parameters: There are none

def maindraw():
    string_draw(25, 50, 50, 200, 350, 180, 200, 350, 25)


# Purpose: To create a black background
#Parameters: There are none

def background():
    global r, g, b
    black()
    set_clear_color(r, g, b)
    clear()


# Purpose: This set the colour to red
# Parameters: There are none

def red():
    global r, g, b
    r = 1
    g = 0
    b = 0

# Purpose: This set the colour to white
# Parameters: There are none

def white():
    global r, g, b
    r = 1
    g = 1
    b = 1

# Purpose: This set the colour to black
# Parameters: There are none

def black():
    global r, g, b
    r = 0
    g = 0
    b = 0

# Purpose: This set the colour to green
# Parameters: There are none

def green():
    global r, g, b
    r = 0
    g = 1
    b = 0

# Purpose: This set the colour to blue
# Parameters: There are none

def blue():
    global r, g, b
    r = 0
    g = 0
    b = 1

# Purpose: This set the colour to light purple
# Parameters: There are none

def lightpurple():
    global r, g, b
    r = 203 / 255
    g = 195 / 255
    b = 227 / 255

# Purpose: This set the colour to purple
# Parameters: There are none

def purple():
    global r, g, b
    r = 176 / 255
    g = 38 / 255
    b = 255 / 255


# Purpose: This set the colour to magenta
# Parameters: There are none

def magenta():
    global r, g, b
    r = 255 / 255
    g = 0 / 255
    b = 255 / 255

# Purpose: This set the colour to medium purple
# Parameters: There are none

def blueviolet():
    global r, g, b
    r = 138 / 255
    g = 43 / 255
    b = 226 / 255

start_graphics(maindraw)