from copy import deepcopy


class DirectedGraph:
    def __init__(self, vertices_count):
        self.__vertices = [_ for _ in range(vertices_count)]
        self.__edges = []

        self.__inbound_neighbours = {vertex: [] for vertex in self.__vertices}
        self.__outbound_neighbours = {vertex: [] for vertex in self.__vertices}
        self.__cost = {}

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

    def add_edge(self, edge, cost):
        start, end = edge

        if self.are_connected(start, end):
            raise ValueError("Invalid edge")

        self.__edges.append(edge)
        self.__cost[edge] = cost

        try:
            self.__outbound_neighbours[start].append(end)
            self.__inbound_neighbours[end].append(start)
        except KeyError:
            raise ValueError("Invalid vertex")

    def remove_edge(self, edge):
        start, end = edge

        if not self.are_connected(start, end):
            raise ValueError("Invalid edge")

        self.__edges.remove(edge)
        self.__cost.pop(edge)

        self.__outbound_neighbours[start].remove(end)
        self.__inbound_neighbours[end].remove(start)

    def add_vertex(self, vertex):
        if vertex in self.__vertices:
            raise ValueError("Invalid vertex")

        self.__vertices.append(vertex)
        self.__inbound_neighbours[vertex] = []
        self.__outbound_neighbours[vertex] = []

    def remove_vertex(self, vertex):
        try:
            self.__vertices[vertex]
        except IndexError:
            raise ValueError("Invalid vertex")

        self.__vertices.remove(vertex)

        for inbound_neighbour in self.__inbound_neighbours[vertex]:
            edge = inbound_neighbour, vertex
            self.__outbound_neighbours[inbound_neighbour].remove(vertex)
            self.__edges.remove(edge)
            self.__cost.pop(edge)

        for outbound_neighbour in self.__outbound_neighbours[vertex]:
            edge = vertex, outbound_neighbour
            self.__inbound_neighbours[outbound_neighbour].remove(vertex)
            self.__edges.remove(edge)
            self.__cost.pop(edge)

        self.__inbound_neighbours.pop(vertex)
        self.__outbound_neighbours.pop(vertex)

    def are_connected(self, start, end):
        return self.__cost.get((start, end)) is not None

    def in_degree(self, vertex):
        try:
            self.__vertices[vertex]
        except IndexError:
            raise ValueError("Invalid vertex")
        return len(self.__inbound_neighbours[vertex])

    def out_degree(self, vertex):
        try:
            self.__vertices[vertex]
        except IndexError:
            raise ValueError("Invalid vertex")
        return len(self.__outbound_neighbours[vertex])

    def inbound_neighbours(self, vertex):
        try:
            self.__vertices[vertex]
        except IndexError:
            raise ValueError("Invalid vertex")
        return iter(self.__inbound_neighbours[vertex])

    def outbound_neighbours(self, vertex):
        try:
            self.__vertices[vertex]
        except IndexError:
            raise ValueError("Invalid vertex")
        return iter(self.__outbound_neighbours[vertex])

    def get_cost(self, edge):
        if self.__cost.get(edge) is None:
            raise ValueError("Invalid edge")
        return self.__cost[edge]

    def set_cost(self, edge, value):
        if self.__cost.get(edge) is None:
            raise ValueError("Invalid edge")
        self.__cost[edge] = value

    def copy(self):
        return deepcopy(self)
