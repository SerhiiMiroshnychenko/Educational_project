class Graph:
    def init(self):
        self.graph = defaultdict(list)

    def add_edge(self, v1, v2):
        self.graph[v1].append(v2)

    def dfs(self, start_v, visited, stack):
        visited[start_v] = True
        for neighbor in self.graph[start_v]:
            if neighbor not in visited:
                self.dfs(neighbor, visited, stack)
        stack.append(start_v)
        # print(start_v, '\n', end=' ')

    def graph_transpose(self):
        g = Graph()
        for vertex in self.graph:
            for neighbor in self.graph[vertex]:
                g.add_edge(neighbor, vertex)
        return g
    def strongly_connected_components(self):
        visited = {}
        # print('1', visited)
        stack = []
        # print('4', stack)

        for v in self.graph:
            if v not in visited:
                self.dfs(v, visited, stack)

        strongly_connected_components = []
        visited = {}
        # print('2', visited)

        g = self.graph_transpose()
        # print('3', stack)

        while stack:
            v = stack.pop()
            if v not in visited:
                component = []
                g.dfs(v, visited, component)
                strongly_connected_components.append(component)
                # print("6", component)

        return strongly_connected_components


if name == "main":
    g = Graph()
    g.add_edge(1, 0)
    g.add_edge(0, 2)
    g.add_edge(2, 1)
    g.add_edge(0, 3)
    g.add_edge(3, 4)
    # g.add_edge(4, 4)

    scc = g.strongly_connected_components()
    print(scc)