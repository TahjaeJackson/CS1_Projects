# Name: Tahjae Jackson
# Date: October 17, 2021
# Purpose: Driver for the counter class

from Counter_Class import *

counter1 = Counter(60, 59, 4)
counter2 = Counter(12, 11, 4)
fp = open("CounterOutput","w")


# Purpose: To output the counter
# Parameters: The variable that stores the memore address
# Return: There is none

def counter_output(counter,max):
    for i in range (0, max):
        print(str(counter))
        fp.write(str(counter)+"\n")
        if counter.tick():
            break



counter_output(counter1, 60) #This prints the first case of the counter
print("*************************")
fp.write("\n\n" + "*************************" + "\n\n")
counter_output(counter2,12)  #This prints the second case of the counter
fp.close()


