def max_number(array):
    for i in range(0,len(array)):
        max=array[i]
        for j in range(i+1,len(array)):
            if array[j]>array[j]:
                max=array[j]
    return max
                
def max_number2(array):
    if len(array)==1:
        return array[0]
    max=max_number2(array[1:])
    if array[0]>max:
        return array[0]
    else:
        return max

def max_number3(array):
    array.sort()
    return array[len(array)-1]


array=[2,67,8,90,34,12,34,7,2,3,8,94,67,98]
print(max_number(array))
print(max_number2(array))
print(max_number3(array))
