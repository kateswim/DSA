def num_print(array):
    for i in array:
        if isinstance(i, list):
            num_print(i)
        else:
            print(i)

print(num_print([1,3,56,[2,8,90,6],6,[9,7,[45,[5,8,[5,8,[56,12,4,7],8,56],67],8],56,45,0],56]))
