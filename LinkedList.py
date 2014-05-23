import sys

class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList(object):
    def __init__(self):
        self.head = None
    
    def add_node(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def remove_duplicates(self):
        seen_vals = []
        if self.head is not None:
            cur = self.head
            prev = cur
            while cur is not None:
                if cur.data in seen_vals:
                    prev.next = cur.next
                else:
                    seen_vals.append(cur.data)
                    prev = cur
                cur = cur.next

    def remove_duplicates_no_buffer(self):
        if self.head is not None:
            cur = self.head.next

            while cur is not None:
                prev = self.head

                while cur != prev:
                    if cur.data == prev.data:
                        prev.next = prev.next.next
                        break
                    else:
                        prev = prev.next
                cur = cur.next

    def print_list(self):
        if self.head:
            cur = self.head
            while cur is not None:
                sys.stdout.write(str(cur.data))
                if cur.next is not None:
                    sys.stdout.write(' --> ')
                else:
                    sys.stdout.write('\n')
                cur = cur.next

    def nth_to_last(self, n):
        if self.head is not None:
            runner = self.head
            nth = self.head
            i = 0
            for i in range(n):
                if runner.next:
                    runner = runner.next
                else:
                    break

            if i == n - 1:
                while runner.next:
                    runner = runner.next
                    nth = nth.next
                return nth
        
    def delete_middle_node(self, node):
        if node is not None and node.next is not None:
            node.data = node.next.data
            node.next = node.next.next
        
    def _partition_list(self, node_list, x):
        num_nodes = len(node_list)
        head = 0
        tail = num_nodes - 1
        while head < tail:
            while node_list[head].data < x and head < num_nodes:
                head += 1
                
            if node_list[head] >= x:
                while node_list[tail].data >= x and tail > head:
                    tail -= 1
                    
                node_list[head], node_list[tail] = node_list[tail], node_list[head]

    def partition_list(self, x):
        if self.head is not None:
            temp_array = []
            cur = self.head
            while cur is not None:
                temp_array.append(cur)
                cur = cur.next
                
            self._partition_list(temp_array, x)
            self.head = temp_array[0]

            cur = self.head
            for node in temp_array[1:]:
                cur.next = node
                cur = cur.next
            cur.next = None
    
if __name__ == "__main__":
    linked_list = LinkedList()
    for val in [1, 2, 1, 3, 2]:
        linked_list.add_node(val)

    linked_list.print_list()

    linked_list.partition_list(2)

    linked_list.print_list()

    print linked_list.nth_to_last(2).data

    linked_list.remove_duplicates()
    linked_list.print_list()
    
    linked_list.delete_middle_node(linked_list.head.next)
    linked_list.print_list()

    linked_list_2 = LinkedList()
    for val in [1, 1]:
        linked_list_2.add_node(val)
    
    linked_list_2.print_list()
    linked_list_2.remove_duplicates_no_buffer()
    linked_list_2.print_list()
    
    print linked_list_2.nth_to_last(2)
