# Author: Tahjae Jackson
# Date: October 14, 2021
# Purpose: question 5

# Question 5(5 points) : Define a function longest_equal_halves that takes a string gstr as
# a parameter. It should return the longest non-empty substring of gstr that has two equal
# halves. Here are few things to note:
# 1. A substring of a string gstr is anything that can be created using build-in slicing in
# Python gstr[m:n] where m <= n, 0 <= m <= len(gstr), and 0 <= n <= len(gstr).
# 2. A string has two equal halves when the string is even length and its first half is equal
# to the second half.
# For example:
# 1. if gstr = “xyztesttestabab”, then your function should return “testtest”.
# 2. if gstr = “xyzxyz”, then your function should return “xyzxyz”.
# 3. if gstr = “xyzabcd”, then your function should return “” (an empty string).
# 4. if gstr = “”, then your function should return “” (when you print an empty string you will
# only see a blank line in the output window).
# 5. if gstr = “xyxyabab”, then your function may return “xyxy” or “abab”.

# Purpose: To check if find the longest half in the string
# Parameter: a string
# Return: the longest half string

def longest_equal_halves(gstr):
    maxstring = ""
    maxlength = 0
    for x in range(0,len(gstr)):
        length = 0
        i = x
        j = len(gstr)
        half = ((j - i) + 1)//2
        end_indx = j
        while i != end_indx:
            j = half + 1
            first_equal = 0
            if half % 2 == 0:
                while i < half:
                    if gstr[i] == gstr[j]:
                        length = length + 1
                        i = i + 1
                        j = j + 1
                        first_equal += 1
                    else:
                        break

                    if first_equal == 1:
                        start = i-1
                        end = end_indx + 2
            end_indx -= 1
            half = ((end_indx - i) + 1)//2

        if length > maxlength:
            maxstring = gstr[start:end]

    return maxstring, start, end


gstr = "xyzxyz"
print(longest_equal_halves(gstr))
