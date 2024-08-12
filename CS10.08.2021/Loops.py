# Author: Tahjae Jackson
# Date: October 8, 2021
# Purpose:

list = [-2, 700, 39, 23, 1015]


def order(mlist):

    for j in range(0, len(mlist)-1):
        for i in range(0, len(mlist)-1):
            if mlist[i] > mlist [i+1]:
                temp = mlist[i]
                mlist[i] = mlist[i+1]
                mlist[i+1] = temp

    return mlist

def is_increasing(glist):
    for i in range(0,len(glist)-1):
        if glist[i] > glist[i+1]:
            return False

    return True


# Parameter: Is a list of lists, where each inner list is a list of integers
def all_increasing(glol):
    for gl in glol:
        check = is_increasing(gl)
        if check == False:
            return False

    return True


def atleast_1_increasing():
    for gl in glol:
        check = is_increasing(gl)
        if check:


xlist = [[5, 7, 2], [20, 5, 3, 4], [6, -14, 5]]

print(order(list))


