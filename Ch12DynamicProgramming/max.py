import time

# start_time = time.time()

# print("--- %s seconds ---" % (time.time() - start_time))

no_of_calculation = 0

# max with recursion (not optimized)
def max(array):
    global no_of_calculation
    if len(array) ==1:
        return array[0]
    if array[0] > max(array[1:]):
        #print("first calculation")
        no_of_calculation +=  1
        return array [0]
    else:
        #print("second calculation")
        no_of_calculation += 1
        return max(array[1:])
    
# max with recursion with memoization
def smart_max(array):
    global no_of_calculation
    if len(array) ==1:
        return array[0]
    max_calculation= smart_max(array[1:])
    no_of_calculation += 1
    #print("all calculation done here")
    if array[0] > max_calculation:
        return array [0]
    else:
        return max_calculation
    
array = [1,2,3,4,5,77,8,9,10,23,543,2,4,2,4,5]
#array = [0,1,2,3,4]


start_time = time.time()
max(array)
print("--- %s seconds ---" % (time.time() - start_time))
print(f"total no of calls: {no_of_calculation}")

print()

no_of_calculation = 0
start_time = time.time()
smart_max(array)
print("smart timer:--- %s seconds ---" % (time.time() - start_time))
print(f"total no of calls when done smartly: {no_of_calculation}")