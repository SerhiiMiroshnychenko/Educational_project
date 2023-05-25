# Класс для представления graphического объекта
class Graph:
    # 1ТП4Т Конструктор
    def __init__(self, edges, n):
        # выделяет память для списка смежности
        self.adj_list = [[] for _ in range(n)]

        # добавляет ребра в ориентированный graph
        for (src, dest) in edges:
            # выделяет узел в списке смежности от src до dest
            self.adj_list[src].append(dest)


# Функция печати представления списка смежности Graph
def print_graph(graph):
    for src in range(len(graph.adj_list)):
        # вывести текущую вершину и все соседние с ней вершины
        for dest in graph.adj_list[src]:
            print(f'({src} —> {dest}) ', end='')
        print()


if __name__ == '__main__':

    # Вход #: ребра в ориентированном Graph
    edges = [(0, 1), (1, 2), (2, 0), (2, 1), (3, 2), (4, 5), (5, 4)]

    # Количество вершин (от 0 до 5)
    n = 6

    # построить graph из заданного списка ребер
    graph = Graph(edges, n)

    # печатать представление списка смежности Graph
    print_graph(graph)
