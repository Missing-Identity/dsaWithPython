class AdjMatrix:
    def __init__(self, size):
        self.arr = []
        for i in range(size):
            self.arr.append([0 for i in range(size)])
        self.size = size

    # Adding Edge to Directed Adjacency Matrix
    def add_edge(self, src, dest):
        self.arr[src][dest] = 1

    # Checking for an Edge in Directed Adjacency Matrix
    def has_edge(self, src, dest):
        if self.arr[src][dest] == 1:
            return 1
        return 0

    # Removing an Edge from Directed Adjacecncy Matrix
    def remove_edge(self, src, dest):
        self.arr[src][dest] = 0

    # Printing Directed Adjacency Matrix
    def print_adj_matrix(self):
        for i in range(self.size):
            for j in range(self.size):
                print(self.arr[i][j], end="")
            print()


# Outputs
obj = AdjMatrix(5)
obj.add_edge(0, 1)
obj.add_edge(0, 2)
obj.add_edge(0, 3)
obj.add_edge(1, 3)
obj.add_edge(1, 4)
obj.add_edge(2, 3)
obj.add_edge(3, 4)

print("Adj Matrix Representation of the graph")
obj.print_adj_matrix()
print(obj.has_edge(0, 4))
print(obj.has_edge(0, 2))
obj.remove_edge(0, 2)
print(obj.has_edge(0, 2))
