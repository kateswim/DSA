import time

# just stupid repetitive recursion
def rfib(n):
    if n ==0:
        return 0
    elif n==1:
        return 1
    return rfib(n-1) + rfib(n-2)

dict = {}

#fib with memoization / dynamic programming
def fib(n):
    global dict
    if n ==0:
        return 0
    elif n==1:
        return 1
    n1 = n-1
    n2 = n-2
    if n1 in dict:
        n1value = dict[n1] 
    else:
        n1value = fib(n-1)
        dict[n1]=n1value
    
    if n2 in dict:
        n2value = dict[n2]
    else:
        n2value = fib(n-2)
        dict[n2]=n2value
    return n1value + n2value

start_time = time.time()
print(fib(40))
print("faster--- %s seconds ---" % (time.time() - start_time))



start_time = time.time()
print(rfib(40))
print("slower--- %s seconds ---" % (time.time() - start_time))


