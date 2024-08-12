# Name: Tahjae Jackson
# Date: November 11, 2021
# Purpose: Question 4 of the exam
#
# Question 4 (5 points): Define a recursive function that takes two strings s1 and s2 and a non-negative integer k as
# parameters and returns True if there are exactly k indices where characters in s1 match the characters in s2,
# otherwise it returns False.
# For example:
# 1. if s1 = “mango” and s2 = “banana” and k = 2, then your function returns True as the characters in s1 and s2 match at indices 1 and 2.

# 2. if s1 = “mango” and s2 = “mentor” and k = 3, then your function returns True as the characters in s1 and s2 match at indices 0, 2 and 4.

# 3. if s1 = “mango” and s2 = “mentor” and k = 4, then your function returns False as the characters in s1 and s2 match at indices 0, 2 and 4.

# 4. if s1 = “testing” and s2 = “text” and k = 2, then your function returns False as the characters in s1 and s2 match at indices 0, 1 and 3.

# 5. if s1 = “testing” and s2 = “” and k = 0, then your function returns True as the characters in s1 and s2 do not match at any index.

# 6. if s1 = “” and s2 = “testing” and k = 2, then your function returns False as the characters in s1 and s2 do not match at any index.

# 7. if s1 = “test” and s2 = “abababab” and k = 2, then your function returns False as the characters in s1 and s2 do not match at any index.

# 8. if s1 = “test” and s2 = “abababab” and k = 0, then your function returns True as the characters in s1 and s2 do not match at any index.

# 9. if s1 = “” and s2 = “” and k = 0, then your function returns True as the characters in s1 and s2 do not match at any index.

# Purpose: To determine if the two strings have a certain number of characters in the same e=index locations
# Parameters: Two strings, the number of common letters, the count and two integers to store the index locations of each string
# Return: A boolean value stating if the strings do have a certain number of characters in the same e=index locations

def equal_string(s1, s2, k, count= 0, i=0, j =0):
    if count > k:
        return False
    if (i >= len(s1)) or (j >= len(s2)):
        if count == k:
            return True
        else:
            return False

    if s1[i] == s2[j]:
        return equal_string(s1,s2,k,count+1, i+1, j+1)
    else:
        return equal_string(s1, s2,k, count, i+1, j+1)




s2 = ""
s1 = ""
k = 0
print(equal_string(s1,s2,k))



