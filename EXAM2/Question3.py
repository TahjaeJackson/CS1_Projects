# Author: Tahjae Jackson
# Date: October 14, 2021
# Purpose: question 3


# Question 3(10 points) : Define a function same_remainders that takes a list of positive
# integers glist and a positive integer k as parameters. Your function should return a list of
# lists where each innerlist contains numbers that give the same remainder when divided by k.
# The order of inner lists or the order in which numbers appear in the inner lists does not
# matter.
# For example:
# 1. if glist = [11, 5, 4, 9, 2, 7] and k = 3, then your function should return [[9], [4, 7], [5,
# 11, 2]].
# 2. if glist = [8, 4, 24, 12] and k = 4, then your function should return [[8, 12, 4, 24]].
# 3. if glist = [ ] and k is any positive integer, then your function should return [ ].
# 4. if glist = [7, 3, 18, 11, 8] and k = 6, then your function should return [[18], [7], [8], [3],
# [11]].


# Purpose: group a list of integers by the remainder value
# Parameter: a list of integers and a positive integer
# Return: a list of lists


def same_remainders(glist,k):
    list = []
    max_remainder = 0
    for x in glist:
        a = x % k
        if a > max_remainder:
            max_remainder = a
    for i in range (0,max_remainder+1):
        list.append([])

    for x in range(0,len(glist)):
        a = glist[x] % k
        list[a].append(glist[x])

    for i in range(len(list) - 1, -1, -1):
        if list[i] == []:
            del list[i]

    return list


glist = [7, 3, 18, 11, 8]
m = 6
print(same_remainders(glist,m))