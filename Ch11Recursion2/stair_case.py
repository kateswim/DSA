def count_steps(n):
    if n ==0:
        return 0
    elif n==1:
        return 1
    elif n ==2:
        return 2
    elif n==3:
        return 4
    else:
        print(f"counting steps for n= {n}")
    return count_steps(n-1)+count_steps(n-2)+count_steps(n-3)
    
# print(count_steps(20))
# print(count_steps(11))
# print(count_steps(110))
print(f"steps for 6 are: {count_steps(6)}")    
print(f"steps for 11 are: {count_steps(11)}")    

    