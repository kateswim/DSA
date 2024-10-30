def binary_search(array, search_value):
    lower_bound=0
    upper_bound=len(array)-1

    while lower_bound<=upper_bound:
        midpoint=(upper_bound+lower_bound)//2
        value_midpoint=array[midpoint]

        if search_value==value_midpoint:
            return midpoint
        elif search_value<value_midpoint:
            upper_bound=midpoint-1
        elif search_value>value_midpoint:
            lower_bound=midpoint+1

    return None

# remember list should be sorted.
mylist = [4, 11, 22, 24, 56, 434, 543, 2345]
print(binary_search(mylist,24))
print(binary_search(mylist,33))
