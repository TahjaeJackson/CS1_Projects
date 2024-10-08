# Name: Aulanni Kidd
# Date: February 13, 2024
# Purpose: Earth Moon Simulator

from cs1lib import *
from system import System
from body import Body

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400

TIME_SCALE = 3.0e6         # real seconds per simulation second
PIXELS_PER_METER = 7 / 1e10  # distance scale for the simulation

FRAMERATE = 3333.33              # frames per second
TIMESTEP = 1/FRAMERATE  # time between drawing each frame

def main():

    set_clear_color(0, 0, 0)    # black background

    clear()

    # Draw the system in its current state.
    solar.draw(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, PIXELS_PER_METER)

    # Update the system for its next state.
    solar.update(TIMESTEP * TIME_SCALE)



earth = Body(5.9736e24, -149.6e9, 0, 0, 29790, "earth.jpg",1/75)           # blue earth
sun = Body(1.98892e30, 0, 0, 0, 0, "sun.png", 1/50) # yellow sun
mercury = Body(0.33e24,-57.9e9,0,0,47890, "mercury.jpg",1/140) # red mercury
venus = Body(4.87e24,	-108.2e9,0,0,	35040, "venus.jpg",1/45)
mars = Body(0.642e24,	-227.9e9,0,0,	24140, "mars.jpg",1/70)


solar = System([ sun, mercury, venus, earth, mars])

start_graphics(main, 2400, framerate=FRAMERATE)