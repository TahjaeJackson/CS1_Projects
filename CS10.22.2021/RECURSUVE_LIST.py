# Name: Tahjae Jackson
# Date: October 22, 2021
# Purpose: Demo to recursion

def sumlist(glist):
    if len(glist) == 0:
        return 0

    small_list = glist[1:]
    x = sumlist(small_list)

    return x + glist[0]