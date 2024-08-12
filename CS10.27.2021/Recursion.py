# Name: Tahjae Jackson
# Date: October 22, 2021
# Purpose: Is palindrome

def is_palindrome(s, i=0, j=None):

     if j == None:
        j = len(s) - 1

     if i >= j:
         return True

     if s[i] != s[j]:
         return False

     res = is_palindrome(s, i+1, j-1)
     return res


print(is_palindrome("  "))