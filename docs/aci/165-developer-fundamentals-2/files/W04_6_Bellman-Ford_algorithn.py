
from typing import List, Tuple

class Graph: 
    def __init__(self, vertices: int) -> None: 
        self.vertices = vertices 
        self.graph: List[Tuple[int, int, int]] = [] 
 
    def add_edge(self, u: int, v: int, w: int) -> None: 
        self.graph.append((u, v, w)) 
 
    def bellman_ford(self, source: int) -> None: 
        distances = [float('inf')] * self.vertices 
        distances[source] = 0 
 
        for _ in range(self.vertices - 1): 
            for u, v, w in self.graph: 
                if distances[u] != float('inf') and distances[u] + w < distances[v]: 
                    distances[v] = distances[u] + w 
 
        for u, v, w in self.graph: 
            if distances[u] != float('inf') and distances[u] + w < distances[v]: 
                print("Graph contains negative weight cycle") 
                return 
 
        print("Shortest distances from source vertex:") 
        for i in range(self.vertices): 
            print(f"Vertex {i} -> Distance: {distances[i]}") 
 
    def dump(self) -> None: 
        for u, v, w in self.graph: 
            print(f"{u} --({w})--> {v}") 
     
    def dump_graphviz(self, filename: str = 'graphviz_output.dot') -> None: 
        with open(filename, 'w') as f: 
            f.write('digraph G {\n') 
            for u, v, w in self.graph: 
                f.write(f'  {u} -> {v} [label="{w}"];\n') 
            f.write('}\n') 
 
 
if __name__ == '__main__': 
    # Example usage: 
    g = Graph(5) 
 
    # Add edges 
    g.add_edge(0, 1, 2) 
    g.add_edge(0, 2, 4) 
    g.add_edge(1, 3, 2) 
    g.add_edge(2, 4, 3) 
    g.add_edge(2, 3, 4) 
    g.add_edge(4, 3, -5) 
 
    # Visualize the graph 
    g.dump() 
    g.dump_graphviz() 
 
    # Run the Bellman-Ford algorithm 
    source_vertex = 0 
    g.bellman_ford(source_vertex) 