import Stack

class MinStack(Stack.Stack):
    ''' A stack that can return the minimum value in constant time'''

    def __init__(self, value=None):
        Stack.Stack.__init__(self, value)
        self.min = Stack.Stack(value)

    def push(self, value):
        super(MinStack, self).push(value)
        if self.min.data and self.min.data[0] > value:
            self.min.push(value)
            
    def pop(self):
        value = super(MinStack, self).pop()
        if self.min.data and value == self.min.data[-1]:
            self.min.pop()
        return value

    def get_min(self):
        if self.min.data:
            return self.min.data[-1]
        return None
        
