# Name: Tahjae Jackson
# Date: November 3, 2021
# Purpose: The driver function for the city class

from city import *

fp = open("world_cities.txt","r")
fp2 = open("cities_out.txt", "w")


citylist = [] #The clear list that will store a list of city objects

# this loop goes through each line of the file, reads the data and makes a list of city objects from that file
for l in fp:
    data = l
    data = data.strip("\n")
    info = data.split(",")
    c = City(info[0], info[1], info[2], int(info[3]), float(info[4]), float(info[5]))
    citylist.append(c)


# this loop outputs the data from each city object into another file
for i in citylist:
    output = str(i)
    fp2.write(output)
    if i != citylist[len(citylist)-1]:
        fp2.write("\n")


fp.close()
fp2.close()