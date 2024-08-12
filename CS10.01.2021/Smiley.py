#Author: Tahjae




from cs1lib import * #the * means all functions

X=200
Y= 200
bsize = 100
WIDTH = 400
HEIGHT = 400
bx = WIDTH//2
by = HEIGHT//2
mpressed = False
gpressed = False
spressed = False

# #Purpose: To draw the eyes
# #Parameters: x, y and size

def draw_eye (x,y,size):


    # OUTER CIRCLE
    enable_stroke()
    set_stroke_color(0,0,0)
    set_stroke_width(1)
    set_fill_color(1,1,1)
    draw_circle(x,y,size)

    #INNER CIRCLE
    set_fill_color(0,0,0)
    draw_circle(x,y-0.5*size, 0.5*size)




#Purpose: To draw an emoji that rolls its eyes
#Parameters: None

def smiley_draw (x, y, size, r, g, b):  #anything that I would like to drawn should be called within this function

    #SET THE BACKGROUND COLOUR
    set_clear_color(1,1,1) # this is used to change the background colour of the window that will be presented. To change the colour, we adjust the numbers in the brackets (red, green, blue)
    clear()

    #DRAW THE FACE
    set_fill_color(r,g,b)
    disable_stroke() #removes the border around the circle
    draw_circle(x,y,bsize)

    #DRAW EYES
    draw_eye(X-0.3 * bsize, Y-0.3*bsize, 0.2*bsize)
    draw_eye(X + 0.3 * bsize, Y - 0.3 * bsize, 0.2 * bsize)

    #DRAW MOUTH
    set_stroke_color(1,1,0)
    set_stroke_width(2)
    draw_line(X-0.3*bsize, Y+0.3*bsize, X+0.3*bsize,Y+0.3*bsize)


def my_mpress(mx,my):
    global mpresed
    mpressed = True

def my_release(mx,my):
    global mpressed
    mpressed = False

def my_move(mx,my):
    global bx, by

    if mpressed: #mpressed == True is another way of typing this condition
        bx = mx
        by = my

def my_kpress(value):
    global bsize

    if value == "g" and bsize<300:
        bsize = bsize + 10

    if value == "s" and bsize > 10:
        bsize = bsize - 10
def my_krelease():
    pass

start_graphics(smiley_draw, width = WIDTH, height = HEIGHT, mouse_press=my_mpress, mouse_release=my_release,mouse_move=my_move,
         key_press=my_kpress, key_release= my_krelease() ) #This is what outputs the graphics. Only one function can be put as a parameter



