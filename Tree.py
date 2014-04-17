from collections import deque

class Tree:
    def __init__ (self, data, left_node=None, right_node=None):
        self.data = data
        self.left = left_node
        self.right = right_node

    def dfs_stack(self, soughtValue):
        visitedNodes = set()
        stack = [self]
        
        while stack:
            node = stack.pop()
            if node in visitedNodes:
                continue
            
            visitedNodes.add(node)
            if node and node.data == soughtValue:
                return True

            if node:
                stack.append(node.left)
                stack.append(node.right)

        return False

    def dfs_recursive(self, soughtValue, visitedNodes=None):
        if self.data == soughtValue:
            return True

        if visitedNodes is None:
            visitedNodes = set()
        
        visitedNodes.add(self.data)
        if self.left is not None and self.left.data not in visitedNodes:
            if self.left.dfs(soughtValue, visitedNodes):
                return True
        if self.right is not None and self.right.data not in visitedNodes:
            if self.right.dfs(soughtValue, visitedNodes):
                return True

        return False

    def bfs(self, soughtValue):
        visitedNodes = set()
        queue = deque([self])
        
        while queue:
            node = queue.pop()
            if node in visitedNodes:
                continue

            visitedNodes.add(node)
            if node and node.data == soughtValue:
                return True
                
            if node:
                queue.appendleft(node.left)
                queue.appendleft(node.right)
        return False

def test():
    A = Tree("A")
    B = Tree("B")
    C = Tree("C")
    D = Tree("D")
    E = Tree("E")
    F = Tree("F")
    A.left = B
    B.left = C
    C.left = E
    D.left = B
    E.left = D
    E.right = F
    print A.bfs("A")
    print A.bfs("E")
    print A.bfs("F")
    print A.bfs("X")

if __name__ == "__main__":
    test()
