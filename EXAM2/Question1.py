# Author: Tahjae Jackson
# Date: October 14, 2021
# Purpose: question 1


# Question 1(10 points) : Define a function even_odd that takes a list of positive integers
# glist as parameter and returns True if there are more even numbers than odd numbers in
# glist. Otherwise, it will return False. In this question, you cannot use while loops.
# For example:
# 1. if glist = [10, 5, 4, 90, 2, 7] then your function should return True.
# 2. if glist = [10, 5, 7, 9, 2, 7, 11] then your function should return False.
# 3. if glist = [ ] then your function should return False.
# 4. if glist = [2, 7, 4, 9] then your function should return False.

# Purpose: to check if there are more even than odd numbers
# Parameter: A list of integers
# Return: a boolean

def even_odd(glist):
    even_count = 0
    odd_count = 0
    for i in glist:
        if i % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    if even_count > odd_count:
        return True
    else:
        return False



glist = [2, 7, 4, 9]
print(even_odd(glist))
