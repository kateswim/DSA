def triplet_sum(list):
    list.sort()
    triplets = []
    for i in range(len(list)):
        if list[i] > 0: # means that if first number positive (> 0) others also positive in sorted list
            break
        if i > 0 and list[i] == list[i-1]: # current number is same as previous
            continue
        pairs = pair_sum_sorted(list, i+1, -list[i])

        for pair in pairs:
            triplets.append(list[i] + pair)
        
    return triplets

def pair_sum_sorted(list, start:int, target:int):
    pairs = []
    left, right = 0, len(list)-1
    while left < right:
        sum = list[left] + list[right]
        if sum < target: 
            left+=1
        elif sum > target:
            right -=1
        else:
            while left < right and list[left] == list[left-1]:
                left +=1
                pairs.append([list[left], list[right]])

    return pairs

list = [-1, 0, 1, 2, -1, -4]
print(triplet_sum(list)) 