def contains_char(string, counter:int =0):
    if len(string)==0:
        return 0
    elif string[0]=='x':
        return counter
    else:
        return contains_char(string[1:], counter+1)
    
print(contains_char('afghsfthjsxpogxjkxkjhxo'))
    

    