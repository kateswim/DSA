def pair_sum_unsorted(nums: list[int], target: int):
    hashmap = {}
    for i, x in enumerate(nums): # enumerate library that lets loop through index and value in array
        if target - x in hashmap:
            return [hashmap[target-x], i]
        
        hashmap[x] = i

    return []

nums = [-1, 3, 4, 2, -6, 8]
print(pair_sum_unsorted(nums, target = 3))        