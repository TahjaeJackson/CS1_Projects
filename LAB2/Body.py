# Name: Tahjae Jackson
# Date: October 27, 2021
# Purpose: Class used to design a body for the solar system

from cs1lib import *
from System import *



class Body:

    # accepts all the necessary values to create the body and puts them into the created object
    def __init__(self,mass, x, y, v_x, v_y, rad, r, g, b):
        self.mass = mass
        self.x = x
        self.y = y
        self.vx = v_x
        self.vy = v_y
        self.rad = rad
        self.r = r
        self.g = g
        self.b = b


    def update_position(self, timestep):
        self.x = self.x + self.vx * timestep
        self.y = self.y + self.vy * timestep

    def update_velocity(self,a_x,a_y, timestep):
            self.vx = self.vx + a_x * timestep
            self.vy = self.vy + a_y * timestep

    def draw(self, cx, cy, pixels_per_metre):
        set_fill_color(self.r, self.g, self.b)
        draw_circle(cx, cy, self.rad)
