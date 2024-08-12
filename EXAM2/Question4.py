# Author: Tahjae Jackson
# Date: October 14, 2021
# Purpose: question 4

# Question 4(15 points) : Define a function no_common_chars that takes a list of strings
# slist and a string gstr as parameters. Your function should return a new list of strings
# (without modifying slist) that do not have any characters that are in gstr. The returned list
# can only contain strings in slist.
# The order of strings in the returned list does not matter. You are not allowed to use sort
# (built-in or your own) for this problem.
# For example:
# 1. if slist = [“pan”, “must”, “check”, “final”, “good”] and gstr = “pea”, then your function
# should return [“must”, “good”] as “must” and “good” are the only words in slist that do
# not have the characters “p”, “e” or “a”.
# 2. if slist = [“peterpan”, “must”, “check”, “final”, “good”, “eagle”] and gstr = “”, then your
# function should return [“peterpan”, “must”, “check”, “final”, “good”, “eagle”] as there
# are no letters in gstr.
# 3. if slist = [ ] and gstr = “peel”, then your function should return [ ] as there are no
# string in slist.
# 4. if slist = [“test”, “happen”, “common”, “keep”] and gstr = “xyzx”, then your function
# should return [“test”, “happen”, “common”, “keep”] as all strings is slist do not have
# the characters “x”, “y” and “z”.

# Purpose: To create a list of strings that do not have a certain letter
# Parameter: a list of string and a string
# Return: the list of unique strings


def no_common_chars(slist,gstr):
    uniquelist = []
    for x in slist:
        found = False
        for i in range(0, len(x)):
            for j in range(0, len(gstr)):
                if x[i] == gstr[j]:
                    found = True
                    break
            if found == True:
                break
        if found == False:
            uniquelist.append(x)

    return uniquelist

print(no_common_chars(["pan", "must", "check", "final", "good"],"pea"))


# Define a function more_that_one_string that takes a list of unique
# strings, glist, as a parameter. Your function should print all the characters that appear in
# more than two strings in the glist. For full credit each character should be printed only once.


def more_than_one_string(glist):
    common = []
    found = False
    for x in glist:
        for i in range(len(x)):
            for j in range(len(glist)):
                if (glist[j] != x):
                    for k in range(len(glist[j])):
                        if x[i] == glist[j][k]:
                            for n in common:
                                if n == x[i]:
                                    found = True
                                    break
                            if(found==False):
                                print(x[i])
                                common.append(x[i])
                                found = False

                            break

more_than_one_string(["pant", "must", "check", "final", "good"])

