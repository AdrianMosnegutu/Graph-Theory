from queue import Queue

from src.graphs.directed_graph import DirectedGraph
from src.services.directed_graph_service import DirectedGraphService


class Kosaraju:
    __graph: DirectedGraph

    def run(self):
        """
        Reads a directed graph from a file and displays its strongly connected components.
        """

        self.__graph = DirectedGraphService.read_graph_from_file("database/scc_data.txt")
        ans = self.__get_strongly_connected_components()
        print("Strongly connected components:")
        for index, components in enumerate(ans):
            print(f"[{index}]: {components}")

    def __create_reverse_depth_vertex_list(self, vertex, visited, processed):
        """
        Performs depth first search on the graph in order to create a stack that contains
        the vertices in reverse order of depth from the starting vertex.

        :type vertex: int
        :param vertex: The vertex to start the depth first search from

        :type visited: set
        :param visited: The set keeping track of all the vertices we have visited during the search

        :type processed: list[int]
        :param processed: The stack containing the elements in reverse order of depth

        :rtype: None
        """

        for neighbour in self.__graph.outbound_neighbours(vertex):
            if neighbour not in visited:
                visited.add(neighbour)
                self.__create_reverse_depth_vertex_list(neighbour, visited, processed)
        processed.append(vertex)

    def __get_strongly_connected_components(self):
        """
        Gets the strongly connected components of a graph using Kosaraju's algorithm.

        :rtype: list[list[int]]
        :returns: A list of lists where each list represents a strongly connected component
        and contains the vertices in that component
        """

        components = list()
        queue = Queue()
        visited = set()
        processed = list()

        # Create the stack in which vertices are sorted in reverse order of time to get to them from node 0 through DFS
        for vertex in self.__graph.vertices:
            if vertex not in visited:
                visited.add(vertex)
                self.__create_reverse_depth_vertex_list(vertex, visited, processed)

        visited.clear()

        while not len(processed) == 0:
            # Get the vertex closest to the root
            top = processed.pop()
            if top in visited:
                continue

            queue.put(top)
            visited.add(top)
            components.append([top])

            # Perform BFS in order to mark the whole SCC as visited and the vertices to the dictionary
            while not queue.empty():
                vertex = queue.get()
                for neighbour in self.__graph.inbound_neighbours(vertex):
                    if neighbour not in visited:
                        visited.add(neighbour)
                        queue.put(neighbour)
                        components[-1].append(neighbour)

        return components
