class Node(object):
    def __init__(self, data = None):
        self.data = data
        self.children = [None, None]

class BinaryTree(object):
    def __init__(self):
        self.root = None

    def in_order_r(self, root):
        if root is not None:
            self.in_order_r(root.children[0])
            print root.data
            self.in_order_r(root.children[1])

    def in_order(self):
        self.in_order_r(self.root)

    def pre_order_r(self, root):
        if root is not None:
            print root.data
            self.pre_order_r(root.children[0])
            self.pre_order_r(root.children[1])

    def pre_order(self):
        self.pre_order_r(self.root)

    def post_order_r(self, root):
        if root is not None:
            self.post_order_r(root.children[0])
            self.post_order_r(root.children[1])
            print root.data

    def post_order(self):
        self.post_order_r(self.root)

    def insert_node_r(self, root, data):
        if root is None:
            root = Node(data)
        else:
            child = data > root.data 
            root.children[child] = self.insert_node_r(root.children[child], data)
        return root
            
    def insert_node(self, data):
        self.root = self.insert_node_r(self.root, data)

if __name__ == "__main__":
    binary_tree = BinaryTree()
    data = [5, 2, 8, 4, 9, 3, 1, 8]
    for d in data:
        binary_tree.insert_node(d)

    
    binary_tree.in_order()
    print '---'
    binary_tree.pre_order()
    print '---'
    binary_tree.post_order()
