def intersection(small_array,big_array):
    table={}
    for i in big_array:
        table[i]=True

    print(table)

    for j in small_array:
        if table[j]:
            print(j)

    return table

intersection([1,2,3],[1,2,3,4,5,6])

