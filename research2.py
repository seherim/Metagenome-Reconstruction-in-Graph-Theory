import networkx as nx
import random
import matplotlib.pyplot as plt

def node_safe_walk(graph):
    if not nx.is_strongly_connected(graph):
        raise ValueError("The graph is not strongly connected.")

    # 1. Get the circular path created in the graph
    circular_path = list(nx.simple_cycles(graph))[0]

    # 2. Initialize certificates for each vertex
    cert = {v: [v] for v in graph.nodes()}

    # 3. Loop for each vertex
    for i in range(len(graph.nodes())):
        # 4. Set Sk to empty set
        Sk = set()

        # 5. Loop for each edge
        for j in range(len(graph.edges())):
            # 6-9. Check conditions for the first edge
            if j == 0:
                if (circular_path[j], circular_path[(j + 1) % len(circular_path)]) == (circular_path[0], circular_path[1]):
                    Sk.add(j)

            # 11. Check conditions for other edges
            elif (j - 1) in Sk and j % len(circular_path) in Sk:
                # Assume l is the length of the graph
                l = len(graph.edges())
                condition = True  # Modify this condition based on the pseudocode
                if condition:
                    Sk.add(j)

            # 12. Check if Cert(vi) ∩ ... ∩ Cert(vi+k mod d) is not empty
            if all(cert[circular_path[i]] for i in Sk):
                Sk = Sk.union(Sk)

        # 13. Update Sk
        Sk = Sk.union({i})

    # Print the result (you may modify this based on how you want to use the result)
    print("Node-Safe Walk Indices:", Sk)
    node_safe_walk_sequence = [circular_path[i] for i in Sk]
    print("Node-Safe Walk Sequence:", node_safe_walk_sequence)

    # Visualize the graph
    plt.figure(figsize=(12, 6))
    pos = nx.spring_layout(graph)
    nx.draw_networkx(graph, pos, with_labels=True, node_size=1200, node_color='r', edge_color='gray')
    plt.title("Strongly Connected Directed Graph", color='forestgreen', fontsize=18, fontname='Calibri')
    plt.show()

# Example usage
G = generate_strongly_connected_graph(5, 12, seed=42)
node_safe_walk(G)
