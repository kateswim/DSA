def count_expressions(numbers, target_result):
    def count(index, current_result):
        if index == len(numbers):
            if current_result == target_result:
                return 1
            else:
                return 0
            
        count_add = count(index+1, current_result + numbers[index])
        count_sub = count(index+1, current_result - numbers[index])

        print(f"Index: {index}, Current Result: {current_result}, Count Add: {count_add}, Count Sub: {count_sub}")

        return count_add + count_sub
        

    index = 0 # left 0 index not 1 like in the book
    current_result = numbers[0]
    return count(index, current_result)

numbers = [1, 2, 3, 4]
print(count_expressions(numbers, target_result=3))