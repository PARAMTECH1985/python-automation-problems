# Python program to demonstrate
# stack implementation using a linked list.
# node class

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    # Initializing a stack.
    # Use a dummy node, which is
    # easier for handling edge cases.
    def __init__(self):
        self.head = Node("Head")
        self.size = 0

    # String representation of the stack
    def __str__(self):
        cur = self.head.next
        out = ""
        while cur:
            out += str(cur.value) + "->"
            cur = cur.next
        return out[:-2]

    # Get the current size of the stack
    def getSize(self):
        return self.size

    # Check if the stack is empty
    def isEmpty(self):
        return self.size == 0

    # Get the top item of the stack
    def peek(self):

        # Sanitary check to see if we
        # are peeking an empty stack.
        if self.isEmpty():
            return None

        return self.head.next.value

    # Push a value into the stack.
    def push(self, value):
        node = Node(value)
        node.next = self.head.next  # Make the new node point to the current head
        self.head.next = node  #!!! # Update the head to be the new node
        self.size =self.size+ 1

    # Remove a value from the stack and return.
    def pop(self):
        if self.isEmpty():
            raise Exception("Popping from an empty stack")
        remove = self.head.next
        self.head.next = remove.next  #!!! changed
        self.size =self.size-1
        return remove.value


# Driver Code
if __name__ == "__main__":
    stack = Stack()
    for i in range(1, 11):
        stack.push(i)
    print(f"Stack: {stack}")

    for _ in range(1, 2):
        top_value = stack.pop()
        print(f"Pop: {top_value}")  # variable name changed
    print(f"Stack: {stack}")
