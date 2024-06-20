class Stack:

    def __init__(self, capacity):
        self. capacity = capacity
        self.stack = []

    def is_empty(self):
        if len(self.stack) == 0:
            return True

        else:
            return False

    def is_full(self):
        if len(self.stack) == self.capacity:
            return True

        else:
            return False

    def is_pop(self):
        if self.is_empty():
            print("The stack is empty")

        else:
            print(self.stack.pop())

    def push(self, value):
        if self.is_full():
            print("The stack is full")

        else:
            self.stack.append(value)

    def top(self):
        if self.is_empty():
            print("The stack is empty. Cannot take out any value")

        else:
            print(self.stack[-1])
