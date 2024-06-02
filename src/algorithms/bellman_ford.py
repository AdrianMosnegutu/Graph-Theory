from src.graphs.directed_graph import DirectedGraph
from src.services.directed_graph_service import DirectedGraphService

class BellmanFord:
    __graph: DirectedGraph

    def run(self):
        """
        Reads a directed graph, a source vertex and a destination vertex from a file and displays the minimum
        cost walk from the source vertex to the destination vertex using the Bellman-Ford algorithm.
        """

        self.__graph = DirectedGraphService.read_graph_from_file("database/shortest_path_data.txt")
        source = int(input("Source vertex: "))
        destination = int(input("Destination vertex: "))

        min_cost_walk, cost = self.__get_minimum_cost_walk(source, destination)
        print(f"Minimum cost walk from {source} to {destination}: {min_cost_walk}")
        print(f"Cost: {cost}")

    def __get_minimum_cost_walk(self, source, destination):
        """
        Calculates the minimum cost walk from a source vertex to a destination vertex using the Bellman-Ford algorithm.

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

        # Set the distance of the source vertex to 0
        dist[source] = 0
        changed = True

        # Relax the edges until no more changes can be made
        while changed:
            changed = False

            # Traverse all the edges
            for start, end in self.__graph.edges:
                if dist[end] > dist[start] + self.__graph.get_cost((start, end)):
                    dist[end] = dist[start] + self.__graph.get_cost((start, end))
                    prev[end] = start
                    changed = True

        # If the destination vertex is unreachable, return None and infinity
        if dist[destination] == float('inf'):
            return None, float('inf')

        min_cost_walk = []
        vertex = destination

        # Reconstruct the minimum cost walk
        while vertex != source and prev:
            min_cost_walk.append(vertex)
            vertex = prev[vertex]

        return min_cost_walk[::-1], dist[destination]
