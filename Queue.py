class Queue:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    # Transfer values in stack1 to stack2
    def stack_transfer(self, stack1, stack2):
        while stack1:
            stack2.append(stack1.pop())

    def enqueue(self, value):
        self.in_stack.append(value)

    def dequeue(self):

        # If no items on either stack
        if not self.in_stack and not self.out_stack:
            return None

        # If in_stack has items, but out_stack is empty
        if self.in_stack and not self.out_stack:
            self.stack_transfer(self.in_stack, self.out_stack)

        return self.out_stack.pop()


if __name__ == "__main__":
    myQueue = Queue()
    for i in xrange(1, 10):
        myQueue.enqueue(i)
        
    while True:
        value = myQueue.dequeue()

        if value is None:
            exit(0)
        else:
            print(value)
