def count_str(array):
     if len(array)==0:
         return 0
     else: 
         return len(array[0])+ count_str(array[1:]) 
       
#can count length of each item in array (if it is strings)
     
print(count_str(['ab','c','def','ghij']))
