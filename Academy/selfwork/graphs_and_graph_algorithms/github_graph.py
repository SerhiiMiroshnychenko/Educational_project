class Graph:
    def __init__(self, name = "Un-named Graph"):
        self.name = name
        self.nodes = []

    def add_node(self, vertex = None):
        self.nodes.append(vertex)

    def print_details(self):
        print(self.name)

    def set_name(self, name):
        self.name = name

    def dfs(self, node):
        str_ = " <dfs> . "
        node.set_visited(True)
        stack = [node]
        while stack:
            n = stack.pop()
            str_ += f"{n.get_name()} . "
            for e in n.edge_list():
                if not e.get_dest().is_visited():
                    stack.append(e.get_dest())
                    e.get_dest().set_visited()

        print(str_)

    def bfs(self, node):
        str_ = " <bfs> . "
        queue = []

        node.set_visited(True)
        queue.insert(0, node)

        while queue:
            n = queue.pop()
            str_ += f"{n.get_name()} . "
            for e in n.edge_list():
                if not e.get_dest().is_visited():
                    queue.insert(0, e.get_dest())
                    e.get_dest().set_visited()

        print(str_)

    def prim(self, node):
        node.set_visited()
        l = [e for e in node.edge_list() if (not e.get_dest().is_visited())]
        while l:
            m = l[0]
            for e in l:
                if e.get_weight() < m.get_weight():
                    m = e

            l.remove(m)

            if not m.get_dest().is_visited():
                m.get_dest().set_visited()
                print(f"{m.get_start().get_name()} - {m.get_dest().get_name()}")
                n = m.get_dest()
                for e in n.edge_list():
                    if not e.get_dest().is_visited():
                        l.append(e)

    def dijkstra(self, node):
        node.set_visited()
        node.set_distance(0)
        l = [node]
        while l:
            n = l.pop(0)
            for ed in n.edge_list():
                if ed.get_start().get_distance() + ed.get_weight() < ed.get_dest().get_distance():
                    ed.get_dest().set_distance(ed.get_start().get_distance() + ed.get_weight())

            min_dist = Node("Dummy")
            for nd in self.nodes:
                if not nd.is_visited() and min_dist.get_distance() > nd.get_distance():
                    min_dist = nd

            if min_dist.get_name() != "Dummy":
                min_dist.set_visited()
                l.append(min_dist)

    def kruskal(self):
        ed = []
        for node in self.nodes:
            ed.extend(iter(node.edge_list()))
        while ed:
            m = ed[0]
            for edge in ed:
                if edge.get_weight() < m.get_weight():
                    m = edge
            ed.remove(m)
            if not m.get_start().is_visited() or not m.get_dest().is_visited():
                print(f"{m.get_start().get_name()} - {m.get_dest().get_name()}")
                m.get_start().set_visited()
                m.get_dest().set_visited()



class Node:
    def __init__(self, name = "Un-named Node", distance = 10000):
        self.name = name
        self.edges = []
        self.distance = distance
        self.visited = False

    def print_details(self):
        print(self.name)

    def add_edge(self, edge = None):
        self.edges.append(edge)

    def set_visited(self, b = True):
        self.visited = b

    def is_visited(self):
        return self.visited

    def get_name(self):
        return self.name

    def edge_list(self):
        return self.edges

    def set_distance(self, distance):
        self.distance = distance

    def get_distance(self):
        return self.distance

class Edge:
    def __init__(self, start, dest, weight = 1):
        self.start = start
        self.dest = dest
        self.weight = weight

    def print_details(self):
        print(self.start, self.dest, self.weight)

    def get_start(self):
        return self.start

    def get_dest(self):
        return self.dest

    def get_weight(self):
        return self.weight



if __name__ == "__main__":

    g1 = Graph()

    p = Node("P")
    q = Node("Q")
    r = Node("R")
    s = Node("S")
    t = Node("T")
    u = Node("U")

    pq = Edge(p, q, 1)
    p.add_edge(pq)

    qr = Edge(q, r, 1)
    q.add_edge(qr)

    ps = Edge(p, s, 6)
    p.add_edge(ps)

    qs = Edge(q, s, 4)
    q.add_edge(qs)

    rs = Edge(r, s, 2)
    r.add_edge(rs)

    ru = Edge(r, u, 1)
    r.add_edge(ru)

    pt = Edge(p, t, 7)
    p.add_edge(pt)

    tu = Edge(t, u, 2)
    t.add_edge(tu)

    st = Edge(s, t, 3)
    s.add_edge(st)

    su = Edge(s, u, 2)
    s.add_edge(su)

    g1.add_node(p)
    g1.add_node(q)
    g1.add_node(r)
    g1.add_node(s)
    g1.add_node(t)
    g1.add_node(u)

    g1.dfs(p)
    g1.bfs(p)
    g1.prim(p)
    g1.dijkstra(p)
    g1.kruskal()