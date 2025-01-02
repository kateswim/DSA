class Node():
    def __init__(self,data,next_node,previous_node):
        self.data=data
        self.next_node=next_node
        self.previous_node=previous_node


def insert_at_end(current_node,value):
    new_node=Node(data=value,next_node=None,previous_node=None)
    while current_node!=None and current_node.next_node!=None:
        current_node=current_node.next_node
    current_node.next_node=new_node #forward link
    new_node.previous_node=current_node # backward link

def insert(current_node,index,value):
    new_node=Node(data=value,next_node=None,previous_node=None)
    current_index=0
    if index==0:
        new_node.next_node=current_node #link new node to current node #forward
        current_node.previous_node=new_node
        return new_node #return new head of the list
   
    while current_index<index-1 and current_node!=None: #we need to reach preceding node 
        # old_node = current_node
        current_node=current_node.next_node
        current_index+=1
    new_node.next_node=current_node.next_node #we create new link from new inserted node to node after current
    current_node.next_node.previous_node=new_node 

    current_node.next_node=new_node #current node becomes new just inserted node
    new_node.previous_node=current_node


def list_all(current_node):
    while current_node!=None:
        print(current_node.data)
        current_node=current_node.next_node
    
def list_all_backwards(current_node):
    while current_node!=None and current_node.next_node!=None:
        current_node=current_node.next_node
    while current_node!= None:
        print(current_node.data)
        current_node = current_node.previous_node



ll=Node(1,None,None)
ll2=Node(2,None,None)   
ll3=Node(3,None,None)
ll4=Node(4,None,None)
ll5=Node(5,None,None)
ll6=Node(6,None,None)

ll.next_node=ll2

ll2.next_node=ll3
ll3.next_node=ll4
ll4.next_node=ll5
ll5.next_node=ll6  

x = Node(1,None,None)
insert_at_end(x,2)
insert_at_end(x,3)
insert_at_end(x,4)
insert_at_end(x,5)
insert_at_end(x,6)

        


