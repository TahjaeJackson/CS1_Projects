# Author: Tahjae Jackson
# Date: September 27, 2021
# Purpose: Question 18

"""
Define a function lcm that takes two positive integer parameters m and n, and prints the smallest number that is divisible
by both m and n. For example:
if m = 2 and n = 3 then it should print 6.
If m = 8 and n = 4 it should print 8.
 [Hint: lcm of two numbers will always be greater than both the numbers, so think where to start the loop]


"""

def lcm (m,n):
    prod = m * n
    found = False
    if m < n:
        count = m
    else:
        count = n
    while count <= prod and found == False:
        if count%m == 0 and count%n == 0:
            found = True
        else:
            count += 1
    print(count)


lcm(2,3)