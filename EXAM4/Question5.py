# Name: Tahjae Jackson
# Date: November 11, 2021
# Purpose: Question 5 of the exam

#5 points
#In each of the following recursive functions there is an error
#that either cause PyCharm to exit with error message or gives the
#wrong output. Expected output is described in the purpose statement
#for each of the functions.
#You are allowed to change only one line of code in the body of each
#function to fix the error.
#
# # 1 point
# # Parameter: n and p are positive integers
# # Purpose:Computes n to the power p
# def func1(n, p):
#     if p == 0:
#         return 1
#     r = func1(n, p-1)
#     return r * n
#
# print(func1(10, 4)) #Correct answer in this case will be 10000
# print(func1(2, 3)) #Correct answer in this case will 8
# print(func1(7, 0)) #Correct answer in this case will 1
#
# #1 point
# #Parameter: glist is a list of positive integers and k is a positive integer
# #Purpose: Returns True if all numbers in glist are
# #greater than k.
#
# def all_greater_than_k(glist, k):
#     if len(glist) == 0:
#         return True
#
#     if glist[0] <= k:
#         return False
#
#     return all_greater_than_k(glist[1:], k)
#
# print(all_greater_than_k([10, 45, 12], 5)) #Correct answer in this case is True
# print(all_greater_than_k([100, 10, 45, 12], 11)) #Correct answer in this case is False
#
# #1 point
# #Parameter: s is string
# #Purpose: Returns the number of times character "a" appears in the
# #string s.
# def count_a(s, i=0):
#     if i == len(s):
#         return 0
#     res = count_a(s, i+1)
#     if s[i] == "a":
#         return res + 1
#     else:
#         return res
# print(count_a("banana")) #Correct answer in this case is 3
# print(count_a("test")) #Correct answer in this case is 0
#
# # 2 points
# # Parameter: glist is a list of unique integers and val is a integer
# # Purpose: To return the index at which val appear in glist, if it
# # does not appear in glist function returns None.
#
# def find_val(glist, val, i=0, j=None):
#     if j == None:
#         j = len(glist)-1
#
#     if i > j:
#         return None
#
#     mid = (i + j) // 2
#     if glist[mid] == val:
#         return mid
#
#     if i == j:
#         return None
#
#     x = find_val(glist, val, i, mid-1)
#     y = find_val(glist, val, mid+1, j)
#
#     if x != None:
#         return x
#
#     if y != None:
#         return y
#
# print(find_val([10, 14, 62, 23], 62)) #Correct answer in this case is 2
# print(find_val([10, 14, 62, 23], 23)) #Correct answer in this case is 3


# def is_suffix(str1, str2,j=None, i = None):
#     if i == None and (len(str2) > 0):
#         i = len(str2) - 1
#     else:
#         return False
#
#     if j == None and (len(str1) > 0):
#         j = len(str1) - 1
#     else:
#         return True
#
#     if len(str2) < len(str1):
#         return False
#
#     if j == 0:
#         return True
#
#     if str1[j] == str2[i]:
#         return is_suffix(str1,str2, j-1, i -1)
#     else:
#         return False
#
#
# print(is_suffix("washer", "dishwasher"))
# print(is_suffix("", "test"))
# print(is_suffix("test", ""))


def product_odd(m,n,prod=1):


    if m > n:
        return prod

    if m % 2 != 0:
        prod = prod * m



    return product_odd(m+1,n,prod)


    # return prod

print(product_odd(2,5))
