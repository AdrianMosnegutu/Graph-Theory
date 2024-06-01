import timeit

from algorithms.kosaraju import Kosaraju
from algorithms.tarjan import Tarjan


if __name__ == "__main__":
    kosaraju_time = timeit.timeit(Kosaraju().run, number=1)
    print(f"Kosaraju's algorithm took {kosaraju_time} seconds to run.", end="\n\n")

    tarjan_time = timeit.timeit(Tarjan().run, number=1)
    print(f"Tarjan's algorithm took {tarjan_time} seconds to run.", end="\n\n")

    print(f"Tarjan's algorithm was {kosaraju_time / tarjan_time:.2f} times faster than Kosaraju's algorithm.")
