# Практика 3
# Куцарев Андрей АИ-183
# Алгорим Прима и Краскала
# Вариант 9

import random
from string import ascii_uppercase

# Прима

def prima(W, city_labels = None):
    """
    Алгоритм Прима для нахождения сети дорог минимальной длины
    Дискретная алгебра, приложение 1
    """

    _ = float('inf')
    cities_count = len(W)

    # проверка на размерость таблицы связей
    for weights in W:
        assert len(weights) == cities_count

    # генерация имен городов
    if not city_labels:
        city_labels = [ascii_uppercase[x] for x in range(cities_count)]

    assert cities_count <= len(city_labels)

    # выбор начального города
    free_vertexes = list(range(0, len(city_labels)))

    starting_vertex = random.choice(free_vertexes)
    tied = [starting_vertex]
    free_vertexes.remove(starting_vertex)

    print('Started with %s' % city_labels[starting_vertex])

    road_length = 0

    # пока есть свободные вершины
    while free_vertexes:
        min_link = None  # соединение, образующее минимальный путь
        overall_min_path = _    # минимальный путь среди всех возможных

        # проход по всем уже связанным дорогой вершинам
        for current_vertex in tied:
            weights = W[current_vertex]   # связи текущей вершины с другими

            min_path = _
            free_vertex_min = current_vertex

            # проход по связанным городам
            for vertex in range(cities_count):
                vertex_path = weights[vertex]
                if vertex_path == 0:
                    continue

                if vertex in free_vertexes and vertex_path < min_path:
                    free_vertex_min = vertex
                    min_path = vertex_path

            if free_vertex_min != current_vertex:
                if overall_min_path > min_path:
                    min_link = (current_vertex, free_vertex_min)
                    overall_min_path = min_path
        try:
            path_length = W[min_link[0]][min_link[1]]
        except TypeError:
            print('Unable to find path')
            return

        print('Connecting %s to %s [%s]' % (city_labels[min_link[0]], city_labels[min_link[1]], path_length))

        road_length += path_length
        free_vertexes.remove(min_link[1])
        tied.append(min_link[1])

    print('Road length: %s' % road_length)
    # TODO: return graph

if __name__ == '__main__':

    _ = float('inf')

    W = [
        #A  B  C  D  E  F  G
        [0, 3, _, _, _, 2, _], # A
        [3, 0, 3, _, _, _, 6], # B
        [_, 3, 0, 3, 2, _, 1], # C
        [_, _, 3, 0, 5, _, _], # D
        [_, _, 2, 5, 0, 4, 3], # E
        [2, _, _, _, 4, 0, 3], # F
        [_, 6, 1, _, 3, 3, 0], # G
    ]

prima(W)

# Краскала

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        xRoot = self.find(parent, x)
        yRoot = self.find(parent, y)
        if rank[xRoot] < rank[yRoot]:
            parent[xRoot] = yRoot
        elif rank[xRoot] > rank[yRoot]:
            parent[yRoot] = xRoot
        else:
            parent[yRoot] = xRoot
            rank[xRoot] += 1

    def kruskal_algorithm(self):
        result = []
        i, e = 0, 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        while e < self.V - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)
        print("\nMST of Kruskal's algorithm: ")
        print("Vertex A   Vertex B  Weight")
        for u, v, weight in result:
            print("%5d %9d %10d" % (u, v, weight))


g = Graph(8)
g.addEdge(0, 1, 7)
g.addEdge(0, 3, 5)
g.addEdge(0, 4, 3)
g.addEdge(1, 2, 8)
g.addEdge(1, 5, 9)
g.addEdge(2, 5, 10)
g.addEdge(2, 7, 6)
g.addEdge(3, 5, 7)
g.addEdge(3, 6, 6)
g.addEdge(4, 6, 10)
g.addEdge(4, 7, 6)
g.addEdge(5, 7, 3)
g.addEdge(6, 7, 4)

g.kruskal_algorithm()
