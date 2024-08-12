from cs1lib import *

radius = 1

def animate_circle():
    global radius

    clear()
    draw_circle(200, 200, radius)

    # change the state for the next frame
    radius = radius + 1

start_graphics(animate_circle, 100)