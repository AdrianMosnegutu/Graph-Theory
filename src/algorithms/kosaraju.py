from src.graphs.directed_graph import DirectedGraph
from src.services.directed_graph_service import DirectedGraphService
from queue import Queue


class Kosaraju:
    __graph: DirectedGraph

    def run(self):
        """ Read a directed graph from a file and display its strongly connected components. """

        self.__graph = DirectedGraphService.read_graph_from_file("database/graph.txt")
        scc = self.__get_strongly_connected_components()

        print("Strongly connected components:")
        for key, value in scc.items():
            print(f"[{key}]: {value}")

    def __create_reverse_depth_vertex_list(self, vertex, visited, processed):
        """
        Start from a given vertex and traverse the graph depth-first in order to create a stack that contains
        the vertices in reverse order of depth from the starting vertex.

        :type vertex: int
        :param vertex: the starting vertex for the depth first search

        :type visited: set
        :param visited: the set keeping track of all the vertices we have visited during the search

        :type processed: list[int]
        :param processed: the stack containing the elements in reverse order of depth

        :rtype: None
        """

        for neighbour in self.__graph.outbound_neighbours(vertex):
            if neighbour not in visited:
                visited.add(neighbour)
                self.__create_reverse_depth_vertex_list(neighbour, visited, processed)
        processed.append(vertex)

    def __get_strongly_connected_components(self):
        """
        Get the strongly connected components of a graph using Kosaraju's algorithm.

        :rtype: dict[int, list[int]]
        :return: a dictionary where the keys represent the id of the strongly connected component and the value is
        """

        queue = Queue()
        components = dict()
        visited = set()
        processed = list()
        component_count = 0

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

            component_count += 1
            components[component_count] = [top]

            # Perform BFS in order to mark the whole SCC as visited and the vertices to the dictionary
            while not queue.empty():
                vertex = queue.get()
                for neighbour in self.__graph.inbound_neighbours(vertex):
                    if neighbour not in visited:
                        visited.add(neighbour)
                        queue.put(neighbour)
                        components[component_count].append(neighbour)

        return components
