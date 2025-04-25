def fibonacci(n):
    prev=1
    curr=1
    for i in range(n-2):
        next=prev+curr
        prev,curr=curr,next
    return curr

print(fibonacci(10))  