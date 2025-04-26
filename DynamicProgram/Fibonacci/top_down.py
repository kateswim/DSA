fibonacci_cache = {}

def fibonacci(n):
    if n <= 2:
        return 1
    if n not in fibonacci_cache:
        fibonacci_cache[n] = fibonacci(n-1) + fibonacci(n-2)
    return fibonacci_cache[n]

def fibo_list(numbers):
    result=[]
    for n in numbers:
        result.append(fibonacci(n))
    return result


print(fibo_list([6,12,13,23]))

def cached(f):
    cache={}
    def worker(*args):
        if args not in cache:
            cache[args]=f(*args)
        return cache[args]
    return worker
    
@cached
def fibonacci(n):
    if n <= 2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n):
    if n <= 2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)


