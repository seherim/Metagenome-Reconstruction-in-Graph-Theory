import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def graphex(gg):
    while True:
        gg = sorted(gg, reverse=True)
        if gg[0] == 0 and gg[-1] == 0:
            return True

        var = gg[0]
        gg = gg[1:]

        if var > len(gg):
            return False
        for i in range(var):
            gg[i] -= 1
            if gg[i] < 0:
                return False

def havelhakimi(degreeseq):
    while True:
        degreeseq = sorted(degreeseq, reverse=True)
        if degreeseq[0] == 0 and degreeseq[-1] == 0:
            return True, degreeseq
        v = degreeseq[0]
        degreeseq = degreeseq[1:]
        if v > len(degreeseq):
            return False, degreeseq
        for i in range(v):
            degreeseq[i] -= 1
            if degreeseq[i] < 0:
                return False, degreeseq

# Original graph
graph = nx.Graph()

# Nodes in the graph
graph_nodes = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}
graph.add_nodes_from(graph_nodes)

# generating random edges
E = zip(np.random.choice(list(graph_nodes), 10), np.random.choice(list(graph_nodes), 10))
graph.add_edges_from(E)

# removing self-loops
graph.remove_edges_from(nx.selfloop_edges(graph))

# original degree sequence
initialdegseqq = list(dict(graph.degree()).values())
print("Initial Degree Sequence:", initialdegseqq)

# initial graph show
initial_position = nx.spring_layout(graph, k=1)
plt.figure(figsize=(12, 6))
nx.draw_networkx(graph, initial_position, with_labels=True, node_size=1200, node_color='r', edge_color='gray')
plt.title("- Initial Graph -")
print("Initial Degree Sequence:", initialdegseqq)
initialseq = "Constructed Graphical Sequence: " + str(initialdegseqq)
plt.text(0.5, -0.1, initialseq, ha='center', va='center', transform=plt.gca().transAxes)
plt.show()

# Havel-Hakimi process
exists, new_sequence = havelhakimi(initialdegseqq)

while exists and not graphex(new_sequence):
    print("Intermediate Sequence:", new_sequence)
    exists, new_sequence = havelhakimi(new_sequence)

if exists:
    print("The degree sequence is graphical.")
    print("Constructed Graphical Sequence:", new_sequence)

    # New graph on the modified sequence after Havel-Hakimi
    new_graph = nx.configuration_model(new_sequence, create_using=nx.Graph())

    # Add edges from the original graph to the new graph
    new_graph.add_edges_from(E)

    # Visualize the new graph
    new_position = nx.spring_layout(new_graph, k=1)

    plt.figure(figsize=(12, 6))
    nx.draw_networkx(new_graph, new_position, with_labels=True, node_size=1200, node_color='r', edge_color='gray')
    plt.title("- Graph Constructed Using Havel-Hakimi -")
    finalseq = "Constructed Graphical Sequence: " + str(new_sequence)
    plt.text(0.5, -0.1, finalseq, ha='center', va='center', transform=plt.gca().transAxes)

    plt.show()

else:
    finalwrong = "The degree sequence is not graphical."
    plt.text(0.4, 0.1, finalwrong, ha='center', va='center', transform=plt.gca().transAxes)

