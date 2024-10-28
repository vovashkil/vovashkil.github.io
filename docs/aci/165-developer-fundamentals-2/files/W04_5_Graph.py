from typing import Dict, List, Tuple

graph: Dict[str, List[str]] = {
    'a': ['b', 'c'],
    'b': ['a', 'd'], 
    'c': ['a', 'd'],
    'd': ['b', 'c', 'e'],
    'e': ['d'],
    'f': []
}

def add_edge(start_vertex: str, end_vertex: str, graph: Dict[str, List[str]]) -> Dict[str, List[str]]:

    if start_vertex in graph.keys() and end_vertex in graph[start_vertex] and \
        end_vertex in graph.keys() and start_vertex in graph[end_vertex]:
        print(f'Edge {start_vertex} -> {end_vertex} is already present')
        return graph
    
    if start_vertex not in graph.keys():
        graph[start_vertex] = []
    if end_vertex not in graph.keys():
        graph[end_vertex] = []

    graph[start_vertex].append(end_vertex)
    graph[end_vertex].append(start_vertex)

    return graph

def print_graph(graph: Dict[str, List[str]]) -> None:

    vertices: List[str] = list(graph.keys())
    edges: List[Tuple[str, str]] = []

    for vertex in graph:
        for item in graph[vertex]:
            if (vertex, item) not in edges:
                edges.append((vertex, item))

    print(f'Vertices: {vertices}')
    print(f'Edges: {edges}')

if __name__ == '__main__':
    print('Original graph')
    print_graph(graph)    

    print('---')

    graph = add_edge('a', 'b', graph)
    graph = add_edge('d', 'f', graph)
    graph = add_edge('x', 'y', graph)

    print('---')

    print('Graph after adding new edges')
    print_graph(graph)