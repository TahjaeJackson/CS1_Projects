# Author: Tahjae Jackson
# Date: September 27, 2021
# Purpose: Question 9

"""

Define a function product_odd that takes two positive integers m and n as parameters and prints the product of all odd
numbers between m and n. You may assume m < n and m is odd.

"""

def product_odd(m,n):
    prod = 1
    while m<=n :
        if m % 2 == 1:
            prod = prod * m
        m = m + 1
    print(prod)

product_odd(1,5)

