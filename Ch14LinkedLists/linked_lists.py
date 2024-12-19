class Node():
    def __init__(self,data,next_node):
        self.data=data
        self.next_node=next_node


def search(current_node, value):
    current_index=0
    while current_node.data!=value and current_node != None:
        current_node=current_node.next_node
        current_index+=1
    if current_node is not None:
        return current_index
    else:
        print("not found 404!")


def read(current_node,index):
    current_index=0
    while current_index<index and current_node != None:
        print(f"current index: {current_index} and current_node.data: {current_node.data}")
        current_node=current_node.next_node
        current_index+=1
    if current_node is None:
        return None
    else:
        return current_node.data


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

read(ll,4)
search(ll,11)

    
