def fibonacci(n):
    prev=1
    curr=1
    for i in range(n-2): # range means how many steps to calculate, we have 2 first numbers, so n-2 steps
        next=prev+curr
        prev,curr=curr,next
    return curr

print(fibonacci(10))  