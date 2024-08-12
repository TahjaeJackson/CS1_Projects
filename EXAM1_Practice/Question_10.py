# Author: Tahjae Jackson
# Date: September 27, 2021
# Purpose: Question 10

"""


Define a function last_n_evens1 that takes two positive integers n and k as parameters. It should print the last k even
numbers between 1 and n. You can make the following assumptions:

There are at least k even numbers between 1 and n
n is an even number
"""

def last_n_evens1(n,k):
    count = 0
    num_even = 0
    while n>1 and count != k:
        if n%2 == 0:
            print (n)
            count +=1
        n -= 1

last_n_evens1(10,2)

