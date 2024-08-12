# Name: Tahjae Jackson
# Date: November 11, 2021
# Purpose: Question 3 of the exam

# Question 3 (10 points): Define a recursive function that takes a list of positive integers glist as a parameter and returns
# a new list that contains all the numbers in glist that appear at odd indices. The order of numbers in the returned list
# does not matter.
#
# For example:
# 1. if glist = [10, 3, 6, 8, 9] then your function should return [3, 8] or [8, 3].
# 2. if glist = [5, 6, 4, 3, 2, 7 ] then your function should return [6, 3, 7] or [7, 3, 6].
# 3. if glist = [10] then your function should return [ ].
# 4. if glist = [ ] then your function should return [ ].

# Purpose: Output a list of the values in a list that are in an odd index location
# Parameters: A list of values and and integer , i, that stores the index location
# Return: A list of values in odd number indices

def odd_index(glist, i = 0):
    if i == len(glist):
        return []
    else:
        new_list = odd_index(glist, i+1)

    if i % 2 == 1:
        new_list.insert(0,glist[i])

    return new_list



glist = [5, 6, 4, 3, 2, 7 ]
print(odd_index(glist))


