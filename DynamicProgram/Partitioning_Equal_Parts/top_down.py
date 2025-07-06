from functools import lru_cache

def can_partition(numbers):
    @lru_cache(maxsize = None)

    def find_subset(index, target_sum):
        if target_sum == 0:
            return True
        if target_sum < 0 or index >= len(numbers):
            return False
        
        number = numbers[index]

        return(find_subset(index + 1, target_sum - number)) or (find_subset(index + 1, target_sum))
    
    total = sum(numbers)
    if total % 2:
        return False
    
    return find_subset(0, total // 2)

numbers = [1, 6, 11, 5]
print(can_partition(numbers))