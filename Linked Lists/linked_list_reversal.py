class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val       
        self.next = next      


def linked_list_reversal(head: ListNode):
    current_node, previous_node = head, None
    while current_node:
        next_node = current_node.next
        current_node.next = previous_node
        previous_node = current_node
        current_node = next_node

    return previous_node

def print_linked_list(head):
    node = head
    while node:
        print(node.val, end=' ')
        node = node.next
    print()

n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n1.next = n2
n2.next = n3
n3.next = n4

head = n1
reversed_head = linked_list_reversal(head)
print_linked_list(reversed_head)


def reverse_recursive(head: ListNode):
    if (not head) or (not head.next):
        return head

    new_head = reverse_recursive(head.next)

    next_node = node.next
    node.next = prev
    return new_head

reversed_head = reverse_recursive(head)
print_linked_list(reversed_head)

