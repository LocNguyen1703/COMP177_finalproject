import numpy as np 
import matplotlib.pyplot as plt
import networkx as nx

def Dijkstra(matrix, root, dest):
    # return NotImplementedError
    return nx.dijkstra_path(matrix, root, dest)
'''                0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19'''
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
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0] # 19
                ])

# Convert adjacency matrix to a graph
graph = nx.from_numpy_array(nparr)
graph_5_down = nx.from_numpy_array(nparr)
graph_7_down = nx.from_numpy_array(nparr)

# Simulate node shutdown (e.g., node 4)
nodes_to_remove_5 = [1, 3, 4, 11, 12]

nodes_to_remove_7 = [1, 3, 4, 11, 12]

for node_to_remove in nodes_to_remove_5:
    graph_5_down.remove_node(node_to_remove)

for node_to_remove in nodes_to_remove_7:
    graph_7_down.remove_node(node_to_remove)

# Attempt to compute shortest path from 0 to 19
try:
    shortestPathNodes = Dijkstra(graph, 0, 19)
    print("Shortest path:", shortestPathNodes)

    # Compute edges in the shortest path
    shortestPathEdges = tuple(zip(shortestPathNodes[:-1], shortestPathNodes[1:]))

    # Visualize graph
    edge_colors = ['r' if edge in shortestPathEdges or (edge[1], edge[0]) in shortestPathEdges else 'b' for edge in graph.edges]
    nx.draw(graph, pos=nx.spring_layout(graph), with_labels=True, edge_color=edge_colors)
    plt.axis("equal")
    plt.show()

except nx.NetworkXNoPath:
    print(f"No path exists between nodes 0 and 19 after removing node {node_to_remove}.")