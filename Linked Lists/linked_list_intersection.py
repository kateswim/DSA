class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val       
        self.next = next  


def linked_list_intersection(head_A: ListNode, head_B: ListNode):
    ptr_A, ptr_B = head_A, head_B

    while ptr_A != ptr_B:
        ptr_A = ptr_A.next if ptr_A else head_B

        ptr_B = ptr_B.next if ptr_B else head_A

    return ptr_A


