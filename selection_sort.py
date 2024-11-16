def selection_sort(array):
    for i in range(len(array)): #outer loop starts with first index and assigns it to minimum
        min_index_number=i
        for j in range(i+1,len(array)): #innel loop checks all remained indexes and assigns to new (minimum=j), if found
            if array[j]<array[min_index_number]: 
                min_index_number=j
        
        if min_index_number!=i: #if smallest number is not on the smallest index place- swipe
            array[i],array[min_index_number]=array[min_index_number],array[i]

    return array


array=[5,90,8,87,65678,3,7,33,0,23,765,4]
print(selection_sort(array))
            





