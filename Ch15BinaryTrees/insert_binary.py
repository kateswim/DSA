class TreeNode():
    def __init__(self,value):
        self.value=value
        self.rightChild=None
        self.leftChild=None


def insert(array,node):
    for value in array:
        if value<node.value:
            if node.leftChild is None:
                node.leftChild=TreeNode(value)
            else:
                insert([value],node.leftChild)

        elif value>node.value:
            if node.rightChild is None:
                node.rightChild=TreeNode(value)
            else:
                insert([value],node.rightChild)
        
def traverse_print(node):
    if node is None:
        return
    else:
        traverse_print(node.leftChild)
        traverse_print(node.rightChild)
        print(node.value)

array=[1,5,9,2,4,10,6,3,8]
node=TreeNode(array[0]) #instantiating node

insert(array[1:],node)

traverse_print(node)

