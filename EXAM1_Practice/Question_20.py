# Author: Tahjae Jackson
# Date: September 27, 2021
# Purpose: Question 19

"""
 Define a function gcd that prints the greatest common divisor of two positive integers m and n that are passed as
 parameters to the function.

"""

def gcd(m,n):
    if m < n:
        max_divisor = m
    else:
        max_divisor = n

    found = False
    while max_divisor>1 and found == False:
        if m % max_divisor == 0 and n % max_divisor == 0:
            found = True
            break

        max_divisor -= 1

    print("The max divisor is:", max_divisor)

gcd(12,18)

