def has_duplicates(array):
    for i in range(len(array)):
        for j in range(len(array)):
            if i!=j and array[i]==array[j]:
                #print(array[i])
                return True
    return False        
    
            

print(has_duplicates([4,2,23,4324,1,42,43,23]))
print(has_duplicates([4,2,23,4324,1,42,43,77,99,88,11]))
            
