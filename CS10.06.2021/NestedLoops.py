# Author: Tahjae Jackson
# Date: October 6, 2021
# Purpose: To demonstrate how nested loops may be implemented

i = 0
while i < 5:
    j = 0
    while j < 3:
        print (i,j)
        j = j + 1

    i = i + 1

#     PUurpose: To check how many 'a' s are in a string
# Parameter:  A list of strings
def func(slist):
    i = 0
    while i < len(slist):
        j = 0
        count_a = 0
        in_s = slist[i]
        while j < len(in_s):
            if in_s[j] == "a":
                count_a = count_a + 1
            j = j + 1
        print(in_s, count_a)
        i = i + 1

func(["amelie", "vasanta", "daniel", "samuel", "alejo"])

#You can have a list within alist


