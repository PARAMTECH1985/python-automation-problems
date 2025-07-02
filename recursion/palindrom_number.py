'''
Let's say number is 123.
Step 1: 123 % 10 is 3. len(str(123)) is 3, so 10 ** (3 - 1) is 100. 3 * 100 is 300.
Step 2: The function recursively calls reverse_number_recursion(123 // 10), which is reverse_number_recursion(12).
Step 3 (within the recursion): 12 % 10 is 2. len(str(12)) is 2, so 10 ** (2 - 1) is 10. 2 * 10 is 20.
Step 4 (within the recursion): The function recursively calls reverse_number_recursion(12 // 10), which is reverse_number_recursion(1).
Step 5 (within the recursion): 1 % 10 is 1. len(str(1)) is 1, so 10 ** (1 - 1) is 1. 1 * 1 is 1.
Step 6 (within the recursion): The function recursively calls reverse_number_recursion(1 // 10), which is reverse_number_recursion(0).
Step 7 (base case): The base case of the recursion is when the number is 0, and it returns 0.
Step 8 (returning up the recursion): The function returns: 1 + 20 + 300 = 321.
'''


def reverse_number_recursion(number):
    if number == 0:
        return 0
    else:
        # original_number = number
        # reverse_number = 0
        # if original_number == number:
        #     reverse_number = (number%10) * 10**(len(str(number))-1) + reverse_number_recursion(number // 10)  #0+3=3,
        #else:
        #     reverse_number = (number%10) * 10**(len(str(number))-1) + reverse_number_recursion(number // 10)  # 0+3=3,
        # print(number)
        # print(reverse_number)
        # number //= 10
        # print(type(number))
        #     return (number%10) * 10*(len(str(number))-1) + reverse_number_recursion(number // 10)
        digit = number % 10
        length = len(str(number))
        # return (number % 10) * 10 ** (len(str(number)) - 1) + reverse_number_recursion(number // 10)
        return digit * 10 ** (length - 1) + reverse_number_recursion(number // 10)


def is_palindrom_number(number, reverse_number):
    if (number == reverse_number):
        return True
    else:
        return False


number = 1331
reverse_number = reverse_number_recursion(number)
print(is_palindrom_number(number, reverse_number))
