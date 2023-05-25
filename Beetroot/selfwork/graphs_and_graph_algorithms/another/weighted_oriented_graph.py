# Класс для представления graphического объекта
class Graph:
    # Конструктор для построения Graph
    def __init__(self, edges, n):

        # Список списков для представления списка смежности
        self.adj_list = [None] * n

        # выделяет память для списка смежности
        for i in range(n):
            self.adj_list[i] = []

        # добавляет ребра в ориентированный graph
        for (src, dest, weight) in edges:
            # выделяет узел в списке смежности от src до dest
            self.adj_list[src].append((dest, weight))


# Функция печати представления списка смежности Graph
def print_graph(graph):
    for src in range(len(graph.adj_list)):
        # вывести текущую вершину и все соседние с ней вершины
        for (dest, weight) in graph.adj_list[src]:
            print(f'({src} —> {dest}, {weight}) ', end='')
        print()


if __name__ == '__main__':

    # Вход #: ребра во взвешенном орграфе (согласно приведенной выше диаграмме)
    # Ребро (x, y, w) представляет собой ребро от `x` до `y`, имеющее вес `w`
    edges = [(0, 1, 6), (1, 2, 7), (2, 0, 5), (2, 1, 4), (3, 2, 10),
            (4, 5, 1), (5, 4, 3)]

    # Количество вершин (от 0 до 5)
    n = 6

    # построить graph из заданного списка ребер
    graph = Graph(edges, n)

    # печатать представление списка смежности Graph
    print_graph(graph)
