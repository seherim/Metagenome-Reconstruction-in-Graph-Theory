
# first we generate a connected graph which is directed
# (hence the use of the word strong)

# 1
# store the circular path created in the graph in a variable

# 2
# cert is basically an array that holds sequences for a walk for each vertice in graph

# 3
# loop for 1 till n
# n is the number of vertices

# 4
# the Sk = expression just represents adding the element i into the set of Sk

# 5
# d is the length of the graph . aka the number of edges present in the graph
# so we start from 0 to the number of edges - 1

# 6 to 9
# k = 1 so for the first edge
# if that particular edge is the only thing connecting v1 vertice and the next one
# then if the circular path from that vertice and the circular path from the next vertice are combined and their common vertices are not empty/0
# Sk ∪ i is a way of indicating the current set of indices under consideration in the algorithm, where
# Sk represents the indices from the previous iteration, and
# i is the current index being processed.

# 11
# if i is an element of Sk-1
# and i+1%d is also an element
# and there is no subgraph whose first edge is different than the edge in e(i+l-1 % d)
# and last edge different than ei
# for this its just a calculation from the array where the information is stored
# 12
# this again just makes sure every single cycle in cert for those vertices mentioned have atleast SOME vertices in common, so it is not 0 basically

# 13
# the Sk = expression just represents adding the element i into the set of Sk