# Name: Tahjae Jackson
# Date: October 22, 2021
# Purpose: Recursively compute the sum of the last k even numbers between 1 and n

def print_lastk(n,k):
    if n == 1:
        return

    if k == 0:
        return

    if n % 2 == 0:
        print(n)
        print_lastk(n-1,k-1)
    else:
        print_lastk(n-1, k)


print_lastk(10,2)