class Singleton:
    _instance = None

    def __new__(cls, value, *args, **kwargs):
        if cls._instance is None:
            print("Creating new instance")
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self, value, *args, **kwargs):
        print(f"Initializing with value: {value}")
        super().__init__(*args, **kwargs)
        self.value = value


a = Singleton("A")
b = Singleton("B")
if a is b:
    print("Only Single Instance Created")
