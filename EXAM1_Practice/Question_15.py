# Author: Tahjae Jackson
# Date: September 27, 2021
# Purpose: Question 15

"""
Define a function last_n_evens3 that takes two positive integers n and k as parameters. Your function should do the following:
print the last k even numbers between 1 and n if there are k or more even numbers between 1 and n.
Otherwise it should print all the even numbers between 1 and n.

For example:
If k = 3 and n = 9, then your function should print:
8
6
4
If k = 2 and n = 8, then your function should print:
8
6
If k = 5 and n = 8, then your function should print:
8
6
4
2

"""
def last_n_evens3(n,k):
    count = 0
    while n>1 and count < k:
        if n%2 == 0:
            print(n)
            count += 1
        n -= 1

last_n_evens3(2,3)
