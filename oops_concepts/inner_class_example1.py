class OuterClass:
    def __init__(self, outer_value):
        self.outer_value = outer_value
        self.inner_instance = self.InnerClass(outer_value * 2)  # Instantiate inner class

    class InnerClass:
        def __init__(self, inner_value):
            self.inner_value = inner_value

        def display_inner_value(self):
            print(f"Inner value: {self.inner_value}")

    def display_values(self):
        print(f"Outer value: {self.outer_value}")
        self.inner_instance.display_inner_value()


# Usage
outer_obj = OuterClass(10)
outer_obj.display_values()
