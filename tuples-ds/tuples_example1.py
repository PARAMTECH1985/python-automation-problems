'''

A tuple in Python is an ordered collection of items, similar to a list, but with a key distinction:
immutability. This means that once a tuple is created, its elements cannot be changed, added, or removed.
This code will not work because:

Tuples don't have an append() method. You can't add items to a tuple.
Tuples don't have a remove() method. You can't remove items from a tuple.
Trying to access an element that doesn't exist (like my_tuple[2] if the tuple only has two elements) will cause an error.
https://www.linkedin.com/pulse/25-python-tuple-questions-solution-mrityunjay-pathak/
'''

first_names = ('Simon', 'Sarah', 'Mehdi', 'Fatime')
last_names = ('Sinek', 'Smith', 'Lotfinejad', 'Lopes')
ages = (49, 55, 39, 33)
zipped = zip(first_names, last_names, ages)
print(zipped)
customers = tuple(zipped)
print(customers)

coordinates = (10, 20)
x, y = coordinates
print(f"X: {x}, Y: {y}")

coordinates = (10, 20, 30)
x, y, z = coordinates
print(f"X: {x}, Y: {y}, Z: {z}")

numbers = (1, 2, 3, 4, 5, 6)
print(numbers[1:4])  # Output: (2, 3, 4)
print(numbers[:3])  # Output: (1, 2, 3)
print(numbers[4:])  # Output: (5, 6)

my_tuple = ("red", "green", "blue")
print(my_tuple[0])  # Output: red
print(my_tuple[1])  # Output: green
print(my_tuple[2])  # Output: blue

mixed_tuple = ("apple", 10, True, 3.14)
print(mixed_tuple)

my_tuple = (1, 2, 3, 4, 5)
element_to_check = 3

if element_to_check in my_tuple:
    print(f"{element_to_check} is in the tuple")
else:
    print(f"{element_to_check} is not in the tuple")

my_tuple = ("apple", "banana", "cherry")

for fruit in my_tuple:
    print(fruit)

my_tuple = (10, 20, 30, 40, 50, 60)

# Slicing to get elements from index 1 to 3 (exclusive)
sliced_tuple = my_tuple[1:4]
print(sliced_tuple)  # Output: (20, 30, 40)

nested_tuple = ((1, 2), (3, 4), (5, 6))
print(nested_tuple)

student_data = {
    (123, "Alice"): {"age": 20, "major": "Computer Science"},
    (456, "Bob"): {"age": 22, "major": "Engineering"}
}

print(student_data[(123, "Alice")])


def manipulate_tuple(my_tuple):
    # my_tuple.append(4)  # This will cause an error
    # my_tuple.remove(1)  # This will also cause an error
    print("Third element:", my_tuple[2])


my_tuple = (1, 2, 3)
manipulate_tuple(my_tuple)

my_tuple = (1, 2, 2, 3, 2, 4, 5, 2)
print("Length of the tuple:", len(my_tuple))  # Output: 8
print("Number of 2s in the tuple:", my_tuple.count(2))  # Output: 4


# Solution 1:
def tuple_length(tup):
    return len(tup)

# Solution 2:
tup = (1, 2, 3, 4, 5)
length = len(tup)
print(length)  # Output: 5


# Solution 1:
def concatenate_tuples(tup1, tup2):
    return tup1 + tup2

# Solution 2:
tup1 = (1, 2, 3)
tup2 = (4, 5, 6)
result = tup1 + tup2
print(result)  # Output: (1, 2, 3, 4, 5, 6)

# Solution 1:
def access_element(tup, index):
    return tup[index]

# Solution 2:
tup = (10, 20, 30, 40, 50)
element = tup[2]
print(element)  # Output: 30


# Solution 1:
def count_element(tup, value):
    return tup.count(value)

# Solution 2:
tup = (1, 2, 2, 3, 2, 4, 2)
count = tup.count(2)
print(count)  # Output: 4

