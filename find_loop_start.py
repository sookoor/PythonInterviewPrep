from LinkedList import LinkedList

def find_loop_start(circular_list):
    if circular_list is not None:
        fast = circular_list.head
        slow = circular_list.head

        

        # Since fast is moving at twice the speed of slow, it will be
        # k nodes into the cycle when slow enters, where k is the
        # number of nodes between the head and the start of the
        # cycle. Due to fast having a k node head start, the two
        # pointers with meet k nodes from the start of the cycle
        while fast.next:
            if fast.next.next:
                fast = fast.next.next
            else:
                
                # Not a circular list
                return 

            slow = slow.next
            
            if fast == slow:
                break

        if fast.next is None:

            # Not circular
            return

        # Moving slow back to the beginning of the list, puts it k
        # nodes from the start of the cycle
        slow = circular_list.head

        # Since fast is k nodes from the start of the cycle as well,
        # moving both pointers one node at a time would cause them to
        # meet at the beginning of the cycle
        while fast != slow:
            fast = fast.next
            slow = slow.next

        return fast


if __name__ == "__main__":
    list_vals = ["E", "D", "C", "B", "A"]

    circular_list = LinkedList()
    for val in list_vals:
        circular_list.add_node(val)

    ptr = circular_list.head
    while ptr.next is not None:
        ptr = ptr.next

    circular_list.print_list()

    ptr.next = circular_list.head.next.next

    cycle_start = find_loop_start(circular_list)
    print cycle_start.data
            
