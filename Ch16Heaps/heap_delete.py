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


def delete(heap):
    heap.data[0]=heap.data.pop()
    root_index=0

    while True:

        left_child=heap.data[heap.left_child_index(root_index)]
        right_child=heap.data[heap.right_child_index(root_index)]
        largest_index=root_index

        if left_child and left_child>heap.data[root_index]:
            largest_index=heap.left_child_index
            
        if right_child and right_child>heap.data[root_index]:
            largest_index=heap.right_child_index

        if root_index==largest_index:
            break
        
        root_index,largest_index=largest_index,root_index

        return heap.data

      

heap=Heap([100,88,25,87,16,8,12,86,50,2,15,3])

print(delete(heap))


