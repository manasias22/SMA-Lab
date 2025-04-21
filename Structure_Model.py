import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
from networkx.algorithms.community import greedy_modularity_communities

edges = [
 ('UserA', 'UserB'),
 ('UserB', 'UserC'),
 ('UserC', 'UserA'),
 ('UserB', 'UserD'),
 ('UserD', 'UserE'),
 ('UserE', 'UserB'),
 ('UserF', 'UserE'),
 ('UserG', 'UserF'),
 ('UserF', 'UserG')
]

G = nx.DiGraph()
G.add_edges_from(edges)

degree_centrality = nx.degree_centrality(G)
betweenness_centrality = nx.betweenness_centrality(G)

print("Degree Centrality:", degree_centrality)
print("Betweenness Centrality:", betweenness_centrality)

communities = list(greedy_modularity_communities(G))
print("\nDetected Communities:")

for i, community in enumerate(communities):
    print(f"Community {i + 1}: {community}")

plt.figure(figsize=(10, 8))
pos = nx.spring_layout(G) 
nx.draw_networkx_nodes(G, pos, node_size=3000, node_color='skyblue',
alpha=0.7)
nx.draw_networkx_edges(G, pos, width=2, alpha=0.7, edge_color='gray')
nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold',
font_color='black')

plt.title("Social Media Network Visualization")
plt.axis('off') 
plt.show()

shortest_path = nx.shortest_path(G, source='UserA', target='UserE',
method='dijkstra')
print("\nShortest Path from UserA to UserE:", shortest_path)





