def sum_of_elements(item, idx = 0):
    if idx == len(item):
        return 0
    value = item[idx] + sum_of_elements(item, idx + 1)
    return value

list_1 = [1, 2, 3, 4, 5]
print(f"Here is sum of the list {list_1} = {sum_of_elements(list_1)}")