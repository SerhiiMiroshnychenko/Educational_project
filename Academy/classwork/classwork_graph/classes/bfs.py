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