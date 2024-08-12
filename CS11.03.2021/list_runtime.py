#runtime of lists

def func1(n):#runtime O(n)
    rlist = []
    for i in range(n):
        rlist.append(i)

    return

def func2 (n): #O(n^2)
    rlist = []
    i = n - 1
    while i>= 0:
        rlist.insert(0,1)
        i = i -1

    return rlist

def func3(glist, val): #0(n^2), n is len(glist)
    i = 0
    while i < len(glist):
        if glist[i] == val:
            del glist[i]

        i = i + 1

def func4(glist, val): #0(n2) n is len(glist)
    i = 0
    while i < len(glist):
        if glist[i] == val:
            return  i
        i = i + 1

    return None


# mlist[i] = O(1)
# mlist append(100) = O(1)
# mlist insert (0,5) = O(n) //Where n = len(mlist)
# mlist remove (5)  = O(n)
# mlist del (5)  = O(n)
# slist = mlist [1:] = O(n)
