class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val       
        self.next = next  


def linked_list_intersection(head_A: ListNode, head_B: ListNode):
    ptr_A, ptr_B = head_A, head_B

    while ptr_A != ptr_B:
        ptr_A = ptr_A.next if ptr_A else head_B

        ptr_B = ptr_B.next if ptr_B else head_A

    return ptr_A # returns node

n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n1.next = n2
n2.next = n3
n3.next = n4

m1 = ListNode(5)
m1.next = n3  

head_A = n1  # head of List A
head_B = m1  # head of List B

result = linked_list_intersection(head_A, head_B)
print("\nIntersection at:", result.val if result else None) # because function returns Node - result.val is Node.val