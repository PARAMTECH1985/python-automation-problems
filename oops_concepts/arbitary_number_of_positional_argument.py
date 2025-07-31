def sum_all(*numbers):
    print("Length is =" + str(len(numbers)))
    total = 0
    for num in numbers:
        total += num
    return total


print(sum_all(1, 2, 3))  # Output: 6
print(sum_all(10, 20, 30, 40))  # Output: 100
print(sum_all(10, 20, 30, 40, 50))  # Output: 150
