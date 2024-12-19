class Node():
    def __init__(self,data,next_node):
        self.data=data
        self.next_node=next_node

def insert(current_node,index,value):
    new_node=Node(data=value,next_node=None)
    current_index=0
    if index==0:
        new_node.next_node=current_node #link new node to current node
        return new_node #return new head of the list
   
    while current_index<index-1 and current_node != None: #we need to reach preceding node 
        current_node=current_node.next_node
        current_index+=1
    new_node.next_node=current_node.next_node #we create new link from new inserted node to node after current
    current_node.next_node=new_node #current node becomes new just inserted node
    
    while current_node is not None: #to print all nodes
        print(f"current index: {current_index} and current_node.data: {current_node.data}")
        current_node = current_node.next_node

def insert_at_end(current_node,value):
    new_node=Node(data=value,next_node=None)
    while current_node != None and current_node.next_node != None:
        current_node=current_node.next_node
    current_node.next_node=new_node

    while current_node is not None: #to print all nodes
        print(f"current_node.data: {current_node.data}")
        current_node = current_node.next_node

def insert_at_end_2(current_node,value):
    new_node=Node(data=value,next_node=None)
    while current_node != None:
        previous_node = current_node # this will actually be last node with some data at end of while loop
        current_node=current_node.next_node # this jumps to none at end
    previous_node.next_node=new_node


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


insert(ll,3,17)
insert_at_end(ll,34)
insert_at_end_2(ll,34)
    