# NAME: Tahjae Jackson
# DATE: October 20, 2021
# PURPOSE: Simulation of a physical ball bouncing


from cs1lib import  *

W = 400
H = 400
FRAMERATE = 100 #Default framerate is usually 40
TIMESTEP = 1/FRAMERATE #Time that has passed per frame rate
TIMESCALE = 1.25  #Used to speed up the simulation

PIXEL_PER_METRE = 20

RADIUS = 1 #metre
x = 0  #metre
y = 10 #metre

v_x = 3 #m/s
v_y = 0 #m/s
G = -9.8 #m/s^2

def draw_ball():
    pixel_x = x * PIXEL_PER_METRE
    pixel_y = H - y * PIXEL_PER_METRE
    pixel_r = RADIUS * PIXEL_PER_METRE

    set_fill_color(1, 1, 0)
    draw_circle(pixel_x,pixel_y,pixel_r)



def update_ball ():
    global x, y, v_x, v_y

    x = x + v_x * TIMESTEP * TIMESCALE
    y = y + v_y * TIMESTEP * TIMESCALE


    if y <= 0:
        v_y = - v_y
    else:
        v_y = v_y + G * TIMESTEP * TIMESCALE




def main_draw():
    set_clear_color(1, 1, 1)
    clear()

    draw_ball()
    update_ball()

start_graphics(main_draw, width = W, height = H, framerate = FRAMERATE)



