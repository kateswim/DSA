from SortableArray import SortableArray

def quicksort(right_index,left_index):
    if right_index-left_index<=0:
        return
    
    pivot_index=oSortableArray.partition(right_index,left_index)

    quicksort(left_index,pivot_index-1,)

    quicksort(pivot_index+1,right_index)

def greatest_product(array):
    quicksort(0,len(array)-1)
    max=array[len(array)-1]*array[len(array)-2]*array[len(array)-3]
    return max


array=[1,87,34,0,8,4,11,54,23,16,9,67,4,9,3,23]
oSortableArray=SortableArray(array) #instantiation object from class
print(greatest_product(array))

    


