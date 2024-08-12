# Author: Tahjae Jackson
# Date: October 13, 2021
# Purpose:


# 1. Define a function that takes a list of lists glol as parameter.  You may assume that each inner list inside glol is
# a list of integers. For example: [[1, 2], [10, 20], [30, 10], [-4, -5]].
# Your function returns True if at least one list inside glol is sorted in increasing order and at least one
# list is sorted in decreasing order, else it returns False.

def is_ordered(glol):
    descending = 0
    ascending = 0
    d_count = 0
    a_count = 0
    for x in glol:
        for i in range(0, len(x) - 1):
            if x[i] <= x[i + 1]:
                ascending += 1
            if x[i] >= x[i + 1]:
                descending += 1
            if descending == len(x) - 1:
                d_count += 1
            if ascending == len(x) - 1:
                a_count += 1

    if a_count >= 1 and d_count>=1:
        return True
    else:
        return False

print(is_ordered([[1, 2, 5, 4], [10, 20, 9], [30, 10, 9], [-4, -5, -4]]))

# Define a function that takes two strings s1 and s2 as parameters and checks if they have the same set of characters
# that occur with the same frequency (you are checking if s1 and s2 are anagrams). For example:
# If s1 = “dirtyroom” and s2 = “dormitory” then it should  return True
# If s1 = “dirty room” and s2 = “dormitory” then it should return False (space is counted as a character)
# If s1 = “too” and s2 = “to” then it should return False

def anagram(s1, s2):
    if len(s1) == len(s2):
        for i in s1:
            letter_count1= 0
            letter_count2 = 0
            for x in s1:
                if i == x:
                    letter_count1 = letter_count1 + 1

            for j in s2:
                if j == i:
                    letter_count2 += 1

            if letter_count1 != letter_count2:
                return False
    else:
        return False

    return True

print(anagram("dirtyroom", "dormitory"))


# Define a function that takes two strings s1 and s2 as parameters and checks if they have the same set of characters
# but possibly with a different frequency. For example:
# If s1 = “dirtyroom” and s2 = “dormitory” then it should  return True
# If s1 = “dirty room” and s2 = “dormitory” then it should return False (space is counted as a character)
# If s1 = “too” and s2 = “to” then it should return True


def anagram2(s1, s2):

    for i in s1:
        found = False
        for j in s2:
            if j == i:
                found = True
                break

        if found == False:
            return False

    return True

print(anagram2("two", "toww"))

# Define a function that takes a list of lists as a parameter such that each inner list is a list of integers. The function
# should return a list containing all integers that occur only in one of the inner lists. For example:
#  If the given list is [[10, 20, 30, 12], [10, 40, 30], [40, -10,  60], [20, 40]] then the function should return [12, -10,  60]
# If the given list is [[10, 20, 12, 30], [10, 40, 30, 60], [40, -10, 12, 60], [-10, 20, 40]] then the function should return []
# You can assume that all numbers within any inner list are unique. But the same number can appear in multiple inner lists.

def only_once(glol):
    uniquelist=[]
    for x in range(0, len(glol)):
        for i in range(0,len(glol[x])):
            found = False
            for j in range(x+1, len(glol)):
                for indx in range(0,len(glol[j])):
                    if glol[x][i] == glol[j][indx]:
                       found = True
                       break
                if found == True:
                    break
            if x != 0:
                for j in range(0,x):
                    for indx in range(0, len(glol[j])):
                        if glol[x][i] == glol[j][indx]:
                            found = True
                            break


            if found == False:
                uniquelist.append(glol[x][i])

    return uniquelist

print(only_once([[10, 20, 30, 12], [10, 40, 30], [40, -10,  60], [20, 40]]))

# Define a function that takes a list of positive integers (greater than 0) as a parameter and returns a list of lists.
# Your  function should group the numbers based on the number of digits they have. Each inner list in the returned list
# represents one such group. Also, in the returned list the inner lists should be sorted in order of length of the numbers
# they contain. You are not allowed to sort the given list.
# For example:
#  If the given list is [9, 67, 200, 456, 20023, 3, 10, 999] then it should return [[9, 3], [67, 10], [200, 456, 999], [20023]]
# If the given list is [] then it should return []

def digits(integers):
    if len(integers) > 0:
        max = integers[0]
        x = 1
        while x < len(integers):
            if max < integers[x]:
                max = integers[x]
            x = x + 1
        maxnum = str(max)
        maxdigit = len(maxnum)
        intlist = []
        for j in range (0, maxdigit):
            intlist.append([])
        for i in integers:
            for z in range(0, maxdigit+1):
                if  i < 10**z and i>=10**(z-1):
                    intlist[z-1].append(i)
                    break

        for i in range(len(intlist) - 1, -1, -1):
            if intlist[i] == []:
                del intlist[i]


    else:
        intlist = []

    return intlist

print(digits([9, 67, 200, 456, 20023, 3, 10, 999]))


# 6. Define a function that takes a list of positive integers glist as parameter and returns a list of lists.
# Assume len(glist) > 0. The returned list of lists should satisfy the following conditions:
# 1. Each inner list in the returned list contains numbers from glist that can form a sequence of consecutive numbers.
# 2. Only longest sequence/sequences should be added to the returned list (there can be multiple longest sequences, see example 2 below)
# 3. The order of numbers in inner lists does not matter.
# 4. The order of inner lists in the returned list does not matter.
# 5. Assume the list has unique numbers.
#
# For example:
# If glist = [100, 8, 9, 3, 99, 2, 101], then your function should return [[99, 100, 101]].
# If glist = [ 8, 12,  9, 3, 99, 2, 101], then your function should return [[2, 3], [9, 8]].
# If glist = [ 8, 2, 10], then your function should return [[8], [2], [10]] as the longest consecutive sequences are all
# of length 1 (i.e. the individual elements).

def final(glol):

