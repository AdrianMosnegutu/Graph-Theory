import random

from src.application.graphs.undirected_graph import UndirectedGraph


class UndirectedGraphService:
    @staticmethod
    def read_graph_from_file(file_path):
        with open(file_path, "r") as input_file:
            vertices, edges = input_file.readline().strip().split(" ")
            vertices, edges = int(vertices), int(edges)

            graph = UndirectedGraph(vertices)

            for _ in range(edges):
                start, end, = input_file.readline().strip().split(" ")
                start, end = int(start), int(end)
                graph.add_edge((start, end))

            return graph

    @staticmethod
    def write_graph_to_file(graph, file_path):
        with open(file_path, "w") as output_file:
            vertices, edges = graph.vertices_count, graph.edges_count
            output_file.write(f"{vertices} {edges}\n")

            for edge in graph.edges:
                start, end = edge
                output_file.write(f"{start} {end}\n")

    @staticmethod
    def generate_random_graph(vertices, edges):
        graph = UndirectedGraph(vertices)
        free_edges = [(start, end) for start in range(vertices) for end in range(vertices) if start != end]
        generated_edges = []

        for _ in range(edges):
            edge = random.choice(free_edges)
            free_edges.remove(edge)

            generated_edges.append(edge)

        generated_edges = sorted(generated_edges, key=lambda x: x[0])

        for edge in generated_edges:
            graph.add_edge(edge)

        return graph