# Solution 1:
def element_exists(tup, value):
    return value in tup

# Solution 2:
tup = (10, 20, 30, 40, 50)
exists = 30 in tup
print(exists)  # Output: True

# Solution 1:
def tuple_to_string(tup):
    return str(tup)

# Solution 2:
tup = (1, 2, 3)
string = str(tup)
print(string)  # Output: "(1, 2, 3)"


# Solution 1:
def find_index(tup, value):
    return tup.index(value)

# Solution 2:
tup = (10, 20, 30, 40, 50)
index = tup.index(30)
print(index)  # Output: 2

# Solution 1:
def list_to_tuple(lst):
    return tuple(lst)

# Solution 2:
lst = [1, 2, 3, 4, 5]
tup = tuple(lst)
print(tup)  # Output: (1, 2, 3, 4, 5)

# Solution:
tup = (10, 20, 30, 40, 50)
for element in tup:
    print(element)

# Solution:
def max_min_elements(tup):
    return max(tup), min(tup)

tup = (5, 8, 2, 10, 3)
max_element, min_element = max_min_elements(tup)
print("Max:", max_element)  # Output: Max: 10
print("Min:", min_element)  # Output: Min: 2


# Solution:
def tuple_to_single_string(tup):
    return ''.join(tup)

tup = ('H', 'e', 'l', 'l', 'o')
result = tuple_to_single_string(tup)
print(result)  # Output: "Hello"

# Solution:
def remove_element(tup, value):
    return tuple(x for x in tup if x != value)

tup = (1, 2, 3, 4, 3, 5)
new_tup = remove_element(tup, 3)
print(new_tup)  # Output: (1, 2, 4, 5)


# Solution:
def common_elements(tup1, tup2):
    return tuple(x for x in tup1 if x in tup2)

tup1 = (1, 2, 3, 4)
tup2 = (3, 4, 5, 6)
common = common_elements(tup1, tup2)
print(common)  # Output: (3, 4)


# Solution:
def sort_tuple(tup):
    return tuple(sorted(tup))

tup = (5, 3, 8, 1, 2)
sorted_tup = sort_tuple(tup)
print(sorted_tup)  # Output: (1, 2, 3, 5, 8)


# Solution:
def sum_tuple(tup):
    return sum(tup)

tup = (1, 2, 3, 4, 5)
total = sum_tuple(tup)
print(total)  # Output: 15


# Solution:
def merge_and_remove_duplicates(tup1, tup2):
    return tuple(set(tup1).union(tup2))

tup1 = (1, 2, 3)
tup2 = (3, 4, 5)
result = merge_and_remove_duplicates(tup1, tup2)
print(result)  # Output: (1, 2, 3, 4, 5)


# Solution:
def first_last_elements(tup):
    return tup[0], tup[-1]

tup = (10, 20, 30, 40, 50)
first, last = first_last_elements(tup)
print("First:", first)  # Output: First: 10
print("Last:", last)    # Output: Last: 50



# Solution:
def int_to_str_tuple(tup):
    return tuple(str(x) for x in tup)

tup = (1, 2, 3, 4, 5)
str_tup = int_to_str_tuple(tup)
print(str_tup)  # Output: ('1', '2', '3', '4', '5')


# Solution:
def product_tuple(tup):
    product = 1
    for x in tup:
        product *= x
    return product

tup = (1, 2, 3, 4, 5)
result = product_tuple(tup)
print(result)  # Output: 120


# Solution:
def second_largest(tup):
    sorted_tup = sorted(tup)
    return sorted_tup[-2]

tup = (10, 5, 8, 20, 15)
second_largest_element = second_largest(tup)
print(second_largest_element)  # Output: 15


# Solution:
def is_subset(sub, main):
    return all(x in main for x in sub)

main_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9)
sub_tuple = (2, 4, 6)
result = is_subset(sub_tuple, main_tuple)
print(result)  # Output: True