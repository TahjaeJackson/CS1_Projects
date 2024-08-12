# Author: Tahjae Jackson
# Date: October 11, 2021
# Purpose:


# Create function that will separate a list into a list of lists of positive and negative negative

def neg_pos(glist):
    glol = [[],[]]
    for x in glist:
        if x < 0:
            glol[0].append(x)
        else:
            glol[1].append(x)

    return glol

print(neg_pos([1, 4, -8, 9, 45, -3, -6, 45]))


# Purpose: Find the length of the longest sting in the given list of strings
# Parameter: A  non-empty list of non-empty strings
# Return: The maximum length of string

def find_max_length(glist):
    max_l = len(glist[0])

    for s in glist:
        if len(s) > max_l:
            max_l = len(s)

    return max_l

# Parameter: A list of empty strings
#  Return: A list of lists, where each inner list contains strings in given list.

def by_len(glist):
    rlist = []
    if len(glist) == 0:
        return rlist

    maxl = find_max_length(glist)

    for r in range(0, maxl): # Putting the 0 in the range is not necessary. If you leave it out, it will automatically start at 0
        rlist.append([])

    for s in glist:
        indx = len(s) - 1
        rlist[indx].append(s)

    # Always decrement when deleting from a list
    for i in range(len(rlist)-1, -1, -1): # The first -1 is to start at the last element, the second is to include the last value, and the last is t decrement
        if rlist[i] == []:
            del rlist[i]


    return rlist

print(by_len(["max", "x", "min", "exam", "testing", "dartmouth", "a", "test"]))