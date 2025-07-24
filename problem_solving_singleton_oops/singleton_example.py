class Singleton:
    _instance = None

    def __new__(cls, value):
        if cls._instance is None:
            print("Creating new instance")
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

    def __init__(self, value):
        print(f"Initializing with value: {value}")
        self.value = value


a = Singleton("A")
print(a.value)
b = Singleton("B")
print(b.value)
