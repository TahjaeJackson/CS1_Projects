# Author: Tahjae Jackson
# Date: October 4, 2021
# Purpose: Lists demo


#Purpose: Sum of all elements of a list of integers
#Parameter: A list of integers

def sum(glist):
    i = 0
    sum = 0

    while i<len(glist):
        sum = sum + glist[i]
        i = i+1

    return sum

print(sum([4, 6, 2, -7, 8]))