# Author: Tahjae Jackson
# Date: October 14, 2021
# Purpose: question 2

# Question 2(10 points) : Define a function string_slicing that takes a string gstr, and two
# non-negative integers m and n as parameters. Your function should return a new string with
# the characters in gstr from index m to n (including m but not n) in the order they appear in
# gstr. In other words, the string returned by your function will be equal to gstr[m:n]. Assume
# m <= n; m <= len(gstr)-1; and n <= len(gstr).
# In this question you not allowed to use:
# ● the built-in list/string slicing in Python
# ● while loops
# For example:
# 1. if gstr = “testing”, m = 1 and n = 5, then your function should return “esti”.
# 2. if gstr = “dartmouth”, m = 0 and n = 4, then your function should return “dart”.
# 3. if gstr = “testing”, m = 2 and n = 7, then your function should return “sting”.
# 4. if gstr = “dartmouth”, m = 3 and n = 3, then your function should return “” (when you
# print an empty string you will only see a blank line in the output window).

# Purpose: To create a function to slice a string
# Parameter: a string, and two positive integers
# Return: the sliced string

def string_slicing(gstr, m, n):

    newstring = ""
    for i in range(m,n):
        newstring = newstring + gstr[i]

    return newstring

print(string_slicing("dartmouth",3,3))