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