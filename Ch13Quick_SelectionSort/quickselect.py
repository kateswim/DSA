from SortableArray import SortableArray

def quickselect(k_lowest,left_index,right_index):
    if right_index-left_index<=0:
        return array[left_index]
    
    pivot_index=oSortableArray.partition(left_index,right_index)

    if k_lowest<pivot_index:
        return quickselect(k_lowest,left_index,pivot_index-1)
    
    elif k_lowest>pivot_index:
        return quickselect(k_lowest,pivot_index+1,right_index)

    else:
        return array[pivot_index]


array=[1,87,34,0,8,4,11,54,23,16,9,67,4,9,3,23]
oSortableArray=SortableArray(array)
print(quickselect(3,0,len(array)-1))