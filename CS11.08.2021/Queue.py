 # Name: Tahjae Jackson
# Date: November 6, 2021
# Purpose: stack class

class Stack:
    def __init__(self):
        self.data = []

    def push(self, val):
        self.data.append(val)

    def pop(self):
        if len(self.data)> 0:
