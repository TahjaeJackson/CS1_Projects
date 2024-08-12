# Author: Tahjae Jackson
# Date: October 12, 2021
# Purpose:


"""
Define a function that takes positive integer n and returns a  list of all multiples of 3 or 5 between 1 and n (including n, if it meets conditions
"""

def multiple3_5(n):
    multiplelist = []
    for i in range (1, n+1):
        if (i % 3 == 0) or (i % 5 == 0):
            multiplelist.append(i)

    return multiplelist


print(multiple3_5(20))


"""
Define a function that takes a list of postive integers as a parameter, and returns True if all integers are prime; false if otherwise
"""

def prime(list):
    for i in list:
        factor_count = 0
        for j in range (1,i+1):
            if (i % j == 0):
                factor_count += 1
            if factor_count > 2 :
                return False

    return True

mlist = [1,2,3,4,5,7,11]
print(prime(mlist))
