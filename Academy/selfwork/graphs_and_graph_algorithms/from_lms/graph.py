from typing import Dict, Optional, Tuple


class Vertex:

    def __init__(self, key: int) -> None:
        self._id = key
        self.connected_to: Dict["Vertex", int] = {}

    def add_neighbor(self, nbr, weight=0) -> None:
        self.connected_to[nbr] = weight

    def __str__(self) -> str:
        return f"{self._id} connected to: {[x.get_id() for x in self.connected_to]}"

    def get_connections(self) -> Tuple["Vertex"]:
        return tuple(self.connected_to.keys())  # type: ignore

    def get_id(self) -> int:
        return self._id


class Graph:

    def __init__(self) -> None:
        self.vertices_dict: Dict[int, Vertex] = {}
        self.num_vertices: int = 0

    def add_vertex(self, key):
        self.num_vertices += 1
        new_vertex = Vertex(key)
        self.vertices_dict[key] = new_vertex
        return new_vertex

    def get_vertex(self, n: int) -> Optional[Vertex]:
        return self.vertices_dict[n] if n in self.vertices_dict else None

    def __contains__(self, n):
        return n in self.vertices_dict

    def add_edge(self, f, t, weight=0) -> None:
        if f not in self.vertices_dict:
            self.add_vertex(f)
        if t not in self.vertices_dict:
            self.add_vertex(t)
        self.vertices_dict[f].add_neighbor(self.vertices_dict[t], weight)

    def get_vertices(self) -> tuple:
        return tuple(self.vertices_dict.keys())

    def __iter__(self):
        return iter(self.vertices_dict.values())


if __name__ == "__main__":
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
        for w in v.get_connections():
            print(f"( {v.get_id()} , {w.get_id()} )")
