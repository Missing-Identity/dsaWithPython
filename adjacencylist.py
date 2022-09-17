# Initialising Node Class
class AdjNode:
    def __init__(self, value):
        self.data = value
        self.next = None


# Initialising Adjacency List class
class AdjList:
    def __init__(self, num):
        self.V = num
        self.adj_list = [None] * self.V

    # Adding edge
    def add_edge(self, src, dest):
        new_node = AdjNode(dest)
        new_node.next = self.adj_list[src]
        self.adj_list[src] = new_node

    # Checking for Edge in Graph
    def has_edge(self, src, dest):
        temp = self.adj_list[src]
        while temp is not None:
            if temp.data is dest:
                return 1
            temp = temp.next
        return 0

    # Removing Edge from Graph
    def remove_edge(self, src, dest):
        if self.adj_list[src] is None:
            return
        if self.adj_list[src].data is dest:
            self.adj_list[src] = self.adj_list[src].next
        else:
            current = AdjNode(self.adj_list[src])
            while current.next is not None:
                if current.next.data is dest:
                    temp = AdjNode(current.next)
                    temp.next = current.next
                    break
                else:
                    current = current.next

    # Printing List
    def print_graph(self):
        for i in range(self.V):
            temp = self.adj_list[i]
            print("Adjacency List[" + str(i) + "] ", end='')
            while temp is not None:
                print(f"{temp.data} --> ", end='')
                temp = temp.next
            print("None")


# Outputs
obj = AdjList(5)
obj.add_edge(0, 1)
obj.add_edge(0, 2)
obj.add_edge(0, 3)
obj.add_edge(1, 3)
obj.add_edge(1, 4)
obj.add_edge(2, 3)
obj.add_edge(3, 4)
print(obj.has_edge(0, 2))
print(obj.has_edge(0, 5))
obj.remove_edge(0, 2)
print(obj.has_edge(0, 2))
obj.print_graph()
