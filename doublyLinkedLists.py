# Node Class
class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Printing List
    def print_list(self):
        temp = self.head

        while temp is not None:
            print(temp.data, end="")
            if temp.next is None:
                last = temp
            temp = temp.next

        print("")

    # Inserting a node at the beginning of the List
    def add_in_beginning(self, val):
        new_node = Node(val)

        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    # Inserting Node at the end of the List
    def add_in_end(self, val):
        new_node = Node(val)

        if self.head is None:
            self.head = new_node
        else:
            last = self.head

            while last.next is not None:
                last = last.next

            last.next = new_node
            new_node.prev = last

    # Searching for a Node in the Doubly Linked List
    def search(self, key):
        temp = self.head

        while temp is not None:
            if temp.data is key:
                return True
            temp = temp.next

        return False

    # Deleting a Node in a Doubly Linked List
    def delete(self, key):
        temp = self.head

        while temp is not None and temp.data is not key:
            temp = temp.next

        if temp is None:
            return "Key not found"
        elif temp is self.head:
            self.head = self.head.next
            self.head.prev = None
        elif temp.next is None:
            temp.prev.next = None
        else:
            temp.prev.next = temp.next
            temp.next.prev = temp.prev


# Execution
llist = LinkedList()
llist.head = Node(4)
llist.add_in_end(5)
llist.add_in_beginning(3)
llist.add_in_beginning(2)
llist.add_in_beginning(1)
llist.print_list()
print(llist.search(5))
print(llist.search(2))
print(llist.search(7))
llist.delete(1)
llist.print_list()
