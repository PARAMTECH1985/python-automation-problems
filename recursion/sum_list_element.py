def sum_list(data):
    # Base case: empty list has a sum of 0
    if not data:
        return 0
    # Recursive case: sum of first element + sum of rest of the list
    else:
        return data[0] + sum_list(data[1:])


my_list = [1, 2, 3, 4, 5]
print(sum_list(my_list))  # Output: 15
