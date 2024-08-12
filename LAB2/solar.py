# Name: Tahjae Jackson
# Date: October 27, 2021
# Purpose: To create a driver function for the solar system

from cs1lib import *
from System import *
from Body import *

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400

TIME_SCALE = 3.0e6       # real seconds per simulation second
PIXELS_PER_METER = 7 / 1e10  # distance scale for the simulation

FRAMERATE = 30              # frames per second
TIMESTEP = 1.0 / FRAMERATE  # time between drawing each frame


# Purpose: to create a main function to be create the solar system an dto be called in star graphics
# Parameters: there are none
# Return: Nothing
def main():

    set_clear_color(0, 0, 0)    # black background

    clear()

    # Draw the system in its current state.
    earth_moon.draw(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, PIXELS_PER_METER)

    # Update the system for its next state.
    earth_moon.update(TIMESTEP * TIME_SCALE)

# DECLARATIONS OF THE DIFFERENT PLANETS IN THE SOLAR SYSTEM

sun = Body(1.98892e30, 0, 0, 0, 0, 25, 249/255, 215/255, 28/255)
mercury = Body(0.330e24, -57.9e9, 0, 0, 47890, 4, 151/255, 151/255, 159/255)
venus = Body(4.87e24, -108.2e9, 0, 0, 35040, 10, 204/255, 153/255, 102/255)
earth = Body(5.9736e24, -149.6e9, 0, 0, 29790, 10.63, 55/255, 86/255, 115/255)
mars = Body(0.642e24, -227.9e9, 0, 0, 24140, 5.66, 173/255, 98/255, 66/255)

earth_moon = System([sun, mercury, venus, earth, mars])

start_graphics(main, 2400, framerate=FRAMERATE)