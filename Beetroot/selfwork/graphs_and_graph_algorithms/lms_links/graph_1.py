def generate_edges(graph):
    """
    Function to generate the list of all edges
    """
    edges = []
    for node in graph:
        edges.extend({node, neighbour} for neighbour in graph[node])
    return edges


def find_isolated_nodes(graph):
    """ returns a set of isolated nodes. """
    return {node for node in graph if not graph[node]}


class Graph(object):
    """
    A Python Class
    A simple Python graph class, demonstrating the essential
    facts and functionalities of graphs.
    """

    def __init__(self, graph_dict=None):
        """ initializes a graph object
            If no dictionary or None is given,
            an empty dictionary will be used
        """
        if graph_dict is None:
            graph_dict = {}
        self._graph_dict = graph_dict

    def edges(self, vertice):
        """ returns a list of all the edges of a vertice"""
        return self._graph_dict[vertice]

    def all_vertices(self):
        """ returns the vertices of a graph as a set """
        return set(self._graph_dict.keys())

    def all_edges(self):
        """ returns the edges of a graph """
        return self.__generate_edges()

    def add_vertex(self, vertex):
        """
        If the vertex "vertex" is not in
        self._graph_dict, a key "vertex" with an empty
        list as a value is added to the dictionary.
        Otherwise, nothing has to be done.
        """
        if vertex not in self._graph_dict:
            self._graph_dict[vertex] = []

    def add_edge(self, edge):
        """
        assumes that edge is of type set, tuple or list;
        between two vertices can be multiple edges!
        """
        edge = set(edge)
        vertex1, vertex2 = tuple(edge)
        for x, y in [(vertex1, vertex2), (vertex2, vertex1)]:
            if x in self._graph_dict:
                self._graph_dict[x].add(y)
            else:
                self._graph_dict[x] = [y]

    def __generate_edges(self):
        """
        A static method generating the edges of the
        graph "graph". Edges are represented as sets
        with one (a loop back to the vertex) or two
        vertices
        """
        edges = []
        for vertex in self._graph_dict:
            for neighbour in self._graph_dict[vertex]:
                if {neighbour, vertex} not in edges:
                    edges.append({vertex, neighbour})
        return edges

    def __iter__(self):
        self._iter_obj = iter(self._graph_dict)
        return self._iter_obj

    def __next__(self):
        """
        allows us to iterate over the vertices
        """
        return next(self._iter_obj)

    def __str__(self):
        res = "vertices: "
        for k in self._graph_dict:
            res += f"{str(k)} "
        res += "\nedges: "
        for edge in self.__generate_edges():
            res += f"{str(edge)} "
        return res



if __name__ == "__main__":

    g1: dict = { "a" : {"c"},
                 "b" : {"c", "e"},
                 "c" : {"a", "b", "d", "e"},
                 "d" : {"c"},
                 "e" : {"c", "b"},
                 "f" : {}
                 }
    g2:dict = { "a" : {"d"},
                "b" : {"c"},
                "c" : {"b", "c", "d", "e"},
                "d" : {"a", "c"},
                "e" : {"c"},
                "f" : {}
                }

    print(generate_edges(g1))
    print(generate_edges(g2))

    graph1: Graph = Graph(g1)
    graph2: Graph = Graph(g1)

    for vertice in graph1:
        print(f"1.Edges of vertice {vertice}: ", graph1.edges(vertice))
    for vertice in graph2:
        print(f"2.Edges of vertice {vertice}: ", graph2.edges(vertice))