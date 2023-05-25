def recursive_dfs(graph, start, path=None):
    """recursive depth first search from start"""
    if path is None:
        path = []
    path=path+[start]
    for node in graph[start]:
        if node not in path:
            path=recursive_dfs(graph, node, path)
    return path

def iterative_dfs(graph, start, path=None):
    """iterative depth first search from start"""
    if path is None:
        path = []
    q=[start]
    while q:
        v=q.pop(0)
        if v not in path:
            path=path+[v]
            q=graph[v]+q
    return path

def iterative_bfs(graph, start, path=None):
    """iterative breadth first search from start"""
    if path is None:
        path = []
    q=[start]
    while q:
        v=q.pop(0)
        if v not in path:
            path=path+[v]
            q += graph[v]
    return path

'''
   +---- A
   |   /   \
   |  B--D--C
   |   \ | /
   +---- E
'''


if __name__ == "__main__":
    graph = {'A':['B','C'],'B':['D','E'],'C':['D','E'],'D':['E'],'E':['A']}
    print('recursive dfs ', recursive_dfs(graph, 'A'))
    print('iterative dfs ', iterative_dfs(graph, 'A'))
    print('iterative bfs ', iterative_bfs(graph, 'A'))