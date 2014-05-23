from LinkedList import LinkedList

def add_linked_lists(l1, l2):
    if l1 is None:
        return l2
    elif l2 is None:
        return l1

    carry = 0
    sum_list = LinkedList()
    while l1 is not None and l2 is not None:
        cur_sum = l1.data + l2.data + carry
        sum_list.add_node(cur_sum % 10)
        carry = cur_sum / 10
        l1 = l1.next
        l2 = l2.next

    while l1 is not None:
        sum_list.add_node(l1.data)
        l1 = l1.next

    while l2 is not None:
        sum_list.add_node(l2.data)
        l2 = l2.next

    return sum_list

l1 = LinkedList()
l2 = LinkedList()

n1 = [5, 1, 3]
n2 = [2, 9, 5]

for i in n1:
    l1.add_node(i)

for i in n2:
    l2.add_node(i)

sum_list = add_linked_lists(l1.head, l2.head)

sum_list.print_list()
