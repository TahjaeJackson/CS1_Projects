# Author: Tahjae Jackson
# Date: October 6, 2021
# Purpose:


print("test", end= "") # end allows you to print something beside the string
print ("ing")
# testing will be printed because of the end

mlist = [6, 5, 23, 8, 3, 91]
nlist = mlist[1:4] #Coppies the values from index 1 to index 3
print(mlist, nlist)


s = "Dartmouth"
n_str = s[:] #copies everything from the first index to the last
# s[3:] copies everything from the third index to the last
# s[:3] copies everything from the first index to the SECONDD index
print(n_str)

"""RANGE FUNCTION"""

alist = [6, 5, 23, 8, 3, 91]
for i in range (0, len(mlist), 2): #[0,1,2,3,4,5]. The 2 means that it does every two values
    # for i in range (len(mdlist)-1, 0, -1) #This cant be used to go through all the numbers backwoe
    print(mlist[i], i)



"""FOR LOOP vs WHILE LOOP"""

#Both codes will print a range of values

def func(n):
    i = 0
    while i < n:
        print (i)
        i = i + 1

    print("End of while loop", n)

func(4)

def func_for(n):
    for i in range(0,n):
        print (i)

    print("End of for Lops", i)


func_for(4)


""" RECOMPUTATION """


i = 0
while i < 10:
    print(i)
    if i == 4:
        i = 6
    i = i+ 1


for i in range (0,10):
    print (1, end="")
    print (i)

"""DELETING AN ELEMENT FROM THE LIST"""

mlist = [8, 4, 6, 7, 8, 9]
i = 0
while i < len(mlist):
    if mlist[i] == 8:
        del mlist[i]
    else:
        i = i + 1

print(mlist)

for i in range (0, len(mlist)):
    if mlist[i] == 8:
        del mlist[i]

print(mlist)


for i in range (len(mlist)-1, -1, -1):  #this searches from the last element to the first element
    if mlist[i] == 9:
        del mlist[i]

print(mlist)

