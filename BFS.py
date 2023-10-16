from collections import defaultdict, deque
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    def add_edge(self, vertex, neighbor):
        self.graph[vertex].append(neighbor)
    def bfs(self, start_vertex):
        visited = set()
        queue = deque()
        visited.add(start_vertex)
        queue.append(start_vertex)
        while queue:
            current_vertex = queue.popleft()
            print(current_vertex, end=" ")
            for neighbor in self.graph[current_vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
if __name__ == "__main__":
    # Create a graph
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)
    start_vertex = 2  # Starting vertex for BFS
    print("Breadth-First Traversal (starting from vertex", start_vertex, "):")
    g.bfs(start_vertex)




###The code you’ve written is a Python implementation of the Breadth-First Search (BFS) algorithm for traversing or searching tree or graph data structures.

Here’s a step-by-step explanation of the code:

The Graph class is defined with methods to initialize the graph (__init__), add an edge to the graph (add_edge), and perform a breadth-first search from a given start vertex (bfs).
In the __init__ method, the graph is initialized as a default dictionary of lists. This allows you to easily add edges to the graph.
The add_edge method adds an edge to the graph by appending the neighbor vertex to the list of neighbors for the given vertex.
The bfs method performs a breadth-first search from the given start vertex. It uses a queue to keep track of vertices to visit next, and a set to keep track of visited vertices.
In the main part of the code, a Graph object is created, edges are added to the graph, and then a breadth-first search is performed from a given start vertex.
The output of this code will be the vertices of the graph printed in the order they are visited by the BFS algorithm, starting from the given start vertex.
