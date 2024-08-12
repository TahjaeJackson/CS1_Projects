# Aithor: Tahjae  Jackson
# Date
# Purpose: Demo cs1lib by drawing rolling eyes smiley

from cs1lib import * #the * means all functions

X=200
Y= 200
SIZE = 100

# #Purpose: To draw the eyes
# #Parameters: x, y and size

def draw_eye (x,y,size):


    # OUTER CIRCLE
    enable_stroke()
    set_stroke_color(0,0,0)
    set_stroke_width(1)
    set_fill_color(1,0,0)
    draw_circle(x,y,size)

    #INNER CIRCLE
    set_fill_color(0,0,0)
    draw_circle(x,y-0.5*size, 0.5*size)




#Purpose: To draw an emoji that rolls its eyes
#Parameters: None

def smiley_draw ():  #anything that I would like to drawn should be called within this function

    #SET THE BACKGROUND COLOUR
    set_clear_color(1,0,0) # this is used to change the background colour of the window that will be presented. To change the colour, we adjust the numbers in the brackets (red, green, blue)
    clear()

    #DRAW THE FACE
    set_fill_color(1,1,0)
    disable_stroke() #removes the border around the circle
    draw_circle(X,Y,SIZE)

    #DRAW EYES
    draw_eye(X-0.3* SIZE, Y-0.3*SIZE, 0.2*SIZE)
    draw_eye(X + 0.3 * SIZE, Y - 0.3 * SIZE, 0.2 * SIZE)

    #DRAW MOUTH
    set_stroke_color(1,0,0)
    set_stroke_width(2)
    draw_line(X-0.3*SIZE, Y+0.3*SIZE, X+0.3*SIZE,Y+0.3*SIZE)


start_graphics(smiley_draw) #This is what outputs the graphics. Only one function can be put as a parameter



#the window that is displayed by this code is 400 x 400 pixels