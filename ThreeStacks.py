# Use a single array to implement three stacks


class ThreeStacks(object):
    def __init__(self):
        self.stack_array = []
        self.tops = [None, None, None]
        self.next_free = 0
        self.free_list = []
        
    def _check_stack_id(self, stack_id):
        if stack_id is None or type(stack_id) is not int or stack_id < 0 or stack_id > 2:
            raise RuntimeError("Invalid stack ID")
            
    def push(self, stack_id, val):
        try:
            self._check_stack_id(stack_id)
        except RuntimeError:
            raise 
            
        if len(self.free_list) > 0:
            i = self.free_list.pop(0)
        else:
            i = self.next_free
            self.next_free += 1

        prev = self.tops[stack_id]
        self.tops[stack_id] = i

        self.stack_array.insert(i, (val, prev))

    def pop(self, stack_id):
        try:
            self._check_stack_id(stack_id)
        except RuntimeError:
            raise 

        top = self.tops[stack_id]
        val = None
        if top is not None:
            val, prev = self.stack_array[top]
            self.free_list.append(top)
            self.tops[stack_id] = prev
        return val

    def peek(self, stack_id):
        try:
            self._check_stack_id(stack_id)
        except RuntimeError:
            raise 

        top = self.tops[stack_id]
        if top is not None:
            return self.stack_array[top][0]
        else:
            return None

    def is_empty(self, stack_id):
        try:
            self._check_stack_id(stack_id)
        except RuntimeError:
            raise 

        return self.tops[stack_id] is None

if __name__ == "__main__":
    s1 = [1, 3, 5, 7, 9]
    s2 = [2, 4, 6, 8]
    s3 = [1, 2, 3, 4, 5, 6]

    stack = ThreeStacks()
    assert stack.is_empty(0) == True

    for val in s2:
        stack.push(1, val)
   
    for val in s1:
        stack.push(0, val)
    
    assert stack.pop(0) == 9
    assert stack.is_empty(0) == False

    l = len(s2)
    for i in range(l):        
        p = stack.pop(1)
        s = s2[l - i - 1]
        assert p == s
        
    assert stack.is_empty(1) == True

    for val in s3:
        stack.push(2, val)

    assert stack.peek(2) == 6
    assert stack.pop(2) == 6
    assert stack.peek(2) == 5

    try:
        print(stack.pop(3))
    except RuntimeError:
        print("Invalid stack ID identified")
