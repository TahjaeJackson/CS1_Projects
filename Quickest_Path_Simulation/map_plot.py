# Name: Tahjae Jackson
# Date: November 17, 2021
# Purpose: Using graphing principles to draw a path between two locations on a map

from cs1lib import *
from load_graph import load_graph
from bfs import *

vertex_dict = load_graph("dartmouth_graph")

W = 1012
H = 811

# Initialization of global variables to be called

x_val = None
y_val= None
hover_x = None
hover_y = None
press = False
count = None
start = None
goal = None

# Purpose: To draw the background image of the map on the window
# Parameter: There are none
# Return: Nothing

def background():
    global count
    if count == None:
        img = load_image("dartmouth_map.png")
        draw_image(img, 0, 0)
        count = 1

# Purpose: To get the location of the mouse when it is pressed on the window
# Parameters: Two values that will store the pixel location of the mouse
# Return: Nothing

def m_press(mx, my):
    global x_val, y_val, press
    press = True
    x_val = mx
    y_val = my

# Purpose: To update the current position of the mouse as it moves
# Parameters: Two values to store the coordinates of the mouse location
# Return: Nothing

def m_move(mx, my):
    global hover_x, hover_y
    hover_x = mx
    hover_y = my


# Purpose: The main draw function to execute the graphing of vertices on the map
# Parameter: There is none
# Return: Nothing

def main():
    global x_val, y_val, press, hover_x, hover_y, start, goal
    background()

    # initial drawing of the vertices and their edges
    for x in vertex_dict:
        vertex_dict[x].draw_vertex(0,0,1)
        vertex_dict[x].draw_all_edges(0,0,1)


    for x in vertex_dict:
        if press:
            if vertex_dict[x].location(x_val, y_val):
                start = vertex_dict[x]
                start.draw_vertex(1, 0, 0)


            if start != None: #If there is no start, then there can be no goal
                if vertex_dict[x].location(hover_x, hover_y):
                    goal = vertex_dict[x]
                    goal.draw_vertex(1, 0, 0)

                    if goal!=None:

                        # drawing of the path
                        list = breadth_first(start,goal)
                        for x in range (0,len(list)-1):
                            list[x].draw_edge(list[x+1],1,0,0)
                            list[x].draw_vertex(1,0,0)






start_graphics(main, width=W, height=H,mouse_press=m_press, mouse_move= m_move)