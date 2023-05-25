class Graph:
    def __init__(self, vertexes_number):
        self.__v = vertexes_number
        self.__vertexes = {index: [] for index in range(self.__v)}

    def add_edge(self, start, end):
        self.__vertexes[start].append(end)

    def dfs(self, vertex=0):
        print('Depth First Search: ')
        self._dfs(vertex)
        print('\n')

    def _dfs(self, vertex, visited_vertex=None):
        if visited_vertex is None:
            visited_vertex = [False] * self.__v
        visited_vertex[vertex] = True
        print(vertex, end=' ')
        for index in self.__vertexes[vertex]:
            if not visited_vertex[index]:
                self._dfs(index, visited_vertex)

    def fill_order(self, vertex, visited_vertex, stack):

        visited_vertex[vertex] = True
        for index in self.__vertexes[vertex]:
            if not visited_vertex[index]:
                self.fill_order(index, visited_vertex, stack)
        stack = stack.append(vertex)

    def transpose(self):
        transposed_graph = Graph(self.__v)

        for start in self.__vertexes:
            for end in self.__vertexes[start]:
                transposed_graph.add_edge(end, start)
        return transposed_graph

    def print_scc(self):
        print("Strongly Connected Components:")
        stack = []
        visited_vertex = [False] * self.__v

        for index in range(self.__v):
            if not visited_vertex[index]:
                self.fill_order(index, visited_vertex, stack)

        transposed_graph = self.transpose()

        visited_vertex = [False] * self.__v

        while stack:
            index = stack.pop()
            if not visited_vertex[index]:
                transposed_graph._dfs(index, visited_vertex)
                print()


if __name__ == "__main__":
    g = Graph(11)

    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 0)
    g.add_edge(3, 4)
    g.add_edge(4, 5)
    g.add_edge(5, 3)
    g.add_edge(6, 5)
    g.add_edge(6, 7)
    g.add_edge(7, 8)
    g.add_edge(8, 9)
    g.add_edge(9, 6)
    g.add_edge(10, 9)

    g.dfs()

    g.print_scc()
