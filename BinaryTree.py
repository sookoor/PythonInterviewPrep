import sys

class Node(object):
    def __init__(self, data = None):
        self.data = data
        self.children = [None, None]
        self.parent = None

class BinaryTree(object):
    def __init__(self):
        self.root = None

    def _insert_node(self, root, data):
        if root is None:
            root = Node(data)
        else:
            child = data > root.data
            root.children[child] = self._insert_node(root.children[child], data)
            root.children[child].parent = root
        return root
            
    def insert_node(self, data):
        self.root = self._insert_node(self.root, data)

    def _in_order(self, root):
        if root is not None:
            self._in_order(root.children[0])
            print(root.data)
            self._in_order(root.children[1])

    def in_order(self):
        self._in_order(self.root)

    def _pre_order(self, root):
        if root is not None:
            print(root.data)
            self._pre_order(root.children[0])
            self._pre_order(root.children[1])

    def pre_order(self):
        self._pre_order(self.root)

    def _post_order(self, root):
        if root is not None:
            self._post_order(root.children[0])
            self._post_order(root.children[1])
            print(root.data)

    def post_order(self):
        self._post_order(self.root)

    def _level_order_linked_lists(self, root, level, list_collection):
        if root is not None:
            if len(list_collection) <= level:
                list_collection.append([root])
            else:
                list_collection[level].append(root)
            if root.children[0]:
                self._level_order_linked_lists(root.children[0], level + 1, list_collection)
            if root.children[1]:
                self._level_order_linked_lists(root.children[1], level + 1, list_collection) 

    def level_order_linked_lists(self):
        list_collection = []
        self._level_order_linked_lists(self.root, 0, list_collection)
        return list_collection

    def _insert_node(self, root, data, bst):
        if root is None:
            root = Node(data)
        else:
            if bst == True:
                child = data > root.data
            else:
                child = data < root.data

            root.children[child] = self._insert_node(root.children[child], data, bst)
            root.children[child].parent = root
        return root
            
    def insert_node(self, data, bst = True):
        self.root = self._insert_node(self.root, data, bst)

    def build_binary_tree(self, array, bst = True):
        mid = len(array) / 2
        self.insert_node(array[mid], bst)

        left = array[:mid]
        if left:
            self.build_binary_tree(left, bst)

        right = array[mid+1:]
        if right:
            self.build_binary_tree(right, bst)

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

    def _LCA(self, root, p, q):
        if root is None:
            return None
        elif root == p or root == q:
            return root
        else:
            left = self._LCA(root.children[0], p, q)
            right = self._LCA(root.children[1], p, q)
            
        # If p and q are on either side of root
        if left and right:
            return root
        elif left:
            return left
        else:
            return right

    def LCA(self, p, q):
        return self._LCA(self.root, p, q)

    def _is_identical(self, root1, root2):
        if root1 is None and root2 is None:
            return True
        elif root1 is None or root2 is None:
            return False
        else:
            return root1.data == root2.data and self._is_identical(root1.children[0], root2.children[0]) and self._is_identical(root1.children[1], root2.children[1])

    def _is_subtree(self, root, target):
        if root is None:
            return False
        elif target is None or self._is_identical(root, target):
            return True
        else:
            return self._is_subtree(root.children[0], target) or self._is_subtree(root.children[1], target)

    def is_subtree(self, target):
        return self._is_subtree(self.root, target.root)

    def _check_sum(self, root, value, paths, cur_path=None):

        if cur_path is None:
            cur_path = []

        if root is not None:
            if root.data == value:
                cur_path = []
                paths.append([root.data])
            elif root.data > value:
                cur_path = []
            elif root.data + sum(cur_path) < value:
                cur_path.append(root.data)
            elif root.data + sum(cur_path) == value:
                paths.append(cur_path + [root.data])
                cur_path = []
            elif root.data + sum(cur_path) > value:
                cur_path = [root.data]

            self._check_sum(root.children[0], value, paths, cur_path)
            self._check_sum(root.children[1], value, paths, cur_path)

    def check_sum(self, value):
        paths = []
        self._check_sum(self.root, value, paths)
        return paths

    def _longest_bst(self, root):
        if root is None:
            return 0
        else:
            left_size = self._longest_bst(root.children[0])
            right_size = self._longest_bst(root.children[1])
            max_child_size = max(abs(left_size), abs(right_size))

            if left_size == 0 and right_size == 0:
                return 1
            elif left_size < 0 or right_size < 0:
                return - max_child_size
            elif left_size == 0:
                if root.data < root.children[1].data:
                    return 1 + right_size
                else:
                    return -right_size
            elif right_size == 0:
                if root.data >= root.children[0].data:
                    return 1 + left_size
                else:
                    return -left_size
            elif root.data >= root.children[0] and root.data < root.children[1]:
                return 1 + max_child_size
            else:
                return -max_child_size
                
    def longest_bst(self):
        return abs(self._longest_bst(self.root))

    def _is_bst(self, root):
        if root is None:
            return True
        else:
            left = self._is_bst(root.children[0])
            if root.children[0] is not None:
                left = left and root.children[0].data <= root.data
                
            right = self._is_bst(root.children[1])
            if root.children[1] is not None:
                right = right and root.children[1].data > root.data

            return left and right

    def is_bst(self):
        return self._is_bst(self.root)
            
if __name__ == "__main__":
    binary_tree = BinaryTree()
    data = [5, 2, 8, 4, 9, 3, 1, 7, 6]
    for d in data:
        binary_tree.insert_node(d)

    print 'In-order'
    binary_tree.in_order()
    print '---'

    print 'Pre-order'
    binary_tree.pre_order()
    print '---'

    print 'Post-order'
    binary_tree.post_order()
    print '---'

    assert(binary_tree.check_balanced() == True)

    unbalanced_tree = BinaryTree()
    unbalanced_data = [2, 1, 3, 4, 6]
    for d in unbalanced_data:
        unbalanced_tree.insert_node(d)

    assert (unbalanced_tree.check_balanced() == False)

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

    
    s = [6, 7, 8, 9]
    t = [2, 3, 4]

    subtree = BinaryTree()
    subtree.build_binary_tree(s)

    not_subtree = BinaryTree()
    not_subtree.build_binary_tree(t)

    assert (binary_tree.is_subtree(subtree) == True)
    assert (binary_tree.is_subtree(not_subtree) == False)

    print built_tree.check_sum(5)
    print built_tree.check_sum(6)
    print built_tree.check_sum(17)

    bt = [5, 6, 12, 8, 9, 10]
    bin_tree = BinaryTree()
    bin_tree.build_binary_tree(bt)
    bin_tree.in_order()
    print bin_tree.longest_bst()

    assert binary_tree.is_bst() == True
    
    not_bst = BinaryTree()
    not_bst.build_binary_tree(s, False)

    lists = not_bst.level_order_linked_lists()

    for li in lists:
        for l in li:
            sys.stdout.write(str(l.data) + " ")
        print " "

    assert not_bst.is_bst() == False

