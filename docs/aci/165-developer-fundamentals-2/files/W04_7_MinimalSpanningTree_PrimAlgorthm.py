from typing import List, Tuple

class Graph: 
    def __init__(self, vertices: int) -> None: 

        self.vertices = vertices 
        self.adjacency_list = [[] for _ in range(vertices)] 
  
    def add_edge(self, u: int, v: int, weight: int) -> None: 
       
        self.adjacency_list[u].append((v, weight)) 
        self.adjacency_list[v].append((u, weight)) 

    def prim_mst(self) -> List[Tuple[int, int, int]]: 

        priority_queue = [(0, 0)]  # (weight, vertex) 
        visited = set() 
        mst_edges = [] 

        while priority_queue:
            priority_queue.sort()  # Sort the priority queue by weight 
            weight, current_vertex = priority_queue.pop(0)

            if current_vertex not in visited:
                visited.add(current_vertex)
 
            for neighbor, edge_weight in self.adjacency_list[current_vertex]: 
               if neighbor not in visited: 
                  priority_queue.append((edge_weight, neighbor)) 
                  mst_edges.append((current_vertex, neighbor, edge_weight)) 
 
        return mst_edges

# Example usage: 
if __name__ == "__main__": 
    # Example of usage 
    g = Graph(5) 
 
    # Add edges 
    g.add_edge(0, 1, 2) 
    g.add_edge(0, 2, 4) 
    g.add_edge(1, 2, 1) 
    g.add_edge(1, 3, 5) 
    g.add_edge(2, 3, 8) 
    g.add_edge(2, 4, 3) 
    g.add_edge(3, 4, 7) 

    # Print adjacency list for each vertex 
    for i in range(g.vertices):
        print(f"Vertex {i}: {g.adjacency_list[i]}")
 
    # Find the Minimum Spanning Tree (MST) using Prim's algorithm 
    mst_edges = g.prim_mst() 
    print("Minimum Spanning Tree (MST) Edges:") 
    for edge in mst_edges: 
        print(edge) 


