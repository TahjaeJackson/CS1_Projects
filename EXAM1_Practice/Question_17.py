# Author: Tahjae Jackson
# Date: September 27, 2021
# Purpose: Question 17

"""
Define a function factorial_limit2 that takes a positive integer limit as parameter and prints the largest number whose factorial is less than or equal to limit. For example:
If limit is 121, then your function should print 5.
If limit is 115, then your function should print 4.
If limit is 120, then your function should print 5.


"""

def factorial_limit2 (limit):
    factorial=1
    n=1
    while factorial < limit:
          n += 1
          factorial = n * factorial
          if factorial > limit:
              n -= 1
    print(n)


factorial_limit2(120)