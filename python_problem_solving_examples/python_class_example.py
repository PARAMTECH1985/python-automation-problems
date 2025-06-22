class Dog:
    # Class attribute
    species = "Canine"

    # Instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    def bark(self):
        return "Woof!"

# Creating instances of the Dog class (objects)
dog1 = Dog("Buddy", 3)
dog2 = Dog("Lucy", 5)

# Accessing attributes and methods
print(dog1.name)  # Output: Buddy
print(dog2.age)  # Output: 5
print(dog1.species)  # Output: Canine
print(dog1.bark())  # Output: Woof!
