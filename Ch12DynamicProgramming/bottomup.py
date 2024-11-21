def fib(n):
    if n==0:
        return 0
    a = 0 #first fibonacci #second last
    b = 1 #second fibonacci #first last
    # 3rdfibo = first last + second last
    print(f"a : {a}")
    print(f"b : {b}")
    for i in range(1,n):
        temp = a #second last
        a = b    # first last
        b = a + temp
        print(f"a : {temp}")
        print(f"b : {a}")
    return b

n = 6
print(f"fib({n}) :  {fib(n)}")

