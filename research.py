import networkx as nx
import matplotlib.pyplot as plt

# Create a graph
G = nx.DiGraph()
edges = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 1)]
G.add_edges_from(edges)

# Define a walk that satisfies node-omnitig conditions
node_omnitig_walk = [1, 2, 3, 4, 5, 1]


# Check if the walk is a node-omnitig
def is_node_omnitig(graph, walk):
    for i in range(1, len(walk)):
        vi, ei = walk[i - 1], walk[i]
        for j in range(i, len(walk)):
            vj, ej = walk[j - 1], walk[j]
            # Condition 1
            if graph.has_edge(vj, vi) and ej != graph[vj][vi]['attr']:
                return False
    for j in range(len(walk)):
        vj, ej = walk[j - 1], walk[j]
        # Condition 2
        if list(graph.neighbors(vj)) != [vi for vi in graph.neighbors(vj)]:
            return False
    return True


def compute_node_covering_circular_walk(graph):
    # Assuming G is strongly connected
    return list(nx.simple_cycles(graph))[0]


def compute_certificates(graph):
    certificates = {}
    for node in graph.nodes:
        certificates[node] = set(graph.in_edges(node))
    return certificates


def compute_node_safe_walks(graph):
    # Step 1: Compute node-covering circular walk C
    circular_walk = compute_node_covering_circular_walk(graph)

    # Step 2: Compute Cert(v) for every v in V(G)
    certificates = compute_certificates(graph)

    # Step 3: Compute node-safe walks
    n = len(graph.nodes)
    d = len(circular_walk)
    node_safe_walks = []

    for k in range(1, n + 1):
        Sk = set()

        for i in range(d):
            if k & (1 << i):
                if nx.has_path(graph, circular_walk[i], circular_walk[(i + 1) % d]):
                    continue

                if certificates[circular_walk[i]] & certificates[circular_walk[(i + 1) % d]] == set():
                    Sk.add(i)
                else:
                    if i in Sk and (i + 1) % d in Sk:
                        first_edge = circular_walk[i]
                        last_edge = circular_walk[(i + k - 1) % d]
                        path_exists = nx.has_path(graph, first_edge, last_edge)

                        if not path_exists:
                            node_safe_walks.append((i, k))

    return circular_walk, node_safe_walks


# Example usage:
G = nx.DiGraph()
G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 1)])

node_covering_walk, node_safe_walks = compute_node_safe_walks(G)

print("Node-Covering Circular Walk:", node_covering_walk)
print("Node-Safe Walks:")
for i, k in node_safe_walks:
    print(f"C({i}, {k}) is node-safe")