class Singleton:
    _instance = None  # Class-level variable to store the single instance

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


# Example usage:
s1 = Singleton()
s2 = Singleton()
print(s1 is s2)  # Output: True (both variables refer to the same instan
