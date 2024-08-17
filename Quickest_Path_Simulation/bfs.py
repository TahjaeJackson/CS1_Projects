# Name: Tahjae Jackson
# Date: November 17, 2021
# Purpose: To create a function that determines the path between two locations on a map

from collections import deque

# Purpose: To determine path needed to be followed between two vertices
# Parameter: Two vertex objects
# Return: a path between the two vertices which is a list of adjacent vertices.

def breadth_first(start,goal):
    frontier = deque()
    bkp_d = {}

    frontier.append(start)
    bkp_d[start] = None

    while len(frontier) > 0:
        v = frontier.popleft()
        for u in v.adj:
            if u not in bkp_d:
                frontier.append(u)
                bkp_d[u] = v

        if goal in bkp_d:
            break

    path = []
    x = goal
    while x != None:
        path.append(x)
        if x in bkp_d:
            x = bkp_d[x]

    return path



