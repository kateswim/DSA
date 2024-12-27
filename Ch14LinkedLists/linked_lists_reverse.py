class Node():
    def __init__(self,data,next_node):
        self.data=data
        self.next_node=next_node


def reverse_list(current_node):
    previous_node=None

    while current_node is not None :
        next_node=current_node.next_node

        current_node.next_node=previous_node #reverse
        
        previous_node=current_node #move 1 step forward
        current_node=next_node

    return previous_node

def list_all(current_node):
    while current_node!=None:
        print(current_node.data)
        current_node=current_node.next_node


ll=Node(1,None)
ll2=Node(2,None)   
ll3=Node(3,None)
ll4=Node(4,None)
ll5=Node(5,None)
ll6=Node(6,None)

ll.next_node=ll2
ll2.next_node=ll3
ll3.next_node=ll4
ll4.next_node=ll5
ll5.next_node=ll6  

reverse_list(ll)
list_all(ll6)       



