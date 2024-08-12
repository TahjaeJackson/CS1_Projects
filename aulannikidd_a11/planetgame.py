# Name: Aulanni Kidd
# Date: February 13, 2024
# Purpose: planet game


from cs1lib import *
import random



# Constants
WIDTH, HEIGHT = 1500, 1500
FRAMERATE = 60


# Planet class
class Planet:
    def __init__(self, x, y, planet_image):
        self.default_image = load_image(planet_image)
        self.width = self.default_image.size().width()
        self.height = self.default_image.size().height()
        self.scale = 0.05
        self.image = self.default_image.scaled(self.width * self.scale, self.height * self.scale)

        self.mass = 1
        self.x = x
        self.y = y

    def grow(self):
        self.scale += 0.1
        self.image = self.default_image.scaled(self.width * self.scale,self.height*self.scale)

    def draw(self):
        draw_image(self.image, self.x - 15 * self.mass, self.y - 15 * self.mass, 30 * self.mass, 30 * self.mass)


# Creating planet objects
earth = Planet(0, 0, "earth.jpg")           # blue earth
sun = Planet(0,0,  "sun.png") # yellow sun
mercury = Planet(0,0, "mercury.jpg") # red mercury
venus = Planet(0,0, "venus.jpg")
mars = Planet(0,0, "mars.jpg")
# List for storing planets
planets = []

# Main game loop


# Main game loop
space_pressed = False
current_planet = None


def draw():
    global space_pressed

    clear()
    set_clear_color(0, 0, 0)  # black background

    for planet in planets:
        planet.draw()

    # Grow the current planet if the space bar is held down
    if space_pressed and current_planet is not None:
        current_planet.grow()

def key_pressed(key):
    global space_pressed, current_planet

    if key == " " and not space_pressed:
        space_pressed = True

        # randomly selecting which planet to draw
        planet_choice = random.randint(1, 5)

        if planet_choice == 1:
            current_planet = mercury
        elif planet_choice == 2:
            current_planet = venus
        elif planet_choice == 3:
            current_planet = earth
        elif planet_choice == 4:
            current_planet = mars
        elif planet_choice == 5:
            current_planet = sun
        else:
            current_planet = earth  # default planet is set to earth

        planets.append(current_planet)

def key_released(key):
    global space_pressed

    if key == " ":
        space_pressed = False



start_graphics(draw, key_press=key_pressed, key_release=key_released, width=WIDTH, height=HEIGHT,
               framerate=FRAMERATE)

