def unique_paths(n,k):
    if n==1 or k==1:
        return 1
    else:
        return unique_paths(n-1,k)+unique_paths(n,k-1)


print(unique_paths(6,5))
print(unique_paths(7,8))