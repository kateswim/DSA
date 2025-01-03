import math

maxSize = 10
size = 0
H = [0,0,0,0,0,0,0,0,0,0]

infinity = math.inf
#negative_infinity = -math.inf

def Parent(i):
    return (i-1)//2

def LeftChild(i):
    return (i*2)+1

def RightChild(i):
    return (i*2)+2

def SiftUp(i):
    while i>0 and H[Parent(i)]< H[i]:
        H[Parent(i)], H[i] = H[i], H[Parent(i)]
        i = Parent(i)

def SiftDown(i):
    global size
    global maxSize
    maxIndex = i
    l = LeftChild(i)
    if l <= size and H[l] > H[maxIndex]:
        maxIndex = l
    r = RightChild(i)
    if r <= size and H[r] > H[maxIndex]:
        maxIndex = r
    if i != maxIndex:
        # swap H[i] and H[maxIndex]
        H[i], H[maxIndex] = H[maxIndex], H[i]
        SiftDown(maxIndex)

def insert(p):
    global size
    global maxSize
    if size==maxSize:
        print("Error its all full!")
        return 
    size+=1
    H[size]= p
    SiftUp(size)

def ExtractMax():
    global size
    result = H[0]
    H[0] = H[size-1] #because we have 0 based array
    size-=1
    SiftDown(0)
    return result

def Remove(i):
    global size
    if i < 0 or i >= size:
        raise IndexError("Index out of bounds")
    
    H[i] = infinity
    SiftUp(i)
    ExtractMax()

def ChangePriority(i,p):
    oldp = H[i]
    H[i] = p
    if p > oldp:
        SiftUp(i)
    else:
        SiftDown(i)


insert(7)
insert(90)
insert(33)
insert(77)
insert(100)
print(H)
print(maxSize)
Remove(2)
Remove(1)
print(H)
