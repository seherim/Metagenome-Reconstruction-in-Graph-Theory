import networkx as netx
import matplotlib.pyplot as pyp
import networkx as nx
import numpy as np
import pandas as pd

graph = netx.Graph()

# nodes in the graph
graphnode = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}
graph.add_nodes_from(graphnode)

E = zip(np.random.choice(list(graphnode), 10), np.random.choice(list(graphnode), 10))
graph.add_edges_from(E)

# removes any self loop
graph.remove_edges_from(netx.selfloop_edges(graph))

cgraph = nx.Graph()
# code for creating a complete graph
for node1 in graph.nodes():
    for node2 in graph.nodes():
        if node1 != node2 and not graph.has_edge(node1, node2):
            cgraph.add_edge(node1, node2)

position = nx.spring_layout(cgraph, k=1)

pyp.figure(figsize=(12, 6))
netx.draw_networkx(cgraph, position, with_labels=True, node_size=1200, node_color='r', edge_color='gray')

pyp.title(" Complete Graph ", color = 'forestgreen', fontsize = 18, fontname = 'Calibri')
pyp.show()