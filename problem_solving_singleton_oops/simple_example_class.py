class Employee:
    #leaves = []
    def __init__(self, name):
        self.name = name
        self.leaves = []

    def apply_leave(self, day):
        self.leaves.append(day)

    def show_leaves(self):
        print(f"{self.name}'s leaves: {self.leaves}")


e1 = Employee("Alice")
e2 = Employee("Bob")

e1.apply_leave("2025-07-23")
e2.apply_leave("2025-07-24")

e1.show_leaves()
e2.show_leaves()

# Bob [2025-07-23,2025-07-24]
