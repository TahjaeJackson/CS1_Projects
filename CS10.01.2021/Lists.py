# Author: Tahjae Jackson
# Date: October 1, 2021
# Purpose: Intro to lists in python


mlist = [10,4,7,12,45,50] #how to define a list
#anything apart of the list is called the element of the list

print(mlist) #prints he context of the list

print(len(mlist)) #prints the number of elements in the list

print(mlist[3]) #prints what is in index location 12. it starts at index location 0

print(mlist[len(mlist)-1]) #prints the last value in the list

#ADDING TO A LIST

mlist.append(3) # this adds 3 to then end of the list
print(mlist)

mlist.insert(1,30) #This puts 30 in index loaction 1
print(mlist)


#DELETE FROM A LIST

mlist.remove(12) #this deletes the number 12. If there are multiple 12's, it will delete the first one. If you want to delete all, you need a loop
print(mlist)

del mlist[0] #This deletes the value in index location 0
print(mlist)

print(mlist.index(7)) # This prints the index location that stores the value 7