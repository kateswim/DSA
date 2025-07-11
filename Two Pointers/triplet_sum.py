def triplet_sum(nums:list):
    nums.sort()
    triplets = []
    for i in range(len(nums)):
        if nums[i] > 0: # means that if first number positive (> 0) others also positive in sorted list
            break
        if i > 0 and nums[i] == nums[i-1]: # current number is same as previous
            continue
        pairs = pair_sum_sorted(nums, i+1, -nums[i])

        for pair in pairs:
            triplets.append([nums[i]] + pair)
        
    return triplets

def pair_sum_sorted(nums:list, start:int, target:int):
    pairs = []
    left, right = start, len(nums)-1
    while left < right:
        sum = nums[left] + nums[right]

        if sum == target:
            pairs.append([nums[left], nums[right]])

            while left < right and nums[left] == nums[left+1]: # look ahead if b has duplicates after adding pair 
                left += 1
                print(nums[left])
            left += 1

        elif sum < target: 
            left += 1
        else:
            right -= 1

    return pairs


list = [-1, 0, 1, 2, -1, -4]
print(triplet_sum(list)) 