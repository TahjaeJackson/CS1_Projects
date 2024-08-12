# Author: Tahjae Jackson
# Date: October 4, 2021
# Purpose: Lists Cont'd

mlist = [10, 4, 7, 2, -3]

"""nlist = mlist""" #this makes both lists point to the same thing
nlist = list(mlist) #create a copy of mlist
print(nlist, mlist)
nlist.append(100) # since nlist and mlist are using the same list, mlist will also append 100

print(nlist, mlist)