class Singleton:
    _instance = None
    _initialized = False

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, value=None):
        if not self._initialized:
            self.value = value
            self._initialized = True
            print(f"Singleton initialized with value: {self.value}")
        else:
            print("Singleton already initialized. Skipping __init__.")


# First instantiation (initializes the singleton)
s1 = Singleton("Initial Value")
# Second instantiation (returns the same instance, skips re-initialization)
s2 = Singleton("New Value")
# Verify that both variables refer to the same instance and the value is from the first initialization
print(f"s1 is s2: {s1 is s2}")
print(f"s1.value: {s1.value}")
print(f"s2.value: {s2.value}")