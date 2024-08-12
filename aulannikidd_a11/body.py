# Name: Aulanni Kidd
# Date: February 13, 2024
# Purpose: Body Class

from cs1lib import *

class Body:
    # initialization method
    def __init__(self, mass, x, y, v_x, v_y, image_file,scale_factor):
        self.mass = mass
        self.x = x  # x location of body
        self.y = y  # y location of body
        self.v_x = v_x  # x-axis velocity
        self.v_y = v_y  # y-axis velocity
        # colours for planets
        default_image = load_image(image_file)
        width=default_image.size().width()
        height = default_image.size().height()
        self.image = default_image.scaled(width * scale_factor,height*scale_factor)



    # method to update position
    def update_position(self, timestep):
        self.x += self.v_x * timestep
        self.y += self.v_y * timestep

    # method to update velocity
    def update_velocity(self, ax, ay, timestep):
        self.v_x += ax * timestep
        self.v_y += ay * timestep

    # draw method
    def draw(self, cx, cy, pixels_per_meter):
        # set_fill_color(self.r, self.g, self.b)
        px = (self.x * pixels_per_meter) + cx
        py = (self.y * pixels_per_meter) + cy

        # draw_circle(px, py, self.pixel_radius)
        draw_image(self.image,px,py)