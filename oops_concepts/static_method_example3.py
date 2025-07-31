# Python program to
# demonstrate static methods

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

        # a static method to check if a Person is adult or not.

    @staticmethod
    def isAdult(age):
        return age > 18


# Driver's code
if __name__ == "__main__":
    res = Person.isAdult(12)
    print('Is person adult:', res)

    res = Person.isAdult(22)
    print('\nIs person adult:', res)