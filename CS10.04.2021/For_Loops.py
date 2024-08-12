# Author: Tahjae Jackson
# Date: October 4, 2021
# Purpose: For Loops

#SYNTAX: for [variable name] in  [ending location] :

#Purpose: To find the maximum value in a list
#Parameter: A list of integers

def find_max(glist):
    max = glist[0]

    for i in glist: #goes through all the elements in the list
        if max < i:
            max = i
    return max

mlist = [4, 6, 20, -7, 8]
print(find_max(mlist))


#Purpose: To find the maximum value index in a list
#Parameter: A list of integers


def find_max_i(glist):
    max_i = 0

    for i in range(0, len(glist)):
        if glist[max_i] < glist[i]:
            max_i = i
    return max_i

mlist = [4, 6, 20, -7, 8]
print(find_max_i(mlist))