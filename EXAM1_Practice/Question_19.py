# Author: Tahjae Jackson
# Date: September 27, 2021
# Purpose: Question 19

"""
 Define a function is_factorial, that takes a positive integer n as parameter and prints True if it is a factorial of a
 positive integer. Otherwise it prints False. [Note: Your program should print False or True only once.

"""

def is_factorial(n):
    count = 1
    factorial = 1
    ans = False
    while count <= n and ans == False:
        factorial = count * factorial
        if factorial == n:
            ans = True
        count += 1
    print(ans)

is_factorial(2)