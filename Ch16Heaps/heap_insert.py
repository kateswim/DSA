class Heap:
    def __init__(self, data=None):
        if data:
            self.data = data
        else:
            self.data = []
    
    def root_node(self):
        if self.data:
            return self.data[0]
        else:
            return None

    def last_node(self):
        if self.data:
            return self.data[-1]
        else:
            return None

    def left_child_index(self,index):
        return (index*2)+1

    def right_child_index(self,index):
        return (index*2)+2   

    def parent_index(self,index):
        return (index-1)//2

def insert(heap,value):
    heap.data.append(value)
    new_node_index=len(heap.data)-1
    new_node=heap.data[new_node_index]
    parent_node=heap.data[heap.parent_index(new_node_index)]

    while new_node_index>0 and new_node>parent_node:
        parent_node,new_node=new_node,parent_node

        new_node_index=heap.parent_index(new_node_index)
        
        return heap.data



heap=Heap([100,88,25,87,16,8,12,86,50,2,15,3])

print(insert(heap,25))


