from src.graphs.directed_graph import DirectedGraph
from src.services.directed_graph_service import DirectedGraphService


class Tarjan:
    __graph: DirectedGraph

    def run(self):
        """
        Reads a directed graph from a file and displays its strongly connected components.
        """

        self.__graph = DirectedGraphService.read_graph_from_file("database/graph.txt")
        ans = self.__get_strongly_connected_components()

        print("Strongly connected components:")
        for index, components in enumerate(ans):
            print(f"[{index}]: {components}")

    def __generate_low_links_dfs(self, vertex, visited, low_link):
        """
        Performs depth first search on the graph in order to calculate the low link values for each vertex.
        The low link value of a vertex is the smallest vertex (in terms of id) that can be reached from the vertex

        :type vertex: int
        :param vertex: The vertex to start the depth first search from

        :type visited: list[int]
        :param visited: The list of vertices that have been visited

        :type low_link: dict[int, int]
        :param low_link: A dictionary containing the low link values for each vertex

        :rtype: None
        """

        # Mark the vertex as visited and set its low link value to itself
        visited.append(vertex)
        low_link[vertex] = vertex

        # Traverse the neighbours of the vertex
        for neighbour in self.__graph.outbound_neighbours(vertex):
            if neighbour not in visited:
                # Recursively call the function on the neighbour and update the low link value of the vertex
                self.__generate_low_links_dfs(neighbour, visited, low_link)
                low_link[vertex] = min(low_link[vertex], low_link[neighbour])

        # If the low link value of the vertex is equal to itself, it is the root of a strongly connected component
        if low_link[vertex] == vertex:
            current = visited.pop() if visited else 0
            # Update the low link values of the vertices in the strongly connected component
            while visited:
                low_link[current] = vertex
                current = visited.pop()

    def __get_strongly_connected_components(self):
        """
        Gets the strongly connected components of a graph using Tarjan's algorithm.

        :rtype: dict[int, list[int]]
        :returns: A dictionary where the keys represent the id of the strongly connected component
        and the value is a list consisting of the vertices in that respective component
        """

        components = list()
        visited = list()
        low_link = dict()
        component_order = dict()
        component_count = -1

        # Generate the low link values for each vertex in the graph
        for vertex in self.__graph.vertices:
            if vertex not in visited:
                self.__generate_low_links_dfs(vertex, visited, low_link)

        # Create a dictionary containing the vertices of each strongly connected component based on the low link values
        for vertex in self.__graph.vertices:
            if low_link[vertex] not in component_order:
                component_count += 1
                component_order[low_link[vertex]] = component_count
                components.append([vertex])
            else:
                components[component_order[low_link[vertex]]].append(vertex)

        return components
