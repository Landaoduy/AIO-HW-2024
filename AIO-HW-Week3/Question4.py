class Queue:

    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = []

    def is_empty(self):
        if len(self.queue) == 0:
            return True

        else:
            return False

    def is_full(self):
        if len(self.queue) == self.capacity:
            return True

        else:
            return False

    def de_queue(self):
        if self.is_empty():
            print('The stack is empty')

        else:
            print(self.queue.pop(0))

    def enqueue(self, value):
        if self.is_full():
            print('The queue is full')

        else:
            self.queue.append(value)

    def front(self):
        if self.is_empty():
            print('The stack is empty. Cannot take out the first value')

        else:
            print(self.queue[0])
