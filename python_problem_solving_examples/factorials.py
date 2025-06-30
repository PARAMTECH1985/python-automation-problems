fact = 1
number = int(input("Enter a number: "))
while number > 0:
    fact = number * fact
    number = number - 1
print(fact)