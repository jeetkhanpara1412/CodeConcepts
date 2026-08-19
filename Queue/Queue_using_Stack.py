# Queue using Stack in Python

# A Queue follows the FIFO (First In, First Out) principle.

# First element inserted → First element removed
# Like people standing in a line.

class QueueUsingStack:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, value):
        self.stack1.append(value)

    def dequeue(self):

        if not self.stack2:

            while self.stack1:
                self.stack2.append(self.stack1.pop())

        if not self.stack2:
            return "Queue is Empty"

        return self.stack2.pop()

    def front(self):

        if not self.stack2:

            while self.stack1:
                self.stack2.append(self.stack1.pop())

        if not self.stack2:
            return "Queue is Empty"

        return self.stack2[-1]

    def is_empty(self):
        return len(self.stack1) == 0 and len(self.stack2) == 0
    

q = QueueUsingStack()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)

print(q.dequeue())
print(q.dequeue())

q.enqueue(50)

print(q.front())

print(q.dequeue())
print(q.dequeue())
print(q.dequeue())