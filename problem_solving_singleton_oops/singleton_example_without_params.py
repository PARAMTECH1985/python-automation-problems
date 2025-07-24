class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
            # Initialization code here
        return cls._instance

    def some_method(self):
        print("Singleton method called")


# Example usage:
singleton1 = Singleton()
singleton2 = Singleton()
print(singleton1)
print(singleton2)
print(singleton1 is singleton2)  # Output: True
