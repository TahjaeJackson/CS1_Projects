# Name: Tahjae Jackson
# Date: November 8, 2021
# Purpose: To sort a given file based on a certain criteria and then to print that output to separate files

from quicksort import *
from city import *

# opening of all four files to be used

fp = open("world_cities.txt","r")
fp1 = open("cities_alpha.txt", "w")
fp2 = open("cities_population.txt", "w")
fp3 = open("cities_latitude.txt", "w")




citylist = [] #The clear list that will store a list of city objects

# For loop that appends a list of city objects read from the main file
for l in fp:
    data = l
    data = data.strip("\n")
    info = data.split(",")
    c = City(info[0], info[1], info[2], int(info[3]), float(info[4]), float(info[5]))
    citylist.append(c)

# Purpose: To compare the population of two city objects
# Parameter: Two city objects
# Return: A boolean value

def compare_ints(city1, city2):
    return city1.population <= city2.population

# Purpose: To compare the names of two city objects and determine which one would come first alphabetically
# Parameter: Two city objects
# Return: A boolean value

def compare_strings(city1, city2):
    return city1.name.lower() >= city2.name.lower()

# Purpose: To compare the latitude of two city objects
# Parameter: Two city objects
# Return: A boolean value

def compare_float(city1, city2):
    return city1.latitude >= city2.latitude


# Sort and for loop used to populate a file with city information arranged in alphabetical order by name
sort(citylist, compare_strings)
for i in citylist:
    output = str(i)
    fp1.write(output)
    if i != citylist[len(citylist)-1]:
        fp1.write("\n")

# Sort and for loop used to populate a file with city information arranged in descending order by population
sort(citylist, compare_ints)
for i in citylist:
    output = str(i)
    fp2.write(output)
    if i != citylist[len(citylist)-1]:
        fp2.write("\n")

# Sort and for loop used to populate a file with city information sorted by latitude, from south to north.
sort(citylist, compare_float)
for i in citylist:
    output = str(i)
    fp3.write(output)
    if i != citylist[len(citylist)-1]:
        fp3.write("\n")




fp.close()
fp1.close()
fp2.close()
fp3.close()

