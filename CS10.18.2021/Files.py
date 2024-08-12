# Author: Tahjae Jackson
# Date: October 18, 2021
# Purpose: Reading and Writing files

fp = open("DATA", "r") #This is how you open the file for reading
fp_w = open("newdata", "w")

for l in fp:
    print(l, end ="") #The end syntax allows it to print until the end of the document
fp.close()
fp = open("DATA", "r")
for j in fp:
    wlist = j.split()
    print( wlist)
    fp_w.write(wlist[0] + "\n") #this is how we write to the file and ensure there is a line in between each text.
    print(int(wlist[1]) + 1)

    #ou can only add string to the file

fp.close() #This is the syntax for closing the file. you hav eto cose the file else expect to see some error


fp_w.close()

