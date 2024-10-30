def bubble_sort(list):
    index=len(list)-1
    sorted=False
    while not sorted:
        sorted=True
        for i in range(index):
            if list[i]>list[i+1]:
                list[i],list[i+1]=list[i+1],list[i]
                sorted=False
        index-=1
    return list

print(bubble_sort([10,8,5,13,5,3,6,7]))
print(bubble_sort([4,22,11,434,543,24,56,2345]))
