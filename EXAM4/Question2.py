# Name: Tahjae Jackson
# Date: November 11, 2021
# Purpose: Question 2 of the exam

# Question 2 (10 points): Define a recursive function that takes two positive integers n and p as parameters and prints
# all the multiples of p between 1 and n in increasing order. A number x is a multiple of p if x%p == 0. For example:

# 1. if n = 12 and p = 3, then your function should print
# 3
# 6
# 9
# 12
# 2. if n = 11 and p = 4, then your function should print:
# 4
# 8
# 3. if n = 11 and p = 11, then your function should print:
# 11
# 4. if n = 7 and p = 8, then your function should not print anything.

# Purpose: To create a recursive function that outputs the multiple of a certain number in a give range
# Parameters: Two integers n and p
# Return: None

def multiple(n, p):
    if n<p:
        return

    multiple(n - 1, p)
    if n%p == 0:
        print(n)



multiple(7, 8)
