def even_num(array1,array2=[]):  
    if len(array1) == 0:
        return array2
    if array1[0]%2==0:
        array2.append(array1[0])
        even_num(array1[1:])   
    else:
        return even_num(array1[1:])
    
    return array2
    
   
    
print(even_num([1,5,8,10,20,4,7,0,-1,-76,-456,390]))