import networkx as nx
import matplotlib.pyplot as plt

# create empty
G = nx.Graph()

# add graph vertices

G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_node(4)
G.add_node(5)
G.add_node(6)

# add graph edges
G.add_edge(1, 2)
G.add_edge(1, 5)
G.add_edge(2, 3)
G.add_edge(2, 5)
G.add_edge(3, 4)
G.add_edge(5, 4)
G.add_edge(6, 4)
G.add_edge(6,3)

print('vertices:',G.nodes())
print('edges:',G.edges())
p=nx.shortest_path(G,source=2,target=6)
print('--------',p)

nx.draw(G,with_labels=True,pos=nx.spectral_layout(G))
plt.show()

