# Author: Tahjae Jackson
# Date: October 13, 2021
# Purpose:




# Define a function that takes a list of integers glist as input and returns a list containing those numbers in glist
# that are equal to the index at which they appear in glist. For example:
# If glist = [0, 13, 2, 33, 5, 67, 36, 7] then your function should return [0, 2, 7]
# If glist =[10, 20, 30, 40, 50] then your function should return [ ]

def equalindx_num(glist):
    equal = []
    for i in range(0,len(glist)):
        if glist[i] == i:
            equal.append(i)

    return equal

print(equalindx_num([0, 13, 2, 33, 5, 67, 36, 7]))



# 2. Define a function that takes a list of integers glist that is sorted (in increasing order) and an integer n as
# parameters and inserts n into glist in such a way that glist remains sorted.

def orderlist(glist,n):
    sorted_list = []
    for i in range(0,len(glist)):
        sorted_list.append(glist[i])
        if n>glist[i] and n<glist[i+1]:
            sorted_list.append(n)
    return sorted_list

print(orderlist([1, 2, 3, 5, 6, 7, 8], 4))



# 3. Define a function that takes a list of integers glist as parameter and returns True if the list is either sorted in
# decreasing or increasing order. Otherwise it returns False. [Extra practice: If you used two loops, think how you can solve
# this problem with only one loop.]

def order_list_check(glist):
    descending = 0
    ascending = 0
    for i in range(0,len(glist)-1):
         if glist[i] <= glist[i+1]:
             ascending += 1
         if glist[i] >= glist [i+1]:
             descending +=1
         if descending == len(glist)-1 or ascending == len(glist)-1:
             return True

    return False

print(order_list_check([5, 4, 3, 2, 2]))



# 4. Define a function that takes a list of strings slist as parameter and checks if at least one of the strings is a
# palindrome. It should return True or False. [Hint: You can use the function is_palindrome that takes a string as parameter
# and return True or False discussed in class.]
#
def is_palindrome(slist):
    palindrome_count = 0
    for s in slist:
        i = 0
        j = len(s) - 1
        palindrome_test = True
        while i < j:
            if s[i] != s[j]:
                palindrome_test = False #The function would stop here and not do anything else
                break
            i = i + 1
            j = j - 1

        if palindrome_test == True:
            palindrome_count += 1

    if palindrome_count >= 1:
        return True
    else:
        return False


print(is_palindrome(["bo", "rac", "chad"]))

#
# 5. Define a function that takes two lists glist1 and glist2 as parameters and returns True if they are the reverse of each
# other, otherwise returns False. For simplicity you can assume that the given lists contain only integers.

def list_compare(glist1, glist2):
    if len(glist1) == len(glist2):
        j = len(glist2) -1
        for i in range(0, len(glist1)-1):
            if glist1[i] != glist2[j]:
                return False
            j = j - 1
    else:
        return False

    return True

print(list_compare([1,2,3,4],[4,2,3,1]))



# 6. Define a function that takes two lists gl1 and gl2 of integers as parameters. Assume the following:
# a. Each list has unique numbers. (Note: A number can occur in both lists)
# b. Both lists are sorted in increasing order

# Your function should return a list that is sorted in increasing order and contains the numbers in both the lists. But
# if a number appears in both the lists then it should appear only once in the result list.
# For example:
# If gl1 = [10, 20, 30, 40] and gl2 = [11, 20, 44, 56, 60] then the result list will be [10, 11, 20, 30, 40, 44, 56, 60]
# If gl1 = [ ] and gl2 = [11, 20, 44] then the result list will be [11, 20, 44]

def list_add_and_order(gl1, gl2):
    biglist = []
    if len(gl1)-1 > len(gl2)-1:
        maxlength = len(gl1) -1
        maxlist = gl1
        minlength = len(gl2)-1
        minlist = gl2

    if len(gl2)-1>len(gl1)-1:
        maxlength = len(gl2)-1
        maxlist = gl2
        minlength = len(gl1)-1
        minlist = gl1

    if len(gl2) -1 == len(gl1) -1:
        x = len(gl2) - 1
        maxlength = len(gl2) - 1
        maxlist = gl2
        minlength = len(gl1) - 1
        minlist = gl1
        if gl1[x] > gl2[x]:
            maxlength = len(gl1) - 1
            maxlist = gl1
            minlength = len(gl2) - 1
            minlist = gl2
    j = 0
    i = 0
    while i <= minlength:
        if minlist[i]<maxlist[j]:
            biglist.append(minlist[i])
            i = i + 1
        elif maxlist[j]<minlist[i]:
            biglist.append(maxlist[j])
            j = j + 1
        else:
            biglist.append(minlist[i])
            i = i + 1
            j = j + 1

    for x in range(j,maxlength+1):
        biglist.append(maxlist[x])

    return biglist
gla = [10, 20, 30, 40,60]
glb = [11, 20, 44, 56, 60]
print(list_add_and_order(gla,glb))






# 7. Define a function that takes a string str as a parameter and returns a string that is the reverse of the given string.


def string_reverse(str):
    string = ""
    j = 0
    for i in range(len(str)-1,-1,-1):
        string = string + str[i]

    return string

print(string_reverse("james"))
