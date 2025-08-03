class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val       
        self.next = next  


def linked_list_loop_naive(head: ListNode):
    visited = set()
    curr = head

    while curr:
        if curr in visited:
            return True
        visited.add(curr)
        curr = curr.next

    return False

