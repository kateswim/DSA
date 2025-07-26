class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val       
        self.next = next 


def remove_kth_last_node(head: ListNode, k: int):
    dummy = ListNode(-1)
    dummy.next = head
    trailer = leader = dummy

    for _ in range(k):
        leader = leader.next
        if not leader:
            return head
        
    while leader.next:
        trailer = trailer.next
        leader = leader.next

    trailer.next = trailer.next.next
    return dummy.next

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
k = 2
new_head = remove_kth_last_node(head, k)
print_linked_list(new_head)
