# Python3 code for printing shortest path between
# two vertices of unweighted graph

# utility function to form edge between two vertices
# source and dest
def add_edge(adj, src, dest):

    adj[src].append(dest)
    adj[dest].append(src)

# a modified version of BFS that stores predecessor
# of each vertex in array p
# and its distance from source in array d
def bfs(adj, src, dest, v, pred, dist):

    # boolean array visited[] which stores the
    # information whether ith vertex is reached
    # at least once in the Breadth first search
    visited = [False for _ in range(v)]

    # initially all vertices are unvisited
    # so v[i] for all i is false
    # and as no path is yet constructed
    # dist[i] for all i set to infinity
    for i in range(v):

        dist[i] = 1000000
        pred[i] = -1

    # now source is first to be visited and
    # distance from source to itself should be 0
    visited[src] = True
    dist[src] = 0
    queue = [src]
    # standard BFS algorithm
    while queue:
        u = queue[0]
        queue.pop(0)
        for i in range(len(adj[u])):

            if not visited[adj[u][i]]:
                visited[adj[u][i]] = True
                dist[adj[u][i]] = dist[u] + 1
                pred[adj[u][i]] = u
                queue.append(adj[u][i])

                # We stop BFS when we find
                # destination.
                if adj[u][i] == dest:
                    return True

    return False

# utility function to print the shortest distance
# between source vertex and destination vertex
def print_shortest_distance(adj, s, dest, v):

    # predecessor[i] array stores predecessor of
    # i and distance array stores distance of i
    # from s
    pred=[0 for _ in range(v)]
    dist=[0 for _ in range(v)]

    if not bfs(adj, s, dest, v, pred, dist):
        print("Given source and destination are not connected")

    crawl = dest
    path = [crawl]
    while pred[crawl] != -1:
        path.append(pred[crawl])
        crawl = pred[crawl]


    # distance from source is in distance array
    print(f"Shortest path length is : {str(dist[dest])}", end = '')

    # printing path from source to destination
    print("\nPath is : : ")

    for i in range(len(path)-1, -1, -1):
        print(path[i], end=' ')

# Driver program to test above functions
if __name__=='__main__':

    # no. of vertices
    v = 8

    # array of vectors is used to store the graph
    # in the form of an adjacency list
    adj = [[] for _ in range(v)]  # type: ignore

    # Creating graph given in the above diagram.
    # add_edge function takes adjacency list, source
    # and destination vertex as argument and forms
    # an edge between them.
    add_edge(adj, 0, 1)
    add_edge(adj, 0, 3)
    add_edge(adj, 1, 2)
    add_edge(adj, 3, 4)
    add_edge(adj, 3, 7)
    add_edge(adj, 4, 5)
    add_edge(adj, 4, 6)
    add_edge(adj, 4, 7)
    add_edge(adj, 5, 6)
    add_edge(adj, 6, 7)
    source = 0
    dest = 7
    print_shortest_distance(adj, source, dest, v)

    # This code is contributed by rutvik_56