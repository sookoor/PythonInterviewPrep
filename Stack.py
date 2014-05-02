class Stack(object):
    def __init__(self, value=None):
        self.data = []
        if value is not None:
            self.data.append(value)

    def push(self, value):
        self.data.append(value)

    def pop(self):
        if self.data:
            return self.data.pop()
        else:
            return None
