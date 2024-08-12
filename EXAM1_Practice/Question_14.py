# Author: Tahjae Jackson
# Date: September 27, 2021
# Purpose: Question 14

"""
Define a function check_number_evens that takes two positive integers n and k as parameters. Your function prints
“at least k evens” if there are at least k even numbers between 1 and n, or prints “less than k evens” if there are
less than k even numbers between 1 and n.

"""

def check_number_evens(n,k):
    count_even = 0
    count = 1
    while count <= n:
        if n%2 == 0:
            count_even +=1
        count += 1

    if count_even >= k:
        print("at least k evens")
    else:
        print("less than k evens")



check_number_evens(100,5)
