import time

def add_until_100(array):
    if len(array)==0:
        return 0
    max_sum=add_until_100(array[1:])
    
    if array[0]+max_sum>100:
        return max_sum
    else:
        return array[0]+max_sum
    

start_time = time.time()

print(add_until_100([3,67,6,0,9,2,9,23,4,9]))
print("faster--- %s seconds ---" % (time.time() - start_time))