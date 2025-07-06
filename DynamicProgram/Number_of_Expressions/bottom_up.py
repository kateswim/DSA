import collections

def count_expressions(numbers, target_result):
    index = 1
    current_result_count = collections.Counter({numbers[0] : 1})

    while index < len(numbers):
        next_result_count = collections.Counter()

        for prefix_result, count in current_result_count.items():
            new_result_add = prefix_result + numbers[index]
            new_result_sub = prefix_result - numbers[index]

            next_result_count[new_result_add] += count
            next_result_count[new_result_sub] += count

        current_result_count = next_result_count
        index += 1
        print(f"Index: {index}, Current Result Count: {current_result_count}")


    return current_result_count[target_result]
              
numbers = [1, 2, 3, 4]
print(count_expressions(numbers, target_result=3))
