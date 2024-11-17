def non_duplicates(s):
    table={}
    non_duplicates=[]

    for i in s:
        table[i]=table.get(i,0)+1 #put 0 for i first time

    for char, count in table.items():
        if count==1:
            non_duplicates.append(char)


print(non_duplicates('minimum'))
            