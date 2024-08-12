# Name: Tahjae Jackson
# Date: October 22, 2021
# Purpose: Demo to recursion

def func(n):
    if n <= 0:
        return
    func(n-1)
    print("test")

func(4)