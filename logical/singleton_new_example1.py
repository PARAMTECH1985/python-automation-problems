class SingleToneNewExample:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            print("Instance is Not Created")
            cls._instance = super().__new__(cls)
        return cls._instance

    def get_details(self):
        return "Rinkoo Kushwah"


a1 = SingleToneNewExample()
a2 = SingleToneNewExample()
a3 = SingleToneNewExample()
print(a1 is a2)
print(a2 is a3)
print(a3 is a1)
print(a1.get_details())
print(a2.get_details())
print(a3.get_details())
