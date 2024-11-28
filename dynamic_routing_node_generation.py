import numpy as np 
import matplotlib.pyplot as plt
import networkx as nx

def Dijkstra(matrix, root, dest):
    # return NotImplementedError
    return nx.dijkstra_path(matrix, root, dest)

def generateMatrix (dimension, choice):
    if choice == 1:
        # generating a random adjacency matrix using np.random.randint
        nparr = np.random.randint(0, 2, (dimension, dimension))  # using np.random.randint
        for i in range(len(nparr)):
            nparr[i][i] = 0
        return nparr

    elif choice == 2: 
        # using nested for loop 
        nparr = np.zeros((dimension, dimension))
        for i in range(len(nparr)//2 + 1):
            for j in range(i+1, len(nparr[i])):
                nparr[i][j] = np.random.randint(0, 2)
                nparr[j][i] = nparr[i][j]
        return nparr

    else: print("invalid input - please enter 1 or 2 for choice")

nparr = generateMatrix(9, 2)

print(nparr)  # for debugging
print(9//2)
graph = nx.from_numpy_array(nparr)

shortestPathNodes = Dijkstra(graph, 2, 8)
print(shortestPathNodes) # for debugging

shortestPathEdges = tuple(zip(shortestPathNodes[:-1], shortestPathNodes[1:]))
print(shortestPathEdges) # for debugging
edge_colors = ['r' if edge in shortestPathEdges or (edge[1], edge[0]) in shortestPathEdges else 'b' for edge in graph.edges]
print(edge_colors) # for debugging
nx.draw(graph, pos=nx.spring_layout(graph), with_labels=True, edge_color=edge_colors)

plt.axis=("equal")
plt.show()
