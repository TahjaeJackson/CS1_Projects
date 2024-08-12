# Name: Tahjae Jackson
# Date: November 1, 2021
# Purpose: Towers of Hanoi




def toh(source, dest, spare, n):
    if n == 0:
        return

    toh(source, spare, dest, n-1)
    print("Move disk", n, "from peg", source, "to", dest)
    toh(spare, dest, source, n-1)


toh("A", "B", "C", 4)