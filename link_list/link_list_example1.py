class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkListClass:
    def __init__(self):
        self.head = None

    def insert_data_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_index(self, data, index):
        if index == 0:
            self.insert_data_at_beginning(data)
            return
        position = 0
        current_node = self.head
        while current_node is not None and position + 1 != index:
            position = position + 1
            current_node = current_node.next
        if current_node is not None:
            new_node = Node(data)
            new_node.next = current_node.next
            current_node.next = new_node

    def insert_data_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node

    def remove_first_node(self):
        if self.head is None:
            return
        self.head = self.head.next

    def remove_last_node(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            return
        current_node = self.head
        while current_node.next and current_node.next.next:
            current_node = current_node.next
        current_node.next = None

    def remove_at_given_index(self, index):
        if self.head is None:
            return
        if index == 0:
            self.remove_first_node()
            return
        current_node = self.head
        position=0
        while current_node is not None and current_node.next is not None and position+1!=index:
            current_node = current_node.next
            position=position+1
        if current_node is not None and current_node.next is not None:
            current_node=current_node.next

    def updateNode(self, data, index):
        current_node = self.head
        position = 0
        while current_node is not None and position != index:
            position += 1
            current_node = current_node.next

        if current_node is not None:
            current_node.data = data
        else:
            print("Index not present")

    # Method to remove first node of linked list
    def printLL(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def remove_node(self, data):
        current_node = self.head
        # If the node to be removed is the head node
        if current_node is not None and current_node.data == data:
            self.remove_first_node()
            return

        # Traverse and find the node with the matching data
        while current_node is not None and current_node.next is not None:
            if current_node.next.data == data:
                current_node.next = current_node.next.next
                return
            current_node = current_node.next

        # If the data was not found
        print("Node with the given data not found")

ll_object = LinkListClass()
ll_object.insert_data_at_beginning(10)
ll_object.insert_data_at_beginning(20)
ll_object.insert_data_at_beginning(30)
ll_object.insert_data_at_beginning(40)
ll_object.printLL()
print("List When All the Element Added First")
ll_object.insert_data_at_end(50)
ll_object.insert_data_at_end(60)
ll_object.insert_data_at_end(70)
ll_object.insert_data_at_end(80)
ll_object.printLL()
print("List When All the Element Added Last")
ll_object.remove_first_node()
ll_object.printLL()
print("List After Removing the First Node")
ll_object.insert_at_index(110, 5)
ll_object.printLL()
print("List After Inserting Element in the Given Index")
ll_object.remove_last_node()
ll_object.printLL()
print("List After Removing Last Element from the List")
ll_object.remove_at_given_index(4)
ll_object.printLL()
print("List After Removing 4th Element from the List")

ll_object.remove_node(110)
ll_object.printLL()
print("List After Removing 110 from the List")
ll_object.updateNode(200,0)
ll_object.printLL()
print("List After Updating the List")