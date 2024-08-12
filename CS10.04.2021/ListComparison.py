# Author: Tahjae Jackson
# Date: October 4, 2021
# Purpose: Lists demo


#Purpose: To find the maximum value in a list
#Parameter: A list of integers

def find_max(glist):
    max = glist[0]
    i = 1

    while i < len(glist):
        if max < glist[i]:
            max = glist[i]
        i = i + 1
    return max

mlist = [4, 6, 20, -7, 8]
print(find_max(mlist))


#Purpose: To find the maximum value index in a list
#Parameter: A list of integers


def find_max_i(glist):
    max_i = 0
    i = 1

    while i < len(glist):
        if glist[max_i] < glist[i]:
            max_i = i
        i = i + 1
    return max_i

mlist = [4, 6, 20, -7, 8]
print(find_max_i(mlist))

#Purpose: To create a list with all integers between m and n, including m and n
#Parameter: Two positive integers m and n, where m<n

def creat_mn_list(m,n):
    i = m
    rlist = []

    while i <= n:
        #rlist.append(i)
        rlist = rlist + [i]
        i = i + 1

    return rlist

print(creat_mn_list(3,7))


#Purpose: To create a string which is a list of characters
#Parameter: two integers

# you cannot append, remove or insert into a string even though it is a list of characters

def create_string(n):
    i = 0
    rstr = ""
    while i < n:
        rstr = rstr + "a" #This is how you append strings (concatenation)
        i = i + 1
    return rstr

print(create_string(6))


#Purpose: To check if a value is in a list
#Parameter: a list of integers and the search value

def find_value(jlist, x):
    y = x
    if y in jlist:  #behind te scenes, python is using a loop to check every element in the list to check if it is there
        print("yes")

rlist = [10, 5, 7, 1]
find_value(rlist,10)

#Purpose: To check if a string is a palindrome
#Parameter: the string


def is_palindrome(s):

    i = 0
    j = len(s) - 1

    while i < j:
        if s[i] != s[j]:
            return False #The function would stop here and not do anything else

        i = i + 1
        j = j - 1

    return True

print(is_palindrome("racecar"))








