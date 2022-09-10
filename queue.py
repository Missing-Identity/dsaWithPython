# Initialising Queue
class Queue:
    def __init__(self, size):
        self.arr = [None] * size
        self.front = 0
        self.rear = 0
        self.size = size

    # Inserting elements into queue
    def enqueue(self, val):
        if self.rear is self.size:
            print("The Queue is full")
        else:
            self.arr[self.rear] = val
            print("Enqueued element: ", self.arr[self.rear])  # Printing Value added to queue
            self.rear += 1

    # Deleting elements from a queue
    def dequeue(self):
        if self.front is self.rear:
            print("Queue is empty")
        else:
            print("Dequeued Element:", self.arr[self.front])
            self.front = self.front + 1


# Outputs
q = Queue(3)
q.enqueue(45)
q.enqueue(56)
q.enqueue(67)
q.enqueue(56)
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
