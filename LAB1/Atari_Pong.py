# Author: Tahjae Jackson
# Date: October 6, 2021
# Purpose: To design a game that is similar to the popular atari pong game

from cs1lib import *

WIDTH = 400
HEIGHT = 400
REC_WIDTH = 20
REC_HEIGHT = 80
LINE_LENGTH = 30
LINE_WIDTH = 10
LINE_X = 195
line_y = 0
horizontal = WIDTH//2  #the starting x position of the ball
vertical = HEIGHT//2   #the starting y position of the ball
RIGHT_WALL = 400
LEFT_WALL = 0
TOP_WALL = 0
BOTTOM_WALL = 400
RAD = 10
left_x = 0
left_y = 0
right_x = 380
right_y = 320
rightwall_hit = False
leftwall_hit = False
MOVE = 5 # The amount each paddle moves by
vx = 5
vy = 5
LEFT_UP = "a"
LEFT_DOWN = "z"
RIGHT_UP = "k"
RIGHT_DOWN = "m"
QUIT = "q"
SPACE = " " #Key that would restart the game
a_press = False
z_press = False
k_press = False
m_press = False
restart = False
paddlehit = False
touch_right = False
touch_left = False
leftscore = 0
rightscore = 0
game_end = False
TOP_LIMIT = 0
BOTTOM_LIMIT = 320
CENTRE_LINE_DISTANCE = 40
maxscore = 5



# Purpose: This is main function that will be inputted into the start graphics
# Parameters: There are none

def main_draw():
    global in_progress
    if game_end == False:
        background()
        left_paddle(left_x,left_y)
        right_paddle(right_x,right_y)
        centre_line()
        ball()


# Purpose: This set the background colour of the game
# Parameters: There are none

def background():
    global r, g, b
    black()
    set_clear_color(r,g,b)
    clear()

# Purpose: To draw the left paddle and manipulate its movement
# Parameters: two values that store the coordinates that indicate where to draw the rectangle from

def left_paddle(s, t):
    global left_x, left_y, r, g, b
    disable_stroke()
    purple()
    set_fill_color(r, g, b)
    if a_press and t != TOP_LIMIT:
        t = t - MOVE
    if z_press and t != BOTTOM_LIMIT:
        t = t + MOVE
    left_y = t
    draw_rectangle(s,t,REC_WIDTH,REC_HEIGHT)

# Purpose: To draw the right paddle and manipulate its movement
# Parameters: two values that store the coordinates that indicate where to draw the rectangle from

def right_paddle(p, q):
    global right_x, right_y, r, g, b
    disable_stroke()
    purple()
    set_fill_color(r,g,b)
    if k_press == True and q != TOP_LIMIT:
        q = q - MOVE
    if m_press and q != BOTTOM_LIMIT:
        q = q + MOVE
    right_y = q
    draw_rectangle(p, q, REC_WIDTH,REC_HEIGHT)

#Purpose: To draw the ball to be used in the game
#Parameters: There are none

def ball():
    global r, g, b, horizontal, vertical, vx, vy, touch_right, touch_left, in_progress, restart
    white()
    enable_stroke()
    set_fill_color(r, g, b)
    set_stroke_color(r, g, b)
    horizontal = horizontal + vx
    vertical = vertical + vy
    in_progress = True
    rightwall_check(horizontal, RIGHT_WALL)
    leftwall_check(horizontal, LEFT_WALL)
    if leftwall_hit == True or rightwall_hit == True:
        in_progress = False
    if in_progress == False:
        horizontal = WIDTH//2
        vertical = HEIGHT//2
    bounce(horizontal, vertical)
    touch_right = False
    touch_left = False
    draw_circle(horizontal, vertical, RAD)


#Purpose: To draw the centre line
#Parameters: There are none

def centre_line():
    global line_y, r, g, b
    lightpurple()
    line_y = 0
    set_fill_color(r,g,b)
    while line_y < BOTTOM_WALL:
        draw_rectangle(LINE_X, line_y, LINE_WIDTH, LINE_LENGTH)
        line_y = line_y + CENTRE_LINE_DISTANCE


#Purpose: To check if the ball has gotten to the edge of the right screen
#Parameters: The coordinate of the centre of the ball and the wall coordinate

def rightwall_check(x, wall_coordinate):
    global rightwall_hit, leftscore

    if x > wall_coordinate - RAD:
        rightwall_hit = True
        leftscore = leftscore + 1
    else:
        rightwall_hit = False


#Purpose: To check if the ball has gotten to the edge of the left screen
#Parameters: The coordinate of the centre of the ball and the wall coordinate

def leftwall_check(x, wall_coordinate):
    global leftwall_hit, rightscore

    if x < wall_coordinate + RAD:
        leftwall_hit = True
        rightscore = rightscore + 1
    else:
        leftwall_hit = False


#Purpose: To allow the ball to bounce when it comes in contact with a surface
#Parameters: The location of the ball and the velocity

def bounce(x,y):
    global vx, vy, left_x, right_x, right_y, touch_right, touch_left, in_progress
    if x >= right_x and y>=right_y and y <= right_y + REC_HEIGHT:
        touch_right = True

    if x <= left_x + REC_WIDTH and y>= left_y and y <= left_y + REC_HEIGHT:
        touch_left = True

    if touch_right == True or touch_left == True:
        in_progress = True
        vx = vx * -1
    else:
        in_progress = False


    if y <= TOP_WALL or y >= BOTTOM_WALL:
        vy = vy * -1




#Purpose: To check if a certain key is pressed
#Parameters: A character value called key that stores the value that is pressed

def k_press (key):
    global a_press, z_press, k_press, m_press, horizontal, vertical, game_end

    if key == LEFT_UP:
        a_press = True

    if key == LEFT_DOWN:
        z_press = True

    if key == RIGHT_UP:
        k_press = True

    if key == RIGHT_DOWN:
        m_press = True

    if key == QUIT:
        cs1_quit()

    if key == SPACE:
        game_end = False
        horizontal = WIDTH // 2
        vertical = HEIGHT // 2
        ball()


#Purpose: To check if a certain key is released
#Parameters: A character value called key that stores the value that is released

def my_krelease(key):
    global a_press, z_press, k_press, m_press
    if key == LEFT_UP:
        a_press = False

    if key == LEFT_DOWN:
        z_press = False

    if key == RIGHT_UP:
        k_press = False

    if key == RIGHT_DOWN:
        m_press = False





# Purpose: This set the colour to red
# Parameters: There are none

def red():
    global r, g, b
    r = 1
    g = 0
    b = 0

# Purpose: This set the colour to white
# Parameters: There are none

def white():
    global r, g, b
    r = 1
    g = 1
    b = 1

# Purpose: This set the colour to black
# Parameters: There are none

def black():
    global r, g, b
    r = 0
    g = 0
    b = 0

# Purpose: This set the colour to green
# Parameters: There are none

def green():
    global r, g, b
    r = 0
    g = 1
    b = 0

# Purpose: This set the colour to blue
# Parameters: There are none

def blue():
    global r, g, b
    r = 0
    g = 0
    b = 1

# Purpose: This set the colour to light purple
# Parameters: There are none

def lightpurple():
    global r, g, b
    r = 203/255
    g = 195/255
    b = 227/255

# Purpose: This set the colour to purple
# Parameters: There are none

def purple():
    global r, g, b
    r = 176/255
    g = 38/255
    b = 255/255

start_graphics(main_draw, width = WIDTH, height = HEIGHT, key_press = k_press, key_release = my_krelease)

