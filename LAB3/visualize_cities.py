# Name: Tahjae Jackson
# Date: November 8, 2021
# Purpose: To use graphics to display the 50 most populated cities in the world on a map

from cs1lib import *
fp1 = open("cities_population.txt", "r")

W = 720
H = 360
PIXEL_PER_DEGREE = 2 # This is the scare factor used for the window

# These variables are used to create the illusion of the centre of the window being (0,0)
MID_H = H//2
MID_W = W//2

# Lists that store tha latitude and longitude values of each country
x_val = []
y_val = []

size = 1
count = 0
FRAMES = 20
F_RATE = 10
clear_num = 0
city_num = 50


# Purpose: To create backgroud map for the animation
# Parameters: There are none
# Return: nothing

def background():
    global clear_num
    set_clear_color(1, 1, 1)

    # ensures that the background is only drawn once
    if clear_num == 0:
        clear()
        img = load_image("world.png")
        draw_image(img, 0, 0)
    clear_num += 1


# Purpose: To create the animation to be called by start graphics
# Parameters: none
# Return: nothing

def main():
    global size, count, city_num
    background()


    # This for loop appends the lattitude and longitude of each city within the file into a list
    for l in fp1:
        data = l
        data = data.strip("\n")
        info = data.split(",")
        c = [info[0], info[1], info[2], info[3]]
        x = MID_W + int(float(c[3])) * PIXEL_PER_DEGREE
        y = MID_H - int(float(c[2])) * PIXEL_PER_DEGREE
        x_val.append(x)
        y_val.append(y)

    #This if-statement is responsible for animating the circles on the map
    if size != 4  and count < city_num:
        set_fill_color(1, 0, 0)
        draw_circle(x_val[count], y_val[count], size)
        size = size + 1
    else:
        count = count + 1
        size = 1

start_graphics(main, width= W, height= H, frames=FRAMES, framerate=F_RATE)
fp1.close()