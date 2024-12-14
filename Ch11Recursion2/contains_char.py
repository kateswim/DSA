# def contains_char(string, counter:int =0):
#     if len(string)==0:
#         return 0
#     elif string[0]=='x':
#         return counter
#     else:
#         return contains_char(string[1:], counter+1)
    
# print(contains_char('afghsfthjsxpogxjkxkjhxo'))


def contains_char(string):
    if len(string)==0:
        return 0
    elif string[0]=='x':
        return 0
    else:
        print(f"string= {string[1:]}  counter: +1")
        return contains_char(string[1:]) +1
    
print(contains_char('afghsfthjsxpogxjkxkjhxo'))

    