def findMissingNumber(array):
    array.sort()

    for i in range(1, len(array)):
        if array[i-1] +1 == array[i]:
            pass
        else:
            #return array[i-1]+1
            return array[i]-1
            

array=[5,2,4,1,0]
print(findMissingNumber(array))

   
