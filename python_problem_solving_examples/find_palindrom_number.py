#Reverse Number//Armstrong Number
def is_palindrome_math(num):
    """Checks if a number is a palindrome by reversing it mathematically."""
    if num < 0:
        return False
    original = num
    reversed_num = 0
    while num != 0:
        digit = num % 10
        print("Digit="+str(digit))
        reversed_num = reversed_num * 10 + digit
        print("Reverse_Number="+str(reversed_num))
        num //= 10
    return original == reversed_num


# Example usage
number = int(input("Enter a number: "))
if is_palindrome_math(number):
    print(f"{number} is a palindrome.")
else:
    print(f"{number} is not a palindrome.")


# Reverse of the number should be same of the actual number-palindrom-number