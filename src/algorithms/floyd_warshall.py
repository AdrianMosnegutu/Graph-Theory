from src.graphs.directed_graph import DirectedGraph
from src.services.directed_graph_service import DirectedGraphService

class FloydWarshall:
    __graph: DirectedGraph

    def run(self):
        """
        Reads a directed graph from a file and displays the shortest path matrix using the Floyd-Warshall algorithm.
        """

        self.__graph = DirectedGraphService.read_graph_from_file("database/shortest_path_data.txt")
        cost, prev = self.__get_shortest_path_matrix()

        print("Shortest path matrix:")
        for row in self.__graph.vertices:
            for column in self.__graph.vertices:
                print(f"{(cost[row, column] if cost[row, column] != float('inf') else '-'):>4}", end=" ")
            print()

        print("\nNext vertex matrix:")
        for row in self.__graph.vertices:
            for column in self.__graph.vertices:
                print(f"{prev.get((row, column), '-'):>4}", end=" ")
            print()

    def __get_shortest_path_matrix(self):
        """
        Calculates the shortest path matrix using the Floyd-Warshall algorithm.

        :rtype: tuple[dict[tuple[int, int], int], dict[tuple[int, int], int]]
        :returns: A tuple containing the cost and next vertex dictionaries
        """

        cost = {}
        next_vertex = {}

        # Initialize the cost and previous vertex dictionaries
        for source in self.__graph.vertices:
            for destination in self.__graph.vertices:
                # The cost of a vertex to itself is 0
                if source == destination:
                    cost[source, destination] = 0
                # The cost of a vertex to its neighbours is the cost of the edge connecting them
                elif self.__graph.are_connected(source, destination):
                    cost[source, destination] = self.__graph.get_cost((source, destination))
                    next_vertex[source, destination] = destination
                # The cost of a vertex to vertices it is not directly connected to is infinity
                else:
                    cost[source, destination] = float('inf')

        # Calculate the shortest path matrix using the Floyd-Warshall algorithm
        for intermediary in self.__graph.vertices:
            for source in self.__graph.vertices:
                for destination in self.__graph.vertices:
                    # Update the cost and next vertex dictionaries if a shorter path is found
                    if cost[source, destination] > cost[source, intermediary] + cost[intermediary, destination]:
                        cost[source, destination] = cost[source, intermediary] + cost[intermediary, destination]
                        next_vertex[source, destination] = next_vertex[source, intermediary]

        return cost, next_vertex
