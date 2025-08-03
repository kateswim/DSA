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
