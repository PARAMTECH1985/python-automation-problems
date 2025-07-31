class MyClass:
   class_variable = "I am a class variable"  # This is a class variable

   def __init__(self, instance_variable):
       self.instance_variable = instance_variable  # This is an instance variable

# Accessing the class variable
print(MyClass.class_variable)  # Output: I am a class variable

# Creating instances
obj1 = MyClass("Instance 1 data")
obj2 = MyClass("Instance 2 data")

# Accessing the class variable through instances
print(obj1.class_variable)  # Output: I am a class variable
print(obj2.class_variable)  # Output: I am a class variable

# Modifying the class variable
MyClass.class_variable = "New value for class variable"

# Observe the change in all instances
print(obj1.class_variable)  # Output: New value for class variable
print(obj2.class_variable)  # Output: New value for class variable
