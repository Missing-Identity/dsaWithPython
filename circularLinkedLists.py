class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    # Printing Circular Linked List
    def print_list(self):
        temp = self.head

        while True:
            print(temp.data, end="")
            temp = temp.next
            if temp is self.head:
                break

    # Inserting node in beginning of Circular Linked Lists
    def add_in_beginning(self, val):
        new_node = Node(val)

        if self.head is None:
            new_node.next = new_node
            self.head = new_node
        else:
            last_node = self.head

            while last_node.next is not self.head:
                last_node = last_node.next

            last_node.next = new_node
            new_node.next = self.head
            self.head = new_node

    # Inserting node at the end of Circular Linked Lists
    def add_in_end(self, val):
        new_node = Node(val)

        if self.head is None:
            new_node.next = new_node
            self.head = new_node
        else:
            last = self.head

            while last.next is not self.head:
                last = last.next

            last.next = new_node
            new_node.next = self.head

    # Searching a node in Circular Linked Lists
    def search(self, key):
        if self.head is None:
            return False
        temp = self.head

        while True:
            if temp.data is key:
                return True
            temp = temp.next
            if temp is self.head:
                break

        return False

    # Deleting a node in Circular Linked Lists
    def delete(self, key):
        if self.head is None:
            return

        if self.head.data is key and self.head.next is self.head:
            self.head = None
        elif self.head.data is key:
            last_node = self.head
            while last_node.next is not self.head:
                last_node = last_node.next

            last_node.next = self.head.next
            self.head = self.head.next
        else:
            current = self.head
            while current.next is not self.head:
                if current.next.data is key:
                    current.next = current.next.next
                    break
                current = current.next


clist = CircularLinkedList()
clist.add_in_beginning(1)
clist.add_in_end(2)
clist.add_in_end(3)
clist.add_in_end(4)
clist.print_list()
print("")
print(clist.search(3))
print(clist.search(6))
clist.delete(2)
clist.print_list()
