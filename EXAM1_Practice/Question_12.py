# Author: Tahjae Jackson
# Date: September 27, 2021
# Purpose: Question 12

"""
Define a function last_n_evens2 that takes two positive integers n and k as parameters. It should print the last k even numbers between
 1 and n. You can make the following assumptions:

There are at least k even numbers between 1 and n

"""

def last_n_evens2 (n,k):
    count = 0
    while count<k and n != 1 :
        if n%2 == 0:
            print(n)
            count += 1
        n -= 1

last_n_evens2(100,10)