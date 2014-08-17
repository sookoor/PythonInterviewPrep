class SetOfStacks(object):
    def __init__(self, capacity=10):
        self.stack_set = [[]]
        self.cur = 0
        self.capacity = capacity

    def push(self, val):
        if len(self.stack_set[self.cur]) >= self.capacity:
            self.stack_set.append([])
            self.cur += 1
        self.stack_set[self.cur].append(val)

    def pop(self, index=None):
        if index is None:
            index = self.cur
        val = None
        if len(self.stack_set[index]) > 0:
            val = self.stack_set[index].pop()
        if len(self.stack_set[index]) == 0 and self.cur > 0:
            self.stack_set.pop(index)
            self.cur -= 1
        return val

    def pop_at(self, index):
        if type(index) is int and index >= 0 and index <= self.cur:
            return self.pop(index)

if __name__ == "__main__":
    s = SetOfStacks()

    assert s.cur == 0

    for i in range(30):
        s.push(i)

    assert s.cur == 2

    for i in [19, 18, 17, 16, 15, 14, 13, 12, 11, 10]:
        assert s.pop_at(1) == i

    assert s.cur == 1

    assert s.pop() == 29

    
