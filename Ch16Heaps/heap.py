import math

maxSize = 10
size = 0
H = [0,0,0,0,0,0,0,0,0,0]

infinity = math.inf
#negative_infinity = -math.inf

def Parent(i):
    return i//2

def LeftChild(i):
    return 2*i

def RightChild(i):
    return (2*i)+1

def SiftUp(i):
    while i>1 and H[Parent(i)]< H[i]:
        # swap H[Parent(i)] and H[i]
        placeholder = H[Parent(i)]
        H[Parent(i)] = H[i]
        H[i] = placeholder
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
        placeholder = H[maxIndex]
        H[maxIndex] = H[i]
        H[i] = placeholder
        SiftDown(maxIndex)

def insert(p):
    global size
    global maxSize
    if size==maxSize:
        print("Error its all full!")
        return 
    size = size +1
    H[size]= p
    SiftUp(size)

def ExtractMax():
    global size
    global maxSize
    result = H[1]
    H[1] = H[size]
    size = size -1
    SiftDown(1)
    return result

def Remove(i):
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
Remove(90)
Remove(33)
print(H)
