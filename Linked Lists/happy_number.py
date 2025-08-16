def happy_number(n: int):
    slow = fast = n

    while True:
        slow = get_next_num(slow)
        fast = get_next_num(get_next_num(fast))
        if fast == 1:
            return True
        elif fast == slow:
            return False
        
def get_next_num(x: int): 
    next_num = 0
    
    while x > 0:
        digit = x % 10
        x //= 10 # calculates the result and updates x with that value

        next_num += digit ** 2

    return next_num       


print(happy_number(19))  # True
print(happy_number(2))   # False
print(happy_number(7))   # True