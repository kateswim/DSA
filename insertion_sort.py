def insertion_sort(array): 
    for index in range(1,len(array)):
        temp=array[index]
        position=index-1 #one step to the left

        while position>=0: 
            if array[position]>temp:
                array[position],temp=temp,array[position]
                position-=1
            else:
                break


    return array

array=[3,89,876,3,4,0,54,23,99,9,1,23,45,67,34,56,88]
print(insertion_sort(array))