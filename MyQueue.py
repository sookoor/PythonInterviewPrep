# A queue based on two stacks

class MyQueue(object):
    def __init__(self):
        self.vals = [[], []]
        
    def enqueue(self, val):
        self.vals[0].append(val)

    def _move(self):
        while len(self.vals[0]) > 0:
            self.vals[1].append(self.vals[0].pop())

    def dequeue(self):
        if len(self.vals[1]) == 0:
            self._move()

        if len(self.vals[1]) > 0:
            return self.vals[1].pop()

    def size(self):
        return len(self.vals[0]) + len(self.vals[1])

    def peek(self):
        if len(self.vals[1]) == 0:
            self._move()

        if len(self.vals[1]) > 0:
            return self.vals[1][-1]

if __name__ == "__main__":
    q = MyQueue()
    
    for i in range(10):
        q.enqueue(i)

    for i in range(5):
        assert q.dequeue() == i

    assert q.peek() == 5

    assert q.size() == 5
