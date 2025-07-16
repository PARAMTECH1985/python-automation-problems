class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(type(self.name))
        print(type(self.age))

    def print(self):
        print(self.name)
        print(self.age)

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age


p1 = Person("Sadananda", 35)
print(p1.name)
print(p1.age)

print(p1.get_name())
print(p1.get_age())
p1.print()
