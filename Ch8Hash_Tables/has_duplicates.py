def hasDuplicateString(array):
    table={}
    duplicates=[]
    
    for i in array:
        if i in table:
            duplicates.append(i)
        
        else:
            table[i]=1
    
    return duplicates




print(hasDuplicateString(['a','b','v','g','d','a','f','s','p','q','r','p','g']))