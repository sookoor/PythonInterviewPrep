from collections import deque
from collections import defaultdict

class Tree:
    def __init__ (self, data, children=None):
        self.data = data

        if children:
            self.children.extend(children)
        else:
            self.children = []

    def bfs(self, process_vertex_early=None, process_edge=None, process_vertex_late=None):
        visitedNodes = set()
        queue = deque([self])
        parent = {}
        while queue:
            node = queue.pop()

            if node.data in visitedNodes:
                continue

            if process_vertex_early:
                process_vertex_early(node)

            visitedNodes.add(node.data)

            if node.children:
                for n in node.children:
                    if n.data not in visitedNodes:
                        if process_edge:
                            process_edge(node, n)
                        queue.appendleft(n)
                        parent[n.data] = node.data

            if process_vertex_late:
                process_vertex_late(node)
        return parent

class BinaryTree:
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

def generate_search_func(search_key):
    def search(node):
        if node and node.data == search_key:
            print str(search_key) + " found!!!" 
    return search

def print_edge(x, y):
    print "processed edge (%s,%s)" %(x.data, y.data)

def print_vertex(vertex):
    print "processed vertex %s" %(vertex.data)

count = 0
def edge_count(x, y):
    global count
    count += 1

def find_path(start, end, parents):
    if end not in parents or start == end:
        print start
    else:
        find_path(start, parents[end], parents)
        print end

def test():
    # A = Tree("A")
    # B = Tree("B")
    # C = Tree("C")
    # D = Tree("D")
    # E = Tree("E")
    # F = Tree("F")
    # A.left = B
    # B.left = C
    # C.left = E
    # D.left = B
    # E.left = D
    # E.right = F
    # print A.bfs("A")
    # print A.bfs("E")
    # print A.bfs("F")
    # print A.bfs("X")

    tree = Tree("A")
    tree.children = [Tree("B")]
    tree.children[0].children = [Tree("C")]
    tree.children[0].children[0].children = [Tree("E")]
    tree.children[0].children[0].children[0].children = [Tree("D"), Tree("F")]
    tree.children[0].children[0].children[0].children[0].children = [Tree("B")]

    search_func = generate_search_func("E")
    global count
    count = 0
    parent = tree.bfs(search_func, edge_count, print_vertex)
    print count
#    find_path("A", "F", parent)

if __name__ == "__main__":
    test()
