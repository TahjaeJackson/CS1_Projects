# Name: Tahjae Jackson
# Date: October 22, 2021
# Purpose: Demo to recursion

# def func(n):
#     if n <= 0:
#         return
#     func(n-1)
#     print(n)
#
# func(4)

# def func (a,b):
#     return a + b
#
# print(func(10, 20))
# mlist = [1, 5, 4]
# print(mlist)


# def func(n):
#     if n <= 0:
#         return
#
#     print(n)
#     func(n-1)
#
#
# func(4)


# this recursive function can be used to find the factorial of a number of the sum of all the consecutive numbers leading to that number. It all depends
# on the sign used in the return statement

def func(n):

    # BASECASE
    if n == 1:
        return 1


    # RECURSIVE FUNCTION
    x = func(n-1)
    return (x * n)


print(func(4))

# base case is the most trivial case where you know the answer for sure.



