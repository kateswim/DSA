def count_str(array):
     for i in array:
        if len(i)==1:
            return 1
        else:
            return 1+count_str(i[1,])
        
print(count_str['ab','c','def','ghij'])
        
        