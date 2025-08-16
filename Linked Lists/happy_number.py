def happy_number(n: int):
    slow = fast = n

    while True:
        slow = get_next_num(slow)
        fast = get_next_num(get_next_num(fast))
        if fast == 1:
            return True
        elif fast == slow:
            return False
        
        