class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    # Transfer values in stack1 to stack2
    def stack_transfer(self, stack1, stack2):
        while stack1:
            stack2.append(stack1.pop())

    def enqueue(self, value):
        self.stack_transfer(self.stack1, self.stack2)
        self.stack1.append(value)
        self.stack_transfer(self.stack2, self.stack1)

    def dequeue(self):
        if self.stack1:
            return self.stack1.pop()
        else:
            return None

if __name__ == "__main__":
    myQueue = Queue()
    for i in xrange(1, 10):
        myQueue.enqueue(i)
        
    value = True
    while value is not None:
        value = myQueue.dequeue()
        print value
