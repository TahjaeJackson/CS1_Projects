# Author: Tahjae Jackson
# Date: October 8, 2021
# Purpose:


def create_biglist(glol):
    biglist = []
    for i in range(0, len(glol)):
        for j in range(0, len(glol[i])):
            num = glol[i][j]
            biglist.append(num)

    return biglist

def find_max(glist):
    c_max = glist[0]
    for x in glist:
        if x > c_max:
            c_max = x

    return c_max

def find_max_lol(glol):
    bg_list = create_biglist(glol)
    max = find_max(bg_list)

    return max

# Method 2 of finding the max in a list of lists

def find_max_lol2(glol):
    final_max = glol [0][0]

    for gl in glol:
        local_max = find_max(gl)
        if local_max > final_max:
            final_max = local_max

    return final_max


