def factorial(n):
   if n == 0 or n == 1:
       return 1
   else:
        return n * factorial(n - 1)

# Example usage:
num = 5
print(f"The factorial of {num} is: {factorial(num)}")

num_zero = 0
print(f"The factorial of {num_zero} is: {factorial(num_zero)}")