def armstrong_number_recursion(number,length, sum=0):
    if number == 0:
        return sum
    else:
        digit = number % 10
        sum = sum + digit ** (length)
        print(sum)
        return armstrong_number_recursion(number // 10, length, sum)
def is_armstrong(original_num):
    n = len(str(original_num))
    calculated_sum = armstrong_number_recursion(original_num, n)
    return original_num == calculated_sum


number = 9474
print(is_armstrong(number))
