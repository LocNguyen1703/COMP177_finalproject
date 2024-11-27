import numpy as np 
import matplotlib.pyplot as plt
import networkx as nx
import random


def Dijkstra(graph, root, dest):
    try:
        return nx.dijkstra_path(graph, root, dest)
    except nx.NodeNotFound:
        return None
    except nx.NetworkXNoPath:
        return None

# Adjacency matrix
nparr = np.array([[0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], # 0
                  [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0], # 1
                  [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # 2
                  [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0], # 3
                  [0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], # 4
                  [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], # 5
                  [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0], # 6
                  [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # 7
                  [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # 8
                  [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0], # 9
                  [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0], # 10
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1], # 11
                  [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # 12
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1], # 13
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], # 14
                  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], # 15
                  [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], # 16
                  [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # 17
                  [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], # 18
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0]  # 19
                ])

# Convert adjacency matrix to graph
graph = nx.from_numpy_array(nparr)

# Create separate copies for failures
graph_5_down = graph.copy()
graph_7_down = graph.copy()

# Remove 5 nodes randomly
nodes_to_remove_5 = random.sample(range(20), 5)
for node in nodes_to_remove_5:
    graph_5_down.remove_node(node)

# Remove 7 nodes randomly
nodes_to_remove_7 = random.sample(range(20), 7)
for node in nodes_to_remove_7:
    graph_7_down.remove_node(node)

# Helper function to check shortest path and visualize
def visualize_path(graph, title):
    if 0 in graph.nodes and 19 in graph.nodes:
        shortestPathNodes = Dijkstra(graph, 0, 19)
        if shortestPathNodes:
            print(f"{title} Shortest path: {shortestPathNodes}")
            shortestPathEdges = tuple(zip(shortestPathNodes[:-1], shortestPathNodes[1:]))
            edge_colors = ['r' if edge in shortestPathEdges or (edge[1], edge[0]) in shortestPathEdges else 'b' for edge in graph.edges]
            nx.draw(graph, pos=nx.spring_layout(graph), with_labels=True, edge_color=edge_colors)
            plt.title(title)
            plt.show()
        else:
            print(f"{title}: No path exists between 0 and 19.")
    else:
        print(f"{title}: Node 0 or 19 not in graph.")

# Visualize the results
visualize_path(graph, "Original Graph")
visualize_path(graph_5_down, "Graph with 5 Nodes Removed")
visualize_path(graph_7_down, "Graph with 7 Nodes Removed")
