from typing import Optional, Dict, Tuple

from homework.homework_23_queue_deque_stack.task_3_2 import Queue


class Vertex:
    def __init__(self, key: int) -> None:
        self._id = key
        self.connected_to: Dict[Vertex, int] = {}

    def add_neighbor(self, vertex:"Vertex", weight:int=0) -> None:
        self.connected_to[vertex] = weight

    def get_connection(self) -> Tuple["Vertex", ...]:
        return tuple(self.connected_to.keys())

    def get_id(self) -> int:
        return self._id

    def get_weight(self, vertex: "Vertex") -> int:
        return self.connected_to[vertex]

    def __str__(self):
        return f'Vertex {self._id} connected to {[vertex.get_id() for vertex in self.connected_to]}'


class Graph:

    def __init__(self) -> None:
        self.vertexes: Dict[int, Vertex] = {}
        self.vertex_amount: int = 0

    def add_vertex(self, key) -> Vertex:
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

    def get_single_vertex(self, key: int) -> Optional[Vertex]:
        if key in self.vertexes:
            return self.vertexes[key]
        print('Graph does not have this vertex.')
        return None

    def get_all_vertexes(self) -> tuple:
        return tuple(self.vertexes.keys())

    def __contains__(self, item):
        return item in self.vertexes

    def __iter__(self):
        return iter(self.vertexes.values())

    def bfs(self):
        vertex_queue = Queue()
        visited_vertex = []
        vertex_queue.enqueue(self.vertexes[0])
        for connection in self.vertexes[0].get_connection():
            vertex_queue.enqueue(connection)
        while not vertex_queue.is_empty():
            current_vertex = vertex_queue.dequeue()
            visited_vertex.append(current_vertex)
            for connection in current_vertex.get_connection():
                if connection not in vertex_queue:
                    vertex_queue.enqueue(connection)
        return visited_vertex




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
        for w in v.get_connection():
            print("( %s , %s , %d )" % (v.get_id(), w.get_id(), v.get_weight(w)))

    print(g.bfs())


