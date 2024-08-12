# Author: Tahjae Jackson
# Date: September 27, 2021
# Course: COSC1
# File: drawing.py in SA3
# Purpose: Using Graphics to create a book cover
# Brief: Anancy (Spider) is a popular Jamaica character that is featured in many short stories told young Jamaican students.
from cs1lib import *

CENTRE_X = 250
CENTRE_Y = 350
SIZE = 100
#Purpose: To adjust the background colour of the image
#Parameters: There are none

def background_colour():
    set_clear_color(0.5294, 0.8078, 0.9216)
    clear()


#Purpose: To display the entire image of anancy
#Parameters: There are none

def anancy():

    background_colour()

    body()
    head()
    eyes()
    mouth()
    legs()
    hat()
    hair()

    name_output()

#Purpose: To display the body of anancy
#Parameters: There are none
def body():
    set_fill_color(50/255, 168/255, 37/255)
    enable_stroke()
    set_stroke_color(0,0,0)
    draw_ellipse(CENTRE_X,CENTRE_Y,140,200)
    disable_stroke()
    set_fill_color(1,1,0)
    draw_rectangle(155,CENTRE_Y,190,150)
    draw_ellipse(250, 500, 91,50)
    draw_triangle(345,CENTRE_Y,345,500,390,CENTRE_Y)
    draw_triangle(155, CENTRE_Y, 155, 500, 110, CENTRE_Y)
    #rotate(0.5)
    draw_rectangle(110,CENTRE_Y,280,55)
    draw_ellipse(340,410,40,78.3,)
    draw_ellipse(160, 410, 40, 78.3,)
    set_fill_color(50/255, 168/255, 37/255)
    draw_rectangle(115,CENTRE_Y-55,270,55)
    set_stroke_color(17/255, 30/255, 94/255)
    set_fill_color(17/255, 30/255, 94/255)
    draw_rectangle(CENTRE_X-140,CENTRE_Y, 280, 15)
    # set_stroke_width(10)
    #draw_line(CENTRE_X-140,CENTRE_Y,CENTRE_X+140,CENTRE_Y)
    set_stroke_color(17/255, 30/255, 94/255)
    set_fill_color(17/255, 30/255, 94/255)
    draw_ellipse(CENTRE_X, CENTRE_Y - 20, 7,10)
    draw_ellipse(CENTRE_X, CENTRE_Y - 55, 5, 7)
    draw_ellipse(CENTRE_X, CENTRE_Y - 85, 3, 5)

#Purpose: This function creates the head of the image
#Parameter: There are no parameters

def head():
    enable_stroke()
    set_stroke_color(0,0,0)
    set_fill_color(130/255,90/255,44/255)
    draw_circle(CENTRE_X, 150, 80)

#Purpose: This function is responsible for drawing the eyes of the image
#Parameter: There is none

def eyes():
    set_fill_color(1,1,1)
    draw_circle(CENTRE_X-50,130,27)
    draw_circle(CENTRE_X+50,130,27)
    set_fill_color(0,0,0)
    draw_circle(CENTRE_X-50,134,23)
    draw_circle(CENTRE_X+50,134,23)

#Purpose: To create the smile of the image
#Parameter: There are no parameters

def mouth():
    set_fill_color(1,1,1)
    set_stroke_width(2)
    draw_ellipse(CENTRE_X,CENTRE_Y-160,50,30)
    enable_stroke()
    set_stroke_color(0,0,0)
    set_fill_color(1,1,1)
    draw_ellipse(CENTRE_X, CENTRE_Y - 170, 50, 30)
    disable_stroke()
    set_fill_color(130 / 255, 90 / 255, 44 / 255)
    draw_ellipse(CENTRE_X,CENTRE_Y-177,50,25)
    set_stroke_color(0,0,0)
    set_fill_color(0,0,0)
    draw_rectangle(CENTRE_X-45 , CENTRE_Y-166,2,20)
    draw_rectangle(CENTRE_X - 35, CENTRE_Y - 161, 2, 23)
    draw_rectangle(CENTRE_X - 25, CENTRE_Y - 158, 2, 25)
    draw_rectangle(CENTRE_X - 15, CENTRE_Y - 156, 2, 26)
    draw_rectangle(CENTRE_X - 5, CENTRE_Y - 153, 2, 25)
    draw_rectangle(CENTRE_X + 45, CENTRE_Y - 166, 2, 20)
    draw_rectangle(CENTRE_X + 35, CENTRE_Y - 161, 2, 23)
    draw_rectangle(CENTRE_X + 25, CENTRE_Y - 158, 2, 25)
    draw_rectangle(CENTRE_X + 15, CENTRE_Y - 156, 2, 26)
    draw_rectangle(CENTRE_X + 5, CENTRE_Y - 153, 2, 25)
    enable_stroke()

    #draw_line(CENTRE_X-50 , CENTRE_Y-160 ,CENTRE_X+50 , CENTRE_Y-160 )


