import random
from Stack import Stack

def sort_stack(stack):
    new_stack = Stack()
    while not stack.isEmpty():
        cur_item = stack.pop()
        while not new_stack.isEmpty() and cur_item > new_stack.peek():
            stack.push(new_stack.pop())
        new_stack.push(cur_item)
    return new_stack

if __name__ == "__main__":
    stack = Stack()

    x = [i for i in range(10)]
    random.shuffle(x)

    for i in x:
        stack.push(i)

    print stack.data

    stack = sort_stack(stack)

    print stack.data
