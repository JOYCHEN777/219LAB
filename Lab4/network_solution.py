import networkx as nx
import matplotlib.pyplot as plt

# Create empty directed graph
G = nx.DiGraph()

# Add graph vertices
G.add_nodes_from([1, 4, 9, 11, 14, 18, 20, 21, 28])

# Add graph edges corresponding to ring topology
G.add_edges_from([(1, 4), (4, 9), (9, 11), (11,14), (14, 18), (18, 20), (20, 21), (21, 28), (28, 1)])

# Draw the graph
nx.draw(G, with_labels=True, pos=nx.spectral_layout(G))
plt.show()

# Compute and print the distances from vertex 1 to each other vertex.
print("Distances from vertex 1 to each other vertex (ring topology)")
length = dict(nx.all_pairs_dijkstra_path_length(G))
for vertex in [1, 4, 9, 11, 14, 18, 20, 21, 28]:
	print('1 - {}: {}'.format(vertex, length[1][vertex]))
print()


# Add an addional shortcut edge from vertex 1 to vertex 18
G.add_edges_from([(1, 18)])

# Draw the graph
nx.draw(G, with_labels=True, pos=nx.spectral_layout(G))
plt.show()

# Compute and print the distances from vertex 1 to each other vertex.
print("Distances from vertex 1 to each other vertex (ring topology with single shortcut edge)")
length = dict(nx.all_pairs_dijkstra_path_length(G))
for vertex in [1, 4, 9, 11, 14, 18, 20, 21, 28]:
	print('1 - {}: {}'.format(vertex, length[1][vertex]))

# Compare the above distances for the graph with ring topology and the graph with ring topology plus shortcut edge.
# You can see that addition of a single shortcut edge reduces the distances significantly.
# For example, the distance from vertex 1 to vertex 28 is reduced from 8 to 4.
