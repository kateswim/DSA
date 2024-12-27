class Node():
    def __init__(self,data,next_node):
        self.data=data
        self.next_node=next_node


def delete(current_node,index):
    if index==0:
        return current_node.next_node
    
    current_index=0
    while current_index<index-1 and current_node is not None:
        current_node=current_node.next_node
        current_index+=1
    
    node_after_deleted=current_node.next_node.next_node
    current_node.next_node=node_after_deleted


def list_all(current_node):
    while current_node!=None:
        print(current_node.data)
        current_node=current_node.next_node


ll=Node(1,None)
ll2=Node(4,None)   
ll3=Node(7,None)
ll4=Node(9,None)
ll5=Node(11,None)
ll6=Node(14,None)

ll.next_node=ll2
ll2.next_node=ll3
ll3.next_node=ll4
ll4.next_node=ll5
ll5.next_node=ll6     


delete(ll,3)
list_all(ll)
