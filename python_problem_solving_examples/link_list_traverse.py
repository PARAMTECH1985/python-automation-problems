"""
This program covers-
0.Initialize the Link List
1.Traverse the Link List
2.Print the Max Value in the Link List
3.Print the Min Value in the Link List
4.Search Item in the Link List
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def traverse_and_print(head):
    currentNode = head
    while currentNode:
        print(currentNode.data, end=" -> ")
        currentNode = currentNode.next
    print("null")


def find_lowest_value(head):
    minValue = head.data
    currentNode = head.next
    while currentNode:
        if currentNode.data < minValue:
            minValue = currentNode.data
        currentNode = currentNode.next
    return minValue


def find_max_value(head):
    maxValue = head.data
    currentNode = head.next
    while currentNode:
        if currentNode.data > maxValue:
            maxValue = currentNode.data
        currentNode = currentNode.next
    return maxValue


def search_element(head, key):
    current = head.next
    while current:
        if current.data == key:
            print("Item Found")
            return True
        current = current.next
    return False


node1 = Node(7)
node2 = Node(11)
node3 = Node(3)
node4 = Node(2)
node5 = Node(9)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

traverse_and_print(node1)
print("Minimnum Value of the List=" + str(find_lowest_value(node1)))
print("Maximum Value of the List=" + str(find_max_value(node1)))
print("Item Found="+str(search_element(node1, 9)))
