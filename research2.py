import networkx as nx
import random
import matplotlib.pyplot as plt

def generate_strongly_connected_graph(num_nodes, seed=None):
    # Generate an undirected graph
    G_undirected = nx.gn_graph(num_nodes, seed=seed)

    # Convert the undirected graph to a directed graph
    G_directed = nx.DiGraph(G_undirected)

    # Ensure the directed graph is strongly connected
    while not nx.is_strongly_connected(G_directed):
        # Regenerate the directed graph until it is strongly connected
        G_directed = nx.DiGraph(nx.gn_graph(num_nodes, seed=seed))

    return G_directed

def compute_certificates(graph, circular_path):
    n = len(graph.nodes)
    d = len(circular_path)

    # Initialize the certificates array
    cert = [set() for _ in range(n)]

    # Convert circular_path to a set for faster membership tests
    circular_set = set(circular_path)

    # Loop over vertices
    for i in range(n):
        # Initialize the set of indices
        Sk = set()

        # Loop over edges
        for l in range(d):
            # For the first edge (k=1)
            if l == 0:
                if is_only_edge(graph, circular_path, i, l):
                    common_vertices = circular_set.intersection(circular_path[1:])
                    if common_vertices:
                        Sk.add(i)
                        cert[i].update(common_vertices)
            else:
                # Check conditions for node-omnitig
                if i in Sk and (i + 1) % d in Sk and not has_subgraph(graph, circular_path, i, l):
                    common_cert = cert[i].intersection(cert[(i + 1) % d])
                    if common_cert:
                        Sk.add(i)
                        cert[i].update(common_cert)

        # Update the certificates array
        Sk.add(i)
        cert[i].update(Sk)

    return cert

def is_only_edge(graph, circular_path, i, l):
    edge = (circular_path[i], circular_path[(i + l) % len(circular_path)])
    return graph.has_edge(*edge) and len(graph.in_edges(circular_path[i])) == 1 and len(graph.out_edges(circular_path[(i + l) % len(circular_path)])) == 1

def has_subgraph(graph, circular_path, i, l):
    first_edge = (circular_path[i + l - 1] % len(circular_path), circular_path[(i + l) % len(circular_path)])
    last_edge = (circular_path[(i + l) % len(circular_path)], circular_path[i])

    # Check if there is a subgraph with the specified conditions
    return nx.has_path(graph, *first_edge) and nx.has_path(graph, *last_edge)

# Example usage
num_nodes = 10
graph = generate_strongly_connected_graph(num_nodes, seed=42)
circular_path = list(nx.circular_layout(graph))
certificates = compute_certificates(graph, circular_path)

# Print certificates for each vertex
for i, cert in enumerate(certificates):
    print(f"Cert({i}): {cert}")
