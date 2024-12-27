from SortableArray import SortableArray


def quicksort(left_index,right_index):
    if right_index-left_index<=0:
       return # it is not returning anything because it needs base case for last step of sorting
    
    pivot_index=oSortableArray.partition(left_index,right_index) #returns left_index, which is pivot

    quicksort(left_index,pivot_index-1)

    quicksort(pivot_index+1,right_index)


array=[1,87,34,0,8,4,11,54,23,16,9,67,4,9,3,23]
oSortableArray=SortableArray(array)
quicksort(0,len(array)-1)
print(f"array after quicksort: {array}")
