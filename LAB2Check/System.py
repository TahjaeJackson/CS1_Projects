# Name: Tahjae Jackson
# Date: October 22, 2021
# Purpose: Class used to design the system of bodies for the solar system


from Body import *
from math import * 


# class System:
#     def __init__(self, body_list):
#         self.body_list = body_list
#
#
#     def update(self, timestep):
#         for i in range(len(self.body_list)):
#
#             ax = 0
#             ay = 0
#
#             if i != 0 :
#                 ax = -0.0028
#                 ay = -0.0028
#
#             self.body_list[i].update_position(timestep)
#
#             self.body_list[i].update_velocity(ax, ay, timestep)
#
#     def draw(self, cx, cy, pixels_per_metre):
#         for i in range(len(self.body_list)):
#             self.body_list[i].draw(cx - self.body_list[i].x * pixels_per_metre, cy - self.body_list[i].y * pixels_per_metre, pixels_per_metre)
G = 6.67384e-11



class System:
    def __init__(self, body_list):
        self.body_list = body_list


    # Updates position and velocities of the moving bodies
    def update(self, timestep):
        for i in range(len(self.body_list)):
            self.body_list[i].update_position(timestep)

        for i in range(len(self.body_list)):
            (ax, ay) = self.compute_acceleration(i)
            self.body_list[i].update_velocity(ax, ay, timestep)

    # draws all the bodies in the system
    def draw(self, cx, cy, pixels_per_metre):
        for i in range(0, len(self.body_list)):
            self.body_list[i].draw(cx - self.body_list[i].x * pixels_per_metre, cy - self.body_list[i].y * pixels_per_metre, pixels_per_metre)



    # calculates the acceleration that each body in the system experiences
    # Return: a tuple of the vertical and horizontal components of the acceleration
    def compute_acceleration(self,n):

        ax = 0
        ay = 0

        for i in range(0, len(self.body_list)):
            if i != n:
                dx = self.body_list[i].x - self.body_list[n].x
                dy = self.body_list[i].y - self.body_list[n].y
                r = sqrt((dx ** 2) + (dy ** 2))
                a = G * self.body_list[i].mass / (r ** 2)
                ax = ax + a * dx/r
                ay = ay + a * dy/r

        return (ax, ay)