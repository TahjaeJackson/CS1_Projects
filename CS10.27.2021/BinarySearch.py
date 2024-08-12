# Name: Tahjae Jackson
# Date: October 22, 2021
# Purpose: To create a binary search function recursively

def binary_search(glist, val):
    start = 0
    end = len(glist) - 1

    while start <= end:
        mid = (start + end)//2

        if glist[mid] < val:
            start = mid + 1
        elif glist[mid] > val:
            end = end - 1
        else:
            return mid


        return None

glist = [2, 7, 11, 22, 37, 89, 92, 105]

print(binary_search(glist, 37))
