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

    def insert_node_link_list(self, current_node, data):
        new_node = Node(data)
        current_node.next = new_node
        return new_node


class LinkList:
    def __init__(self):
        self.head = None

    def insert_node_link_list_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node

    def remove_node(self, index):
        current_node = self.head
        position = 0
        while current_node is not None and current_node.next is not None and position + 1 != index:
            position += 1
            current_node = current_node.next

        if current_node is not None and current_node.next is not None:
            current_node.next = current_node.next.next
        else:
            print("Index not present")

    def insert_node_link_list_at_given_index(self, index, data):
        if self.head is None:
            self.head = Node(data)
            return
        position = 0
        current_node = self.head
        while current_node is not None and (position + 1) != index:
            print("Position Value=" + str(position))
            print(current_node.data)
            position = position + 1
            current_node = current_node.next
            if current_node is not None and (position + 1) == index:
                print("Index and Position Values are Same")
                new_node = Node(data)
                new_node.next = current_node.next
                current_node.next = new_node
            else:
                print("Given Index Not Found")

    def printLinkListData(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" ->")
            current_node = current_node.next

    def search_element(self,head_node, key):
        current = head_node.next
        while current:
            if current.data == key:
                print("Item Found")
                return True
            current = current.next
        return False

list = LinkList()
list.insert_node_link_list_at_end(10)
list.insert_node_link_list_at_end(20)
list.insert_node_link_list_at_end(30)
list.insert_node_link_list_at_end(40)
list.insert_node_link_list_at_end(50)
list.insert_node_link_list_at_end(60)
list.insert_node_link_list_at_end(70)
list.printLinkListData()
list.insert_node_link_list_at_given_index(3, 100)
list.insert_node_link_list_at_given_index(7, 1000)
list.printLinkListData()
list.remove_node(3)
print("\n")
list.printLinkListData()

# print(list.search_element(Node(10),100))


