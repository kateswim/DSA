class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val       
        self.next = next  


def linked_list_midpoint(head: ListNode):
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

head = node1

mid = linked_list_midpoint(head)
print(mid.val)