import networkx as netx
import pandas as pd
import numpy as np
import matplotlib.pyplot as pyp

from networkx.drawing.layout import bipartite_layout

# hardcoding values for the bipartite (need to change to randomized)
bp1 = {1, 2, 3, 4, 5}
bp2 = {6, 7, 8, 9, 10}
bp3 = {11, 12, 13, 14, 15}

# forming a random combination
Ebi = zip(np.random.choice(list(bp1), 10), np.random.choice(list(bp2), 10))

Ebi = list(Ebi)
# print(E)

# printing all the connections/edges
edge = pd.DataFrame([{"s": bp1, "t": bp2} for bp1, bp2 in Ebi])
# print(edge)

# establishing our graph - directed graph
graph = netx.DiGraph()
graph.add_nodes_from(bp1, bipartite=0)
graph.add_nodes_from(bp2, bipartite=2)

graph.add_edges_from(tuple(x) for x in edge.values)
 # print(graph.edges)

 # for tripartite graphs
Etri = zip(np.random.choice(list(bp1), 10), np.random.choice(list(bp2), 10), np.random.choice(list(bp3), 10))

Etri = list(Etri)

# Printing all the connections/edges for tripartite graph
edgestri = pd.DataFrame([{"s": s, "t": t, "u": u} for s, t, u in Etri])

graphtri = netx.DiGraph()
graphtri.add_nodes_from(bp1, bipartite=0)
graphtri.add_nodes_from(bp2, bipartite=1)
graphtri.add_nodes_from(bp3, bipartite=2)
edges_tri = [(row['s'], row['t']) for _, row in edgestri.iterrows()] + [(row['t'], row['u']) for _, row in edgestri.iterrows()]

graphtri.add_edges_from(edges_tri)

positionbp = bipartite_layout(graph, bp1)
positionbp1 = {node: (1, i) for i, node in enumerate(bp1)}
positionbp2 = {node: (2, i) for i, node in enumerate(bp2)}
positionbp3 = {node: (3, i) for i, node in enumerate(bp3)}
positiontri = {**positionbp1, **positionbp2, **positionbp3}


# Drawing bipartite graph
pyp.figure(figsize=(12, 6))
pyp.subplot(1, 2, 1)
netx.draw_networkx(graph, positionbp, with_labels=True, node_size=1200, node_color='m', edge_color='r', arrowsize=20)
pyp.title("Bipartite Graph")

# Drawing tripartite graph
pyp.subplot(1, 2, 2)
netx.draw_networkx(graphtri, positiontri, with_labels=True, node_size=1200, node_color='c', edge_color='b', arrowsize=20)
pyp.title("Tripartite Graph")

pyp.show()