# Author: Tahjae Jackson
# Date: September 30, 2021
# Purpose: Question 3

"""
 Question 3 (15 points): Define a function count_factorials that takes three positive
integers m, n and k as parameters. Your function should print True if there are exactly k
integers between m and n (including m and n) that are equal to factorial of some positive
integer. Otherwise it should print False.
For example:
1. if m = 2, n = 10 and k = 2 then your function should print True as there are exactly k
integers (2 and 6) between m and n that are equal to factorial of some positive
integer.
2. if m = 24, n = 24 and k = 1 then your function should print True as 24 is equal to
factorial of 4.
3. if m = 5, n = 24 and k = 3 then your function should print False as there are fewer
than k integers (6 and 24) between m and n that are equal to factorial of some
positive integer.
4. if m = 120, n = 5 and k = 2 then your function should print False as there are more
than k integers (6, 24, 120) between m and n that are equal to factorial of some
positive integer.
5. if m = 6, n = 24 and k = 3 then your function should print False as there are fewer
than k integers (6 and 24) between m and n that are equal to factorial of some
positive integer.
"""

#Purpose: To find out if there are exactly k integers in a given range that are fatorials of a positive integer
#Parameter: Three positive integers (m,n and k)

def count_factorials(m,n,k):
    factorial_count = 0
    while m <= n:
        count = 1
        factorial = 1
        while count <= m:
            factorial = count * factorial
            if factorial == m:
                factorial_count += 1
            count += 1
        m += 1

    if factorial_count == k:
        print(True)
    else:
        print(False)

count_factorials(2,10,2)


