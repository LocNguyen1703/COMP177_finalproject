import numpy as np 
import matplotlib.pyplot as plt
import networkx as nx

def Dijkstra(matrix, root, dest):
    # return NotImplementedError
    return nx.dijkstra_path(matrix, root, dest)

edge_list = [(1, 2), (2, 3), (2, 5), (3, 4), (4, 5), (5, 6), (6, 7)]
graph = nx.from_edgelist(edgelist=edge_list)

shortest_path = Dijkstra(graph, 4, 7)

# co-pilot generated shiet
# nx.draw_spring(graph, with_labels=True, edge_color='r', nodelist=shortest_path, edgelist=[(shortest_path[i], shortest_path[i+1]) for i in range(len(shortest_path)-1)])

# drawing this way below will show the nodes in the shortest path in blue
# nx.draw_spring(graph, with_labels=True, nodelist=shortest_path, edgelist=edge_list, edge_color='r', node_color='b')

edge_colors = ['r' if (u, v) in zip(shortest_path[:-1], shortest_path[1:]) else 'b' for u, v in edge_list]
nx.draw_spring(graph, with_labels=True, edge_color=edge_colors)

plt.axis=("equal")
plt.show()