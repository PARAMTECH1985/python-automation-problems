class Calculator:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b


# Calling static methods without creating an instance
result_add = Calculator.add(5, 3)
print(f"Addition result: {result_add}")

result_multiply = Calculator.multiply(4, 2)
print(f"Multiplication result: {result_multiply}")

result_add = Calculator.add(5, 3)
print(f"Addition result: {result_add}")

result_multiply = Calculator.multiply(4, 2)
print(f"Multiplication result: {result_multiply}")
