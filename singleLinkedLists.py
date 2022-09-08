# Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Creating a Singly Linked List
class LinkedList:
    def __init__(self):
        self.head = None

    # Adding a node at the beginning of the linked list
    def add_at_beginning(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    # Adding a node at the end of the linked list
    def add_at_ending(self, val):
        new_node = Node(val)

        if self.head is None:
            self.head = new_node
        else:
            last_node = self.head

            while last_node.next:
                last_node = last_node.next

            last_node.next = new_node

    # Searching for a node in singly linked list
    def search(self, key):
        temp = self.head

        while temp is not None:
            if temp.data is key:
                return True
            temp = temp.next

        return False

    # Deleting a node in singly linked list
    def delete(self, key):
        if self.head.data is key:
            self.head = self.head.next
        else:
            temp = self.head

            while temp is not None:
                if temp.next.data is key:
                    temp.next = temp.next.next
                    break
                else:
                    temp = temp.next
