from typing import Optional, Union, Dict, Tuple


class Vertex:
    def __init__(self, key: int) -> None:
        self._id: int = key
        self.connected_to: Dict[Vertex, int] = {}

    def add_neighbor(self, vertex: "Vertex", weight: int = 0) -> None:
        self.connected_to[vertex] = weight

    def get_connection(self) -> Tuple["Vertex"]:
        return tuple(self.connected_to.keys())

    def get_weight(self, vertex: "Vertex") -> int:
        return self.connected_to[vertex]

    def get_id(self) -> int:
        return self._id

    def __str__(self):
        return f'Vertex {self._id} connected to {[vertex.get_id() for vertex in self.connected_to]}'


class Graph:
    def __init__(self):
        self.vertexes: Dict[int, Vertex] = {}
        self.vertex_amount: int = 0

    def add_vertex(self, key: int) -> Vertex:
        self.vertex_amount += 1
        new_vertex = Vertex(key)
        self.vertexes[key] = new_vertex
        return new_vertex

    def add_edge(self, start: int, end: int, weight: int) -> None:
        if start not in self.vertexes:
            self.add_vertex(start)
        if end not in self.vertexes:
            self.add_vertex(end)
        self.vertexes[start].add_neighbor(self.vertexes[end], weight)

    def get_single_vertex(self, key: int) -> Union[Vertex, None]:
        if key in self.vertexes:
            return self.vertexes[key]
        else:
            print('Graph does not have this vertex')
            return None

    def get_all_vertexes(self) -> tuple:
        return tuple(self.vertexes.keys())

    def __contains__(self, item):
        return item in self.vertexes

    def __iter__(self):
        return iter(self.vertexes.values())


if __name__ == '__main__':
    g = Graph()
    for i in range(6):
        g.add_vertex(i)

    g.add_edge(0, 1, 5)
    g.add_edge(0, 5, 2)
    g.add_edge(1, 2, 4)
    g.add_edge(2, 3, 9)
    g.add_edge(3, 4, 7)
    g.add_edge(3, 5, 3)
    g.add_edge(4, 0, 1)
    g.add_edge(5, 4, 8)
    g.add_edge(5, 2, 1)
    for v in g:
        for w in v.get_connection():
            print("( %s , %s , %d )" % (v.get_id(), w.get_id(), v.get_weight(w)))
