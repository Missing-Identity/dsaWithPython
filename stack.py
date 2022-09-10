# Initialising Stack Class
class Stack:
    def __init__(self, size):
        self.arr = [None] * size
        self.top = -1
        self.size = size

    # Pushing elements to stack of particular size
    def push(self, val):
        if self.top is self.size - 1:
            print("Stack is full")
        else:
            self.top = self.top + 1
            self.arr[self.top] = val
            print(self.arr[self.top])

    # Popping Stack elements
    def pop(self):
        if self.top == -1:
            print("Stack is empty")
        else:
            print("Popped element = ", self.arr[self.top])
            self.top = self.top - 1


# Output
stack = Stack(3)
stack.push(1)
stack.push(230)
stack.push(500)
stack.push(34)
stack.pop()
stack.pop()
stack.pop()
stack.pop()
