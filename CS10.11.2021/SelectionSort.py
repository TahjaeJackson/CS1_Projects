# Author: Tahjae Jackson
# Date: October 11, 2021
# Purpose: To create function that does selection sort




# Purpose: Find the index of the minimum value in the ist between i and end of the list

def find_min_indx(glist, i):
    min_i = i
    indx = i

    while indx < len(glist):
        if glist[indx] < glist[min_i]:
            min_i = indx
        indx = indx + 1

    return min_i



# Purpose: To arrange a list in ascending order
# Parameter: A list of integers
# Return: TBD (You do not have to return the list. It changes the given list for you)

def selectionsort(glist):

    for i in range(len(glist)):
        mi = find_min_indx(glist, i)

        temp = glist[mi]
        glist[mi] = glist[i]
        glist[i] = temp



def bubblesort(mlist):

    for j in range(0, len(mlist)-1):
        for i in range(0, len(mlist)-1):
            if mlist[i] > mlist [i+1]:
                temp = mlist[i]
                mlist[i] = mlist[i+1]
                mlist[i+1] = temp




mlist = [8, -4, 8, -9, -4, 4, 5, 23, 18, 6]
bubblesort(mlist)
selectionsort(mlist)
print(mlist)

# Built in python functions to sort
"""
nlist = mlist.sort() #This sorts a given list in ascending order and copies it in another list

nlist = mlist.sort(reverse = True)  #This sorts a given list in descending order and copies it in another list

nlist = sorted(mlist, reverse = True) #This is another way of sorting a given list in ascending order and copies it in another list
"""