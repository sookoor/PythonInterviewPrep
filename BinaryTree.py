class Node(object):
    def __init__(self, data = None):
        self.data = data
        self.children = [None, None]
        self.parent = None

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

    def level_order_linked_lists_r(self, root, level, list_collection):
        if root is not None:
            if len(list_collection) <= level:
                list_collection.append([root])
            else:
                list_collection[level].append(root)
            if root.children[0]:
                self.level_order_linked_lists_r(root.children[0], level + 1, list_collection)
            if root.children[1]:
                self.level_order_linked_lists_r(root.children[1], level + 1, list_collection) 

    def level_order_linked_lists(self):
        list_collection = []
        self.level_order_linked_lists_r(self.root, 0, list_collection)
        return list_collection

    def insert_node_r(self, root, data):
        if root is None:
            root = Node(data)
        else:
            child = data > root.data
            root.children[child] = self.insert_node_r(root.children[child], data)
            root.children[child].parent = root
        return root
            
    def insert_node(self, data):
        self.root = self.insert_node_r(self.root, data)

    def build_binary_tree(self, array):
        mid = len(array) / 2
        self.insert_node(array[mid])

        left = array[:mid]
        if left:
            self.build_binary_tree(left)

        right = array[mid+1:]
        if right:
            self.build_binary_tree(right)

    def max_depth(self, root):
        if root is None:
            return 0
        return 1 + max(self.max_depth(root.children[0]), self.max_depth(root.children[1]))

    def min_depth(self, root):
        if root is None:
            return 0
        return 1 + min(self.min_depth(root.children[0]), self.min_depth(root.children[1]))

    def check_balanced(self):
        return self.max_depth(self.root) - self.min_depth(self.root) <= 1

    def next_node(self, node):
        if node is None:
            return
        elif node.children[1]:
            next_node = node.children[1]
            while next_node.children[0] is not None:
                next_node = next_node.children[0]
            return next_node
        elif node.parent:
            next_node = node.parent
            while node.parent and next_node.children[0] != node:
                node = next_node
                next_node = next_node.parent
            if next_node is not None and next_node.children[0] == node:
                return next_node

    def LCA_r(self, root, p, q):
        if root is None:
            return None
        elif root == p or root == q:
            return root
        else:
            left = self.LCA_r(root.children[0], p, q)
            right = self.LCA_r(root.children[1], p, q)
            
        # If p and q are on either side of root
        if left and right:
            return root
        elif left:
            return left
        else:
            return right

    def LCA(self, p, q):
        return self.LCA_r(self.root, p, q)
            
if __name__ == "__main__":
    binary_tree = BinaryTree()
    data = [5, 2, 8, 4, 9, 3, 1, 7, 6]
    for d in data:
        binary_tree.insert_node(d)

    binary_tree.in_order()
    print '---'
    binary_tree.pre_order()
    print '---'
    binary_tree.post_order()

    print binary_tree.check_balanced()

    unbalanced_tree = BinaryTree()
    unbalanced_data = [2, 1, 3, 4, 6]
    for d in unbalanced_data:
        unbalanced_tree.insert_node(d)

    print unbalanced_tree.check_balanced()

    built_tree = BinaryTree()
    built_tree.build_binary_tree(sorted(data))

    print 'Built tree: '
    list_collection = built_tree.level_order_linked_lists()

    for level, node_list in enumerate(list_collection):
        print "Level " + str(level)
        for node in node_list:
            print node.data


    cur_node = built_tree.root.children[1].children[0].children[0]
    next_node = built_tree.next_node(cur_node)
    if next_node:
        print "Next node of " + str(cur_node.data) + " is " + str(next_node.data)
    else:
        print "Node " + str(cur_node.data) + " does not have an in-order successor"

    p = built_tree.root.children[0].children[0]
    q = built_tree.root.children[1]
    lca = built_tree.LCA(p, q)
    if lca:
        print "The LCA of " + str(p.data) + " and " + str(q.data) + " is " + str(lca.data)
    else:
        print str(p.data) + " and " + str(q.data) + " do not have an LCA"
