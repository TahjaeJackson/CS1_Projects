


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, x):
        self.items.append(x)

    def dequeue(self):
        return self.items.pop(0)

    def empty(self):
        return self.items == []

    def __str__(self):
        return str(list(self.items))