#Purpose: To display the draw the legs of the spider
#Parameters: There are none
def legs():
    set_stroke_color(0, 0, 0)
    set_fill_color(0, 0, 0)
    draw_rectangle(CENTRE_X-200,CENTRE_Y-5, 60,10)
    draw_rectangle(CENTRE_X + 140, CENTRE_Y-5, 60, 10)
    draw_rectangle(CENTRE_X - 200, CENTRE_Y - 60, 10, 60)
    draw_rectangle(CENTRE_X + 200, CENTRE_Y - 60, 10, 65)
    draw_rectangle(CENTRE_X - 200, CENTRE_Y + 55, 70, 10)
    draw_rectangle(CENTRE_X + 130, CENTRE_Y + 55, 70, 10)
    draw_rectangle(CENTRE_X - 200, CENTRE_Y + 55, 10, 70)
    draw_rectangle(CENTRE_X + 200, CENTRE_Y + 55, 10, 70)
    draw_rectangle(CENTRE_X - 200, CENTRE_Y-100, 77, 10)
    draw_rectangle(CENTRE_X +124, CENTRE_Y - 100, 77, 10)
    draw_rectangle(CENTRE_X - 200, CENTRE_Y-170, 10, 77)
    draw_rectangle(CENTRE_X +200, CENTRE_Y - 170, 10, 80)
    draw_rectangle(CENTRE_X - 200, CENTRE_Y + 140,105, 10)
    draw_rectangle(CENTRE_X +95, CENTRE_Y + 140, 105, 10)
    draw_rectangle(CENTRE_X - 200, CENTRE_Y + 140,10, 90)
    draw_rectangle(CENTRE_X +200, CENTRE_Y + 140, 10, 90)


#Purpose: To draw the hat of the spider
#Parameters: There are none
def hat():
    set_fill_color(0,0,0)
    draw_ellipse(CENTRE_X,60,50,20)
    enable_stroke()
    set_stroke_color(0,0,0)
    set_fill_color(1,0,0)
    draw_rectangle(CENTRE_X-50,60,100,10)
    set_fill_color(1,1,0)
    draw_rectangle(CENTRE_X - 50, 70, 100, 10)
    set_fill_color(0,1,0)
    draw_rectangle(CENTRE_X - 50, 80, 100, 10)

# Purpose: To draw the locs on to the character
# Parameter: There are none

def hair():
    enable_stroke()
    set_stroke_color(0,0,0)

    #BANGS
    draw_line(CENTRE_X - 53, 90, CENTRE_X - 53, 105)
    draw_line(CENTRE_X - 50, 90, CENTRE_X - 52, 105)
    draw_line(CENTRE_X -45, 90, CENTRE_X  -43, 105)
    draw_line(CENTRE_X - 40, 90, CENTRE_X -40, 108)
    draw_line(CENTRE_X - 41, 90, CENTRE_X + -41, 106)
    draw_line(CENTRE_X - 38, 90, CENTRE_X - 38, 105)
    draw_line(CENTRE_X - 33, 90, CENTRE_X - 33, 106)
    draw_line(CENTRE_X - 30, 90, CENTRE_X - 30, 107)
    draw_line(CENTRE_X - 27, 90, CENTRE_X - 26, 109)
    draw_line(CENTRE_X - 23, 90, CENTRE_X - 24, 106)
    draw_line(CENTRE_X - 19, 90, CENTRE_X - 19, 115)
    draw_line(CENTRE_X - 14, 90, CENTRE_X - 19, 106)
    draw_line(CENTRE_X - 9, 90, CENTRE_X - 9, 110)
    draw_line(CENTRE_X - 4, 90, CENTRE_X - 3, 107)
    draw_line(CENTRE_X + 1, 90, CENTRE_X - 1, 112)
    draw_line(CENTRE_X + 3, 90, CENTRE_X + 3, 105)
    draw_line(CENTRE_X + 8, 90, CENTRE_X + 8, 105)
    draw_line(CENTRE_X + 11, 90, CENTRE_X + 12, 113)
    draw_line(CENTRE_X + 17, 90, CENTRE_X + 17, 109)
    draw_line(CENTRE_X + 20, 90, CENTRE_X + 19, 115)
    draw_line(CENTRE_X + 23, 90, CENTRE_X + 23, 114)
    draw_line(CENTRE_X + 29, 90, CENTRE_X + 29, 110)
    draw_line(CENTRE_X + 31, 90, CENTRE_X + 31, 109)
    draw_line(CENTRE_X+30,90,CENTRE_X+30,100)
    draw_line(CENTRE_X + 36, 90, CENTRE_X + 36, 104)
    draw_line(CENTRE_X + 41, 90, CENTRE_X + 41, 105)
    draw_line(CENTRE_X + 46, 90, CENTRE_X + 45, 105)
    draw_line(CENTRE_X + 51, 90, CENTRE_X + 52, 106)

    #RIGHT SIDE OF HAIR
    draw_line(CENTRE_X+55,90, CENTRE_X + 65, 93)
    draw_line(CENTRE_X + 57, 94, CENTRE_X + 68, 96)
    draw_line(CENTRE_X + 59, 99, CENTRE_X + 70, 102)
    draw_line(CENTRE_X + 62, 105, CENTRE_X + 75, 109)
    draw_line(CENTRE_X + 67, 110, CENTRE_X + 70, 116)

    #LEFT SIDE OF HAIR
    draw_line(CENTRE_X - 55, 90, CENTRE_X - 65, 93)
    draw_line(CENTRE_X - 57, 94, CENTRE_X - 68, 96)
    draw_line(CENTRE_X - 59, 99, CENTRE_X - 70, 102)
    draw_line(CENTRE_X - 62, 105, CENTRE_X - 75, 109)
    draw_line(CENTRE_X - 67, 110, CENTRE_X - 70, 116)




# Purpose: To display my name onto the window
# Parameter: There are none

def name_output():
    enable_stroke()
    set_font("Times")
    set_font_bold()
    set_font_italic()
    set_font_size(20)
    set_stroke_color(1,1,1)
    name = "Tahjae Jackson"
    w = get_text_width(name)

    draw_text(name, 350 - w // 2, 650)
    # draw_text("Tahjae Jackson",600,1000)



start_graphics(anancy, width=500,height=700)