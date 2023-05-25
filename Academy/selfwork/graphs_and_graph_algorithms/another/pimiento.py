from collections import deque


graph = {'A': ['B', 'C'],
         'B': ['A', 'D', 'E'],
         'C': ['A', 'F'],
         'D': ['B'],
         'E': ['B', 'F'],
         'F': ['C', 'E']}
def dfs(graph, start):
    """
    Depth-First Search — Пошук вглибину
    """
    visited, stack = [], [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.append(vertex)
            stack.extend(set(graph[vertex]) - set(visited))
    return visited


def iterative_dfs(graph, start, path=None):
    """iterative depth first search from start"""
    if path is None:
        path = []
    q = [start]
    while q:
        v = q.pop()
        if v not in path:
            path = path + [v]
            q += graph[v]
    return path


def dfs_paths(graph, start, goal):
    """
    3 DFS Paths — пошук шляху між двома вершинами
    """
    stack = [(start, [start])]  # (vertex, path)
    while stack:
        (vertex, path) = stack.pop()
        for next in set(graph[vertex]) - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))


def bfs(graph, start):
    """
    Bread-First Search — Пошук в ширину
    """
    visited, queue = [], deque([start])
    while queue:
        vertex = queue.pop()
        if vertex not in visited:
            visited.append(vertex)
            queue.extendleft(set(graph[vertex]) - set(visited))
    return visited


def bfs_paths(graph, start, goal):
    """
    BFS Path
    """
    queue = deque([(start, [start])])
    while queue:
        (vertex, path) = queue.pop()
        for next in set(graph[vertex]) - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.appendleft((next, path+[next]))
                

def shortest_path(graph, start, goal):
    """
    BFS Shortest Path
    """
    try:
        return next(bfs_paths(graph, start, goal))
    except StopIteration:
        return None


if __name__ == "__main__":
    print(bfs(graph, 'A'))
    print(list(dfs_paths(graph, 'A', 'F')))
    print(iterative_dfs(graph, 'A'))
    print(dfs(graph, 'A'))
    print(list(bfs_paths(graph, 'A', 'F')))
    print(shortest_path(graph, 'A', 'F'))
    print(shortest_path(graph, 'E', 'D'))
    print(shortest_path(graph, 'A', 'D'))
    print(shortest_path(graph, 'F', 'D'))
