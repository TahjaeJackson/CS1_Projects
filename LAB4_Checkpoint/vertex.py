# Name: Tahjae Jackson
# Date: November 15, 2021
# Purpose: To create a vertex class

class Vertex:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        self.adj = []


    def __str__(self):
        adj = ""
        for a in range(0, len(self.adj)):
            if a == len(self.adj) - 1:
                comma = ""
            else:
                comma = ", "
            adj = adj + self.adj[a].name + comma
        return self.name + "; Location: " + str(self.x) + ", " + str(self.y) + "; Adjacent vertices: " + adj