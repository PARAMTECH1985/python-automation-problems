# Define a decorator function
'''
Syntax of Decorator Parameters
def decorator_name(func):
    def wrapper(*args, **kwargs):
        # Add functionality before the original function call
        result = func(*args, **kwargs)
        # Add functionality after the original function call
        return result
    return wrapper

@decorator_name
def function_to_decorate():
    # Original function code
    pass

Explanation of Parameters
1. decorator_name(func):

decorator_name: This is the name of the decorator function.
func: This parameter represents the function being decorated. When you use a decorator, the decorated function is passed to this parameter.
2. wrapper(*args, **kwargs):

wrapper: This is a nested function inside the decorator. It wraps the original function, adding additional functionality.
*args: This collects any positional arguments passed to the decorated function into a tuple.
**kwargs: This collects any keyword arguments passed to the decorated function into a dictionary.
The wrapper function allows the decorator to handle functions with any number and types of arguments.
3. @decorator_name:

This syntax applies the decorator to the function_to_decorate function. It is equivalent to writing function_to_decorate = decorator_name(function_to_decorate
'''


def decorator_name(func):
    def wrapper(*args, **kwargs):
        # Add functionality before the original function call
        result = func(*args, **kwargs)
        # Add functionality after the original function call
        return result

    return wrapper


@decorator_name
def function_to_decorate():
    # Original function code
    pass


def log_function_call(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function {func.__name__} with arguments {args} and keyword arguments {kwargs}")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} returned {result}")
        return result

    return wrapper


# Apply the decorator to a function
@log_function_call
def add(a, b):
    return a + b

# Call the decorated function
result = add(5, 3)
