from collections import defaultdict

class Graph:

    def __init__(self,vertices):
        self._v= vertices
        self._graph = defaultdict(list)
    def add_edge(self, u, v):
        self._graph[u].append(v)
    def dfs_util(self, v, visited):
        visited[v]= True
        print(v, end='')
        for i in self._graph[v]:
            if not visited[i]:
                self.dfs_util(i, visited)
    def fill_order(self, v, visited, stack):
        visited[v]= True
        for i in self._graph[v]:
            if not visited[i]:
                self.fill_order(i, visited, stack)
        stack = stack.append(v)

    def get_transpose(self):
        gr = Graph(self._v)
        for i in self._graph:
            for j in self._graph[i]:
                gr.add_edge(j, i)
        return gr

    def print_sc_cs(self):

        stack = []
        visited = [False] * self._v
        for i in range(self._v):
            if not visited[i]:
                self.fill_order(i, visited, stack)
        gr = self.get_transpose()
        visited = [False] * self._v
        while stack:
            print('\t'*4, end='')
            i = stack.pop()
            if not visited[i]:
               gr.dfs_util(i, visited)
               print('')


if __name__ == "__main__":

    g = Graph(5)
    g.add_edge(1, 0)
    g.add_edge(0, 2)
    g.add_edge(2, 1)
    g.add_edge(0, 3)
    g.add_edge(3, 4)

    print ("Following are strongly connected components\nin given graph:")
    g.print_sc_cs()
