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

    def traverse_link_list(self, head_node):
        current_node = head_node
        while current_node is not None:
            print(current_node.data, end=" ->")
            current_node = current_node.next
        print("\n")


node1 = Node(7)
node2 = Node(11)
node3 = Node(3)
node4 = Node(2)
node5 = Node(9)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node1.traverse_link_list(node1)
node2.traverse_link_list(node2)
node3.traverse_link_list(node3)
node4.traverse_link_list(node4)
node5.traverse_link_list(node5)
