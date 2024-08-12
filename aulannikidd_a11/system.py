# Name: Aulanni Kidd
# Date: February 13, 2024
# Purpose: System Class

from body import Body
from math import sqrt

class System:
    # initialization method
    def __init__(self, body_list):
        self.body_list = body_list


    # method that calls updates position and velocity of all Body objects in the system
    def update(self, timestep):
        for planet in self.body_list:
            planet.update_position(timestep)

        for planet in self.body_list:
            (ax, ay) = self.compute_acceleration(planet)
            planet.update_velocity(ax, ay, timestep)


    def compute_acceleration(self,planet):
        G = 6.67384e-11
        ax_total = 0
        ay_total = 0
        for planet2 in self.body_list:
            if planet2 != planet:
                # distance between the two planets
                dx = planet2.x - planet.x
                dy = planet2.y - planet.y

                # total distance between the two bodies
                r = sqrt(dx * dx + dy * dy)
                # calculate acceleration
                a = G * planet2.mass / (r * r)
                ax = a * dx / r
                ay = a * dy / r
                # calculating total acceleration
                ax_total += ax
                ay_total += ay
        return(ax_total, ay_total)

        # draw method
    def draw(self, circle_x, circle_y, pixels_per_meter):
        for planet in self.body_list:
            planet.draw(circle_x, circle_y, pixels_per_meter)
