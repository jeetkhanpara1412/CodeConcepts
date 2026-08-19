# Circular Queue in Python

# A Circular Queue is a type of queue where the last position is connected back to the first position. Instead of wasting empty spaces after deletions, it reuses them.

# Think of it like a clock.

# 🕐 After 12, it comes back to 1.

# Similarly, in a circular queue, after reaching the last index, it goes back to index 0.

class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    def enqueue(self, data):

        # Queue Full
        if (self.rear + 1) % self.size == self.front:
            print("Queue is Full")
            return

        # First element
        if self.front == -1:
            self.front = 0
            self.rear = 0

        else:
            self.rear = (self.rear + 1) % self.size

        self.queue[self.rear] = data
        print(data, "inserted")

    def dequeue(self):

        if self.front == -1:
            print("Queue is Empty")
            return

        data = self.queue[self.front]

        # Only one element
        if self.front == self.rear:
            self.front = -1
            self.rear = -1

        else:
            self.front = (self.front + 1) % self.size

        print(data, "deleted")

    def peek(self):

        if self.front == -1:
            print("Queue is Empty")
        else:
            print("Front element:", self.queue[self.front])

    def display(self):

        if self.front == -1:
            print("Queue is Empty")
            return

        print("Queue:", end=" ")

        i = self.front

        while True:
            print(self.queue[i], end=" ")

            if i == self.rear:
                break

            i = (i + 1) % self.size

        print()



cq = CircularQueue(5)

