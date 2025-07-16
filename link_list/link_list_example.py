'''
Basic Link List Example
'''


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def list_is_empty(self):
        return not self.head

    def return_first(self):
        if self.list_is_empty():
            print("List is Empty")
            return
        return self.head.value

    def return_last(self):
        if self.list_is_empty():
            print("List is Empty")
            return
        last_node = self.head
        while last_node.next is not None:
            last_node = last_node.next
        return last_node.value

    def insert_at_beginning(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        return

    def traverse_link_list(self, head):
        current_node = head
        while current_node is not None:
            print(current_node.value, end=" ->")
            current_node = current_node.next
        print("\n")


if __name__ == '__main__':
    my_linked_list = LinkedList()
    my_linked_list.insert_at_beginning(10)
    my_linked_list.insert_at_beginning(20)
    my_linked_list.insert_at_beginning(30)
    my_linked_list.insert_at_beginning(40)
    my_linked_list.insert_at_beginning(50)
    my_linked_list.insert_at_beginning(60)
    # my_linked_list.print_link_list_elements(my_linked_list)
    my_linked_list.traverse_link_list(Node(10))
