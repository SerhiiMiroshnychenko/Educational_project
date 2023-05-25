# adjacency matrix, undirected graph

class Graph():
    def __init__(self, size):
        self.size = size
        self.adj = [[0] * size for i in range(size)]
        for i in range(self.size):
            self.adj[i][i] = "x"

    def add_edge(self, orig, dest):
        if (orig and dest) in range(1, self.size + 1) and orig != dest:
            self.adj[orig - 1][dest - 1] = 1
            self.adj[dest - 1][orig - 1] = 1
        else:
            print("Invalid Edge")

    def remove_edge(self, orig, dest):
        if (orig and dest) in range(1, self.size + 1) and orig != dest:
            self.adj[orig - 1][dest - 1] = 0
            self.adj[dest - 1][orig - 1] = 0
        else:
            print("Invalid Edge")

    def display(self):
        for row in self.adj:
            print()
            for val in row:
                print(' {}'.format(val), end="")

            # sample graph


G = Graph(4)
G.display()

print()

G.add_edge(1, 2)
G.add_edge(1, 4)
G.add_edge(2, 3)
G.display()

print()

G.remove_edge(1, 2)
G.remove_edge(1, 4)
G.display()

print()
print()

G.add_edge(2, 0)
G.add_edge(3, 5)
G.add_edge(4, 4)

# code by github.com/alandavidgrunber