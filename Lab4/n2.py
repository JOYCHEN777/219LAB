import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_nodes_from([1, 2, 3, 4, 5])
G.add_edges_from([(1, 2), (1, 5), (2, 3), (2, 5), (3, 4), (4, 5)])

print('edges:',G.edges())
nx.draw(G,with_labels=True,pos=nx.spectral_layout(G))
plt.show()
