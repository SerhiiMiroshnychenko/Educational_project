from typing import Dict, Optional, Tuple

from selfwork.graphs_and_graph_algorithms.from_lms.queue import Queue


class Vertex:

    def __init__(self, key: int) -> None:
        self._id = key
        self.connected_to: Dict["Vertex", int] = {}
        self._color = "white"
        self._predecessor = None
        self._distance = 0

    def get_color(self) -> str:
        return self._color

    def set_color(self, color) -> None:
        self._color = color

    def get_distance(self) -> int:
        return self._distance

    def set_distance(self, distance: int) -> None:
        self._distance = distance

    def get_previous(self) -> Optional["Vertex"]:
        return self._predecessor

    def set_previous(self, previous: Optional["Vertex"]) -> None:
        self._predecessor = previous

    def add_neighbor(self, nbr, weight=0) -> None:
        self.connected_to[nbr] = weight

    def __str__(self) -> str:
        return f"{self._id} connected to: {[x.get_id() for x in self.connected_to]}"

    def get_connections(self) -> Tuple["Vertex"]:
        return tuple(self.connected_to.keys())

    def get_id(self) -> int:
        return self._id


class Graph:

    def __init__(self) -> None:
        self.vertices_dict: Dict[str, Vertex] = {}
        self.num_vertices: int = 0

    def add_vertex(self, key):
        self.num_vertices += 1
        new_vertex = Vertex(key)
        self.vertices_dict[key] = new_vertex
        return new_vertex

    def get_vertex(self, n: str) -> Optional[Vertex]:
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

    def bfs(self, start: Vertex):
        start.set_distance(0)
        start.set_previous(None)
        vert_queue = Queue()
        vert_queue.enqueue(start)
        while vert_queue.size() > 0:
            current_vert: Vertex = vert_queue.dequeue()
            for nbr in current_vert.get_connections():
                if nbr.get_color() == 'white':
                    nbr.set_color('gray')
                    nbr.set_distance(current_vert.get_distance() + 1)
                    nbr.set_previous(current_vert)
                    vert_queue.enqueue(nbr)
            current_vert.set_color('black')


def build_graph(file_path):
    d: dict = {}
    g: Graph = Graph()
    with open(file_path, 'r') as file:
        # create buckets of words that differ by one letter
        for line in file:
            word = line[:-1]
            for ind in range(len(word)):
                bucket = f'{word[:ind]}_{word[ind + 1:]}'
                if bucket in d:
                    d[bucket].append(word)
                else:
                    d[bucket] = [word]
        # add vertices and edges for words in the same bucket
        for bucket in d:
            for word1 in d[bucket]:
                for word2 in d[bucket]:
                    if word1 != word2:
                        g.add_edge(word1, word2)
        return g


def traverse(y: Vertex):
    x = y
    while x.get_previous():
        print(x.get_id())
        x = x.get_previous()
    print(x.get_id())


if __name__ == "__main__":
    g = build_graph("vocabulary.txt")
    g.bfs(g.get_vertex("FOOL"))
    traverse(g.get_vertex("SAGE"))
