# Author: Aulanni Kidd
# Date: February 3, 2024
# Purpose: Pong Game

from cs1lib import *
from random import *

# constants
WINDOW_HEIGHT = 400 # setting window dimensions
WINDOW_WIDTH = 400 # setting window dimensions
PADDLE_HEIGHT = 80
PADDLE_WIDTH = 20
LEFT_PADDLE_X = 0 # making the left paddle x position constant
RIGHT_PADDLE_X = 379 # making the right paddle x position constant
RADIUS = 10 # constant size of ball
STARTING_VX = 4
STARTING_VY = -4
# to register the different keys for game play
A_PRESS = "a"
Z_PRESS = "z"
K_PRESS = "k"
M_PRESS = "m"
Q_PRESS = "q"
SPACE_BAR = " "
# variables
left_paddle_y = 0
right_paddle_y = 320
MOVE_PADDLE = 10 # amount that each paddle will move by when keys are pressed
press_a = False
press_k = False
press_z = False
press_m = False
press_q = False
start_game = False

# initial coordinates of ball
circle_x = 200
circle_y = 200
velocity_x = 0
velocity_y = 0
velocity_increase = 1.15


#  initial color of ball
r, g, b = 0, 0.95, 1

# setting background
def background():
    set_clear_color(0.7,0,0.5)
    clear()

# drawing paddles and setting initial coordinates
def create_paddles():
    set_stroke_color(0.3, 0, 1) # stroke colour of paddles
    set_stroke_width(2)
    set_fill_color(0.5, 0.5, 0.9) # fill colour of paddles
    draw_rectangle(LEFT_PADDLE_X,left_paddle_y,PADDLE_WIDTH, PADDLE_HEIGHT)
    draw_rectangle(RIGHT_PADDLE_X,right_paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT)

# drawing pong ball
def create_ball():
    global r,g,b
    set_stroke_color(r,g,b)
    set_fill_color(r,g,b)
    draw_circle(circle_x,circle_y, RADIUS)

# function for increments of paddles up and down
def paddle_movement():
    global press_a, press_z, press_k, press_m, left_paddle_y,right_paddle_y
    if (press_a == True) and (left_paddle_y > 0):
        left_paddle_y = left_paddle_y - MOVE_PADDLE
    if (press_z == True) and (left_paddle_y < WINDOW_HEIGHT-PADDLE_HEIGHT):
        left_paddle_y = left_paddle_y + MOVE_PADDLE
    if (press_k == True) and (right_paddle_y > 0):
        right_paddle_y = right_paddle_y - MOVE_PADDLE
    if (press_m == True) and (right_paddle_y < WINDOW_HEIGHT-PADDLE_HEIGHT):
        right_paddle_y = right_paddle_y + MOVE_PADDLE

# function for when ball hits paddle
def paddle_hit():
    global circle_x, circle_y, velocity_x, velocity_y, left_paddle_y, right_paddle_y,r,g,b
    if (PADDLE_WIDTH < circle_x) and (circle_x < PADDLE_WIDTH + 2*RADIUS):
        if (left_paddle_y < circle_y) and (circle_y < left_paddle_y + PADDLE_HEIGHT):
            velocity_x = - velocity_x * velocity_increase # changes the direction of the ball and increases the speed
            # changing the color of the ball if it is hit
            r = randint(0, 1)
            g = randint(0, 1)
            b = randint(0, 1)
    elif (WINDOW_WIDTH - PADDLE_WIDTH - 2 * (RADIUS) < circle_x) and (circle_x < WINDOW_WIDTH - PADDLE_WIDTH):
        if (right_paddle_y < circle_y) and (circle_y < right_paddle_y + PADDLE_HEIGHT ):
            velocity_x = - velocity_x *velocity_increase # negative to change the direction of the ball and increases the speed
            # changing the color of the ball if it is hit
            r = randint(0, 1)
            g = randint(0, 1)
            b = randint(0, 1)

# function for ball bouncing when horizontal walls (ceiling or floor) are hit
def wall_hit():
    global circle_y, velocity_y
    if circle_y > WINDOW_HEIGHT - RADIUS:
        velocity_y = - velocity_y
    if circle_y < RADIUS:
        velocity_y = - velocity_y

# function that resets game when wall is hit
def vertical_wall_hit():
    if circle_x < RADIUS:
        start_over()
    if circle_x > WINDOW_WIDTH - RADIUS:
        start_over()

# function that updates ball position
def ball_movement():
    global circle_x, circle_y, velocity_x, velocity_y
    circle_x = circle_x + velocity_x
    circle_y = circle_y + velocity_y

# function for when game-play keys are pressed
def my_kpress(value):
    global press_a, press_z, press_k, press_m, press_q, start_game, velocity_x, velocity_y
    if value == A_PRESS:
        press_a = True
    elif value == Z_PRESS:
        press_z = True
    elif value == K_PRESS:
        press_k = True
    elif value == M_PRESS:
        press_m = True
    elif value == Q_PRESS:
        press_q = True
    elif value == SPACE_BAR:
        velocity_x = STARTING_VX # resetting the initial velocity
        velocity_y = STARTING_VY # resetting the initial velocity
        start_game = True # starts the game

# function for when game-play keys are released
def my_krelease(value):
    global press_a, press_z, press_k, press_m, press_q
    if value == A_PRESS:
        press_a = False
    elif value == Z_PRESS:
        press_z = False
    elif value == K_PRESS:
        press_k = False
    elif value == M_PRESS:
        press_m = False
    elif value == Q_PRESS:
        press_q = False

def start_over():
    global circle_x, circle_y, left_paddle_y, right_paddle_y,LEFT_PADDLE_X,RIGHT_PADDLE_X, velocity_x, velocity_y
    # resetting game to starting position
    circle_x = 200
    circle_y = 200
    left_paddle_y = 0
    right_paddle_y = 320
    LEFT_PADDLE_X = LEFT_PADDLE_X
    RIGHT_PADDLE_X = RIGHT_PADDLE_X
    velocity_x = 0
    velocity_y = 0

# calling all relevant functions
def pong_p1():
    background()
    create_ball()
    create_paddles()
    paddle_hit()
    paddle_movement()
    ball_movement()
    wall_hit()
    vertical_wall_hit()
    if press_q == True: #cs1lib function that quits the program
        cs1_quit()

start_graphics(pong_p1, key_press = my_kpress, key_release = my_krelease)