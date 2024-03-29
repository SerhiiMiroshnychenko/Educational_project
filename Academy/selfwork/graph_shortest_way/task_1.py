# Task 1

# Modify the `depth-first search` to produce strongly connected components
# (Strongly Connected Components ).

class Graph:
    def __init__(self, vertexes_number):
        self.__v = vertexes_number
        self.__vertexes = {index: [] for index in range(self.__v)}
        self.__weights = {}

    def add_edge(self, start, end, weight=0):
        self.__vertexes[start].append(end)
        self.__weights[(start, end)] = weight

    def show_vertexes(self):
        print(self.__vertexes)

    def show_weights(self):
        print(self.__weights)

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

    def _dfs2(self, vertex, visited_vertex=None):

        if visited_vertex is None:
            visited_vertex = [False] * self.__v
        visited_vertex[vertex] = True
        for index in self.__vertexes[vertex]:
            if not visited_vertex[index]:
                self._dfs2(index, visited_vertex)
        return vertex

    def show_dfs2(self):
        for vertex in self.__vertexes:
            print(vertex, ':', self._dfs2(vertex))



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
    from random import randint

    g = Graph(11)

    g.add_edge(0, 1, randint(1, 9))
    g.add_edge(1, 2, randint(1, 9))
    g.add_edge(1, 3, randint(1, 9))
    g.add_edge(2, 0, randint(1, 9))
    g.add_edge(3, 4, randint(1, 9))
    g.add_edge(4, 5, randint(1, 9))
    g.add_edge(5, 3, randint(1, 9))
    g.add_edge(6, 5, randint(1, 9))
    g.add_edge(6, 7, randint(1, 9))
    g.add_edge(7, 8, randint(1, 9))
    g.add_edge(8, 9, randint(1, 9))
    g.add_edge(9, 6, randint(1, 9))
    g.add_edge(10, 9, randint(1, 9))


    # g.show_vertexes()
    # g.dfs()
    #
    g.show_dfs2()

    # g.print_scc()
    #
    # g.show_vertexes()
    # g.show_weights()
