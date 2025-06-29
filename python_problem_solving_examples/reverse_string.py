def reverse_string(s):
    stack = []

    # Push the characters into stack
    for char in s:
        stack.append(char)

    # Prepare a list to hold the reversed characters
    rev = [''] * len(s)

    # Pop the characters from stack into the reversed list
    for i in range(len(s)):
        rev[i] = stack.pop()

    # Join the list to form the reversed string
    return ''.join(rev)

str="India"
print(reverse_string(str))