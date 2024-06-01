from copy import deepcopy


class UndirectedGraph:
    def __init__(self, vertices_count):
        self.__vertices = [_ for _ in range(vertices_count)]
        self.__edges = []

        self.__neighbours = {vertex: [] for vertex in self.__vertices}

    @property
    def vertices_count(self):
        return len(self.__vertices)

    @property
    def edges_count(self):
        return len(self.__edges)

    @property
    def vertices(self):
        return iter(self.__vertices)

    @property
    def edges(self):
        return iter(self.__edges)

    def add_edge(self, edge):
        start, end = edge

        if self.are_connected(start, end):
            raise ValueError("Invalid edge")

        self.__edges.append(edge)
        self.__neighbours[start].append(end)
        self.__neighbours[end].append(start)

    def remove_edge(self, edge):
        start, end = edge

        if not self.are_connected(start, end):
            raise ValueError("Invalid edge")

        self.__edges.remove(edge)
        self.__neighbours[start].remove(end)
        self.__neighbours[end].remove(start)

    def add_vertex(self, vertex):
        if vertex in self.__vertices:
            raise ValueError("Invalid vertex")

        self.__vertices.append(vertex)
        self.__neighbours[vertex] = []

    def remove_vertex(self, vertex):
        try:
            self.__vertices[vertex]
        except IndexError:
            raise ValueError("Invalid vertex")

        self.__vertices.remove(vertex)

        for neighbour in self.__neighbours[vertex]:
            self.__neighbours[neighbour].remove(vertex)
            self.__edges.remove((vertex, neighbour) if (vertex, neighbour) in self.__edges else (neighbour, vertex))

        self.__neighbours.pop(vertex)

    def are_connected(self, start, end):
        return end in self.__neighbours[start]

    def degree(self, vertex):
        try:
            self.__vertices[vertex]
        except IndexError:
            raise ValueError("Invalid vertex")
        return len(self.__neighbours[vertex])

    def neighbours(self, vertex):
        try:
            self.__vertices[vertex]
        except IndexError:
            raise ValueError("Invalid vertex")
        return iter(self.__neighbours[vertex])

    def copy(self):
        return deepcopy(self)
