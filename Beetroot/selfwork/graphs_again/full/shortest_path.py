"""
Functions for finding paths in graphs.
"""

# pylint: disable=dangerous-default-value
def find_path(graph, start, end, path=[]):
    """
    Find a path between two nodes using recursion and backtracking.
    """
    path = path + [start]
    if start == end:
        return path
    if start not in graph:
        return None
    return next(
        (
            find_path(graph, node, end, path)
            for node in graph[start]
            if node not in path
        ),
        None,
    )

# pylint: disable=dangerous-default-value
def find_all_path(graph, start, end, path=[]):
    """
    Find all paths between two nodes using recursion and backtracking
    """
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_path(graph, node, end, path)
            paths.extend(iter(newpaths))
    return paths

def find_shortest_path(graph, start, end, path=[]):
    """
    find the shortest path between two nodes
    """
    path = path + [start]
    if start == end:
        return path
    if start not in graph:
        return None
    shortest = None
    for node in graph[start]:
        if node not in path:
            if newpath := find_shortest_path(graph, node, end, path):
                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath
    return shortest