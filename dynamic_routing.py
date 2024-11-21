import numpy as np 
import matplotlib.pyplot as plt
import networkx as nx

def Dijkstra(matrix, root, dest):
    # return NotImplementedError
    return nx.dijkstra_path(matrix, root, dest)

nparr = np.array([[0, 1, 0, 0, 0, 0, 0, 0],
                  [1, 0, 1, 0, 1, 0, 0, 0],
                  [0, 1, 0, 1, 0, 0, 0, 0],
                  [1, 0, 0, 0, 0, 0, 0, 1],
                  [0, 1, 0, 0, 0, 0, 0, 0],
                  [1, 0, 0, 0, 0, 0, 0, 1],
                  [1, 1, 0, 0, 0, 0, 0, 1],
                  [0, 0, 0, 1, 0, 1, 1, 0]
                ])
edge_list = [(i, j) for i in range(len(nparr)) for j in range(len(nparr[i])) if nparr[i][j] == 1]

graph = nx.from_numpy_array(nparr)

shortestPathNodes = Dijkstra(graph, 4, 7)

# co-pilot generated shiet
# nx.draw_spring(graph, with_labels=True, edge_color='r', nodelist=shortest_path, edgelist=[(shortest_path[i], shortest_path[i+1]) for i in range(len(shortest_path)-1)])

# drawing this way below will show the nodes in the shortest path in blue
# nx.draw_spring(graph, with_labels=True, nodelist=shortest_path, edgelist=edge_list, edge_color='r', node_color='b')

# zip function creates a zip object that's basically a list of tuples that represents edges in the shortest path
# tuple() reassigns the zip object to a tuple object
shortestPathEdges = tuple(zip(shortestPathNodes[:-1], shortestPathNodes[1:]))

edge_colors = ['r' if (u, v) in shortestPathEdges or (v, u) in shortestPathEdges else 'b' for u, v in edge_list]
nx.draw_spring(graph, with_labels=True, edge_color=edge_colors)

print(shortestPathNodes[:-1]) # for debugging
print(shortestPathNodes[1:]) # for debugging

plt.axis=("equal")
plt.show()