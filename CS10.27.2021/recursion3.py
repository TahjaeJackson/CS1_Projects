# Name: Tahjae Jackson
# Date: October 22, 2021
# Purpose: Recursively computing fibanacci and why it is a bad idea


def fib(n):
    if n == 1 or n == 2:
        return 1

    n2 = fib(n-2)
    n1 = fib(n-1)

    return n2 + n1

print(fib(7))

# for this case, using recursion is not efficient because a particular case may be frequently repeated

def fib(n, list=[]):
    if n == 1 or n == 2:
        return 1

    if list[n-2] == None:
        n2 = fib(n-2)
        list[n-2].append(n2)
    else:
        n2 = list[n-2]

    if list[n-1] == None:
        n1 = fib(n-1)
        list[n-1].append(n1)
    else:
        n1 = list[n-1]


    return n2 + n1

print(fib(7))
