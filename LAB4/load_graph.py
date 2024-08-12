# Name: Tahjae Jackson
# Date: November 15, 2021
# Purpose: Using information read from a file to turn them into vertex objects for graphingLAB4_Checkpoint

from vertex import *


# Purpose: To parse a line within a text file
# Parameters: A line from the file
# Return: The vertex and x and y coordinates in the line

def parse_line(line):

    # separates the content of the line by a semicolon
    section_split = line.split(";")
    vertex_name = section_split[0].strip()
    coordinates_val = section_split[2].strip().split(",")

    coordinates = []

    for i in coordinates_val:
        if i:
            coordinates.append(i.strip())

    x = coordinates[0]
    y = coordinates[1]

    return vertex_name, x, y


# Purpose: To create a diction of vertex objects from a file
# Parameters: A text file
# Return: Ta dictionary with vertex objects

def load_graph(filename):
    vertex_dict = {}

    # Read the lines in the file into a list of lines:
    file = open(filename, "r")

    # Initial opening of the file to create vertex objects
    for l in file:

        # if this is a line in the correct format:
        if len(l.split(";")) == 3:
            vertex_name, x, y = parse_line(l)
            vertex_dict[vertex_name] = Vertex(vertex_name,x,y)

    file.close()

    # second opening of the file to append to the adjacent instance variable of each vertex
    file = open(filename,"r")
    for l in file:
        if len(l.split(";")) == 3:
            section_split = l.split(";")
            vertex_name = section_split[0].strip()
            adjacent_vertices = section_split[1].strip().split(",")
            adjacent = []

            for a in adjacent_vertices:
                if a:
                    adjacent.append(a.strip())

            for x in adjacent:
                if x in vertex_dict:
                    vertex_dict[vertex_name].adj.append(vertex_dict[x])

    file.close()
    return vertex_dict

print(load_graph("dartmouth_graph"))