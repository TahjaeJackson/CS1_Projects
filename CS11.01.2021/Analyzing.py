# Author: Tahjae Jackson
# Date: November 1, 2021
# Purpose:

def func(n): #O(n)
    i = 0
    while i < n-1:
        i = i + 1

def func1(n): #O(n)
    i = 4
    while i < n:
        i = i + 1

def func2(n): #O(n)
    i = 1
    while i < n:
        i = i + 2

def func3(n): #O(n^2)
    i = 1
    while i < n:
        j = 2
        while j < n-1:
            j = j + 1

        i = i + 1

def func4(n): #O(n)
    i = 1
    while i < n:
        i = i + 1

    j = 1
    while j < n:
        j = j + 1


def func5(n): #O(n^2)
    for i in range(n):
        for j in range(n):
            print(i, j)


def func6(n): #O(1)
    while i < 10:
        i = i + 1


def func7(n): #0(log(n))
    i = 1
    while i < n:
        i = i * 2


def func8(n): #0(log(n))
    i = n
    while i > 1:
        i = i // 2


def func9(n): #0(nlog(n))
    i = n
    while i > 1:
        j = 0
        while j < n:
            j = j + 1

        i = i//2


def func10(n): #0(n)
    i = 0
    while i < 3:
        j = 0
        while j < n:
            j = j + 1
        i = i + 1


def func11(n): #0(n)
    i = 0
    while i < n:
        j = 0
        while j < n:
            j = j + 1
            i = i + 1
        i = i + 1


def func12(n): #0(n^2)
    i = 0
    j = 0
    while j < n:
        i = i + 1
        if i == n:
            i = 0
            j = j + 1
