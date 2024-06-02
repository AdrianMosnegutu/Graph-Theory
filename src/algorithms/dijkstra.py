from queue import PriorityQueue

from src.graphs.directed_graph import DirectedGraph
from src.services.directed_graph_service import DirectedGraphService


class Dijkstra:
    __graph: DirectedGraph

    def run(self):
        """
        Reads a directed graph, a source vertex and a destination vertex from a file and displays the minimum
        cost walk from the source vertex to the destination vertex using the Dijkstra algorithm.
        """

        self.__graph = DirectedGraphService.read_graph_from_file("database/shortest_path_data.txt")
        source = int(input("Source vertex: "))
        destination = int(input("Destination vertex: "))

        min_cost_walk, cost = self.__get_minimum_cost_walk(source, destination)
        print(f"Minimum cost walk from {source} to {destination}: {min_cost_walk}")
        print(f"Cost: {cost}")

    def __get_minimum_cost_walk(self, source, destination):
        """
        Calculates the minimum cost walk from a source vertex to a destination vertex using the Dijkstra algorithm.

        :type source: int
        :param source: The source vertex

        :type destination: int
        :param destination: The destination vertex

        :rtype: tuple[list[int], int]
        :returns: A tuple containing the minimum cost walk from the source vertex to the destination vertex
        and the cost of the walk
        """

        # Initialize the distance and previous vertex dictionaries
        dist = {vertex: float('inf') for vertex in self.__graph.vertices}
        prev = {}
        q = PriorityQueue()

        q.put((0, source))
        dist[source] = 0

        # Traverse the graph using Dijkstra's algorithm
        while not q.empty():
            vertex = q.get()[1]
            if vertex == destination:
                break

            # Traverse the neighbours of the current vertex and update the distance and previous vertex dictionaries
            for neighbour in self.__graph.outbound_neighbours(vertex):
                cost = self.__graph.get_cost((vertex, neighbour))
                if neighbour not in dist or dist[vertex] + cost < dist[neighbour]:
                    dist[neighbour] = dist[vertex] + cost
                    q.put((dist[neighbour], neighbour))
                    prev[neighbour] = vertex

        # If the destination vertex is unreachable, return None and infinity
        if dist[destination] == float('inf'):
            return None, float('inf')

        min_cost_walk = []
        vertex = destination

        # Reconstruct the minimum cost walk
        while vertex != source and prev:
            min_cost_walk.append(vertex)
            vertex = prev[vertex]

        min_cost_walk.append(source)
        return min_cost_walk[::-1], dist[destination]
