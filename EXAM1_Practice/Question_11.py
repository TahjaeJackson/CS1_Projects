# Author: Tahjae Jackson
# Date: September 27, 2021
# Purpose: Question 11

"""
Define a function product_odd that takes two positive integers m and n as parameters and prints the product of all odd
numbers between m and n. You may assume m < n. Parameters m and n can be even or odd.
"""

def product_odd(m,n):
    while m<=n:
        if m%2 == 1:
            print(m)
        m += 1

product_odd(1,10)