# Name: Tahjae Jackson
# Date: November 13, 2021
# Purpose: To use graphing principles to create a game where you decide your output

# I am using a late day for this assignment

from vertex import *

def parse_line(line):
    section_split = line.split("|")
    vertex_name = section_split[0].strip()

    adjacent_vertices = section_split[1].strip().split(",")

    # add all except empty strings
    adjacent = []
    for a in adjacent_vertices:
        if a:
            adjacent.append(a.strip())

    text = section_split[2].strip()

    return vertex_name, adjacent, text


def load_story(filename):

    vertex_dict = {}

    # Read the lines in the file into a list of lines:
    file = open(filename, "r")

    for l in file:

        # if this is a line in the correct format:
        if len(l.split("|")) == 3:
            vertex_name, adjacent_vertices, text = parse_line(l)
            #
            # print("vertex " + vertex_name)
            # print(" adjacent:  " + str(adjacent_vertices))
            # print(" text:  " + text)

        # YOU WRITE THIS PART
        # create a graph vertex here and add it to the dictionary
            vertex_dict[vertex_name] = Vertex(vertex_name, adjacent_vertices,text)

    file.close()

    return(vertex_dict)



# Purpose: to execute the functionality of the game
# Parameters: A dictionary
# Return: There are none


def game(dict):
    print(dict["START"].text)

    indx = ord(input("Enter your choice: ")) - ord("a")
    vertex = dict["START"].adjacent[indx]

    print(dict[vertex].text)

    while len(dict[vertex].adjacent) > 0:

        indx = ord(input("Enter your choice: ")) - ord("a")
        vertex = dict[vertex].adjacent[indx]

        print(dict[vertex].text)


story_dict = load_story("story")
game(story_dict)