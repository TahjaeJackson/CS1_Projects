# NAME: Tahjae Jackson
# DATE: October 20, 2021
# PURPOSE: Understanding the act of calling of functions (Intro to Recursion)

#Run in python tutor to see the steps followed once this code is run

# Stack overflow is an infinitely run function

def funcA(n):
    if n > 10:
        print("FuncA: ", n)
        return n
    else:
        x = funcB(n+2)
        return x

def funcB(n):
    if n > 10:
        print("FuncB: ", n)
        return n
    else:
        x = funcC(n+1)
        return x

def funcC(n):
    if n>10:
        print("FuncC: ", n)
        return n
    else:
        x = funcB(n+3)
        return x

print(funcA(5))