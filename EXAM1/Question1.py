# Author: Tahjae Jackson
# Date: September 30, 2021
# Purpose: Question 1

"""
 Question 1(10 points) : Define a function product_m_n that takes two positive
integers m and n as parameters and prints the product of all integers between m and
n, including n but not m in the product. You may assume m < n. For example:
1. if m = 2 and n = 5 then your function should print 60.
2. if m = 3 and n = 4 then your function should print 4.

"""

#Purpose: Takes two positive integers and outputs the product of the integers within that range
#Parameter: Two integers m and n

def product_m_n(m,n):
    prod = 1
    while m < n:
        m += 1
        prod = prod * m
    print("The product of the integers within that range is: ", prod)


product_m_n(3,4)