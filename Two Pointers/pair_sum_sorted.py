def pair_sum_sorted(list, target):
    left, right = 0, len(list) - 1
    while left < right:
        sum = list[left] + list[right]
        if sum < target:
            left += 1
        elif sum > target:
            right -= 1
        else:
            return [left, right] # returning positions of the pair
    return [] # if no pair found

list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 10
print(pair_sum_sorted(list, target))