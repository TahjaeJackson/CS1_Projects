# Author: Tahjae Jackson
# Date: September 27, 2021
# Purpose: Question 16

"""
Define a function factorial_limit1 that takes a positive integer limit as parameter and prints the largest number whose
factorial is strictly less than the value limit. For example:
 If limit is 121, then your function should print 5.
If limit is 115, then your function should print 4.
If limit is 120, then your function should print 4 (strictly smaller than the limit).

"""
def factorial_limit1 (limit):
    factorial=1
    n=1
    while factorial < limit:
          n += 1
          factorial = n * factorial
          if factorial >= limit:
              n -= 1
    print(n)


factorial_limit1(115)
