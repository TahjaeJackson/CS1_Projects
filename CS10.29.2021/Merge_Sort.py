# Name: Tahjae Jackson
# Date: October 29, 2021
# Purpose: Demo of the the merge sort

# FIRST DEMO OF THE MERGE LIST FUNCTION


# def merge(list1, list2):
#     i = 0
#     j = 0
#     res = []
#
#     while i < len(list1) and j < len(list2):
#         if list1[i] < list2[j]:
#             res.append(list1[i])
#             i = i + 1
#         else:
#             res.append(list2[j])
#             j = j + 1
#
#     while j < len(list2): #Numbers remaining in list 2 but list 1 is done
#         res.append(list2[j])
#         j = j + 1
#
#     while i < len(list1): #Numbers remaining in list 1 but list 2 is done
#         res.append(list1[i])
#         i = i + 1
#
#
#     return res


def merge(glist, p, q, r):
    glist1 = glist[p:q+1]
    glist2 = glist[q+1:r+1]

    i = 0
    j = 0
    k = p

    while i < len(glist1) and j < len(glist2):
        if glist1[i] < glist2[j]:
            glist[k] = glist1[i]
            i = i + 1
            k = k + 1

        else:
            glist[k] = glist2[j]
            j = j + 1
            k = k + 1

    while j < len(glist2):  # Numbers remaining in list 2 but list 1 is done

        glist[k] = glist2[j]
        j = j + 1
        k = k + 1

    while i < len(glist1): #Numbers remaining in list 1 but list 2 is done
        glist[k] = glist1[i]
        i = i + 1
        k = k + 1




def mergesort (glist, p = 0, r = None):
    if r == None:
        r = len(glist) - 1

    if p >= r:
        return

    mid = (p+r)//2
    mergesort(glist,p, mid)
    mergesort(glist, mid + 1, r)

    merge(glist, p, mid, r)


mlist = [8, -5, 23, 71, 24, 10, 13, 11]
mergesort(mlist)

print(mlist)
