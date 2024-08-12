# Name: Tahjae Jackson
# Date: November 15, 2021
# Purpose: To create a vertex class

from cs1lib import *

RAD = 7
WIDTH = 3
N = RAD + 2

class Vertex:
    def __init__(self, name, x, y):
        self.name = name
        self.x = int(x)
        self.y = int (y)
        self.adj = []


    def __str__(self):
        adj = ""
        for a in range(0, len(self.adj)):
            if a == len(self.adj) - 1:
                comma = ""
            else:
                comma = ", "
            adj = adj + self.adj[a].name + comma
        return self.name + "; Location: " + str(self.x) + ", " + str(self.y) + "; Adjacent verticies: " + adj

    def draw_vertex(self,r,g,b):
        disable_stroke()
        set_fill_color(r,g,b)
        draw_circle(self.x, self.y, RAD)

    def draw_edge(self,vertex,r,g,b):
        enable_stroke()
        set_stroke_color(r,g,b)
        set_stroke_width(WIDTH)
        draw_line(self.x,self.y,vertex.x,vertex.y)

    def draw_all_edges(self,r,g,b):
        for adjacents in self.adj:
            self.draw_edge(adjacents,r,g,b)

    def location(self,x,y):
        return ((x>=self.x - N and x<=self.x + N) and (y>=self.y - N and y <= self.y + N))

