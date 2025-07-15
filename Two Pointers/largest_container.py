def largest_container(heights: list[int]):
    max_water = 0
    left, right = 0, len(heights)-1
    while left < right: 
        water = min(heights[left], heights[right]) * (right - left)
        max_water = max(max_water, water)

        if heights[left] < heights[right]:
            left += 1

        elif heights[left] > heights[right]:
            right -= 1

        else:
            left += 1 # we move both inside if they are at same level (same value), because if next number is bigger we still will consider smaller 
            right -= 1

    return max_water


heights = [2, 7, 8, 3, 7, 6]
heights = []
heights = [1]

print(largest_container(heights))