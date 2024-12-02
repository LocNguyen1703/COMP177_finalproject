import numpy as np 
import matplotlib.pyplot as plt
import networkx as nx
import random

def Dijkstra(matrix, root, dest):
    # return NotImplementedError
    try: 
        path = nx.dijkstra_path(matrix, root, dest)
    except: 
        path = None
    return path if path else None 

def generateMatrix (dimension, choice):
    if choice == 1:
        # generating a random adjacency matrix using np.random.randint
        nparr = np.random.randint(0, 2, (dimension, dimension))  # using np.random.randint
        for i in range(len(nparr)):
            nparr[i][i] = 0
        return nparr

    elif choice == 2: 
        # generating a random adjacency matrix using nested for loop 
        nparr = np.zeros((dimension, dimension))
        for i in range(len(nparr)//2 + 1):
            for j in range(i+1, len(nparr[i])):
                nparr[i][j] = np.random.randint(0, 2)
                nparr[j][i] = nparr[i][j]
        return nparr

    else: print("invalid input - please enter 1 or 2 for choice")

def simulateBreakdown(graph, pEdges, pNodes):
    # simulate a breakdown by setting the value of the edge to 0
    graphCopy = graph.copy()
    numEdges = int(len(list(graphCopy.edges))*pEdges/100)
    numNodes = int(len(list(graphCopy.nodes))*pNodes/100)
    edgesToRemove = random.sample(list(graphCopy.edges), numEdges)
    nodesToRemove = random.sample(list(graphCopy.nodes), numNodes)
    graphCopy.remove_edges_from(edgesToRemove)
    graphCopy.remove_nodes_from(nodesToRemove)
    return graphCopy

"""
generateMatrix(x, y) 
    - x is for matrix's dimensions (adjacency matrix as to have equal width and height)
    - y is for choice of generation method 
        - 1: uses np.random.randint
        - 2: uses nested for loop
"""
numNodes = int(input("Enter the number of nodes: "))
choice = int(input(
    "Enter 1 or 2 for choice of matrix generation method: \nenter 1 for np.random.randint\nenter 2 for nested for loop\n"))

nparr = generateMatrix(numNodes, choice)  
graph = nx.from_numpy_array(nparr)

startNode = int(input("Enter the sender's node: "))
endNode = int(input("Enter the receiver's node: "))

shortestPathNodes = Dijkstra(graph, startNode, endNode)

if not shortestPathNodes: print("No shortest path found.")
else:
    plt.figure("original network")
    shortestPathEdges = tuple(zip(shortestPathNodes[:-1], shortestPathNodes[1:]))
    edge_colors = ['r' if edge in shortestPathEdges or (edge[1], edge[0]) in shortestPathEdges else 'b' for edge in graph.edges]
    nx.draw(graph, pos=nx.circular_layout(graph), with_labels=True, edge_color=edge_colors)

percentNodesSabotage = int(input("Enter the percentage (in normal integer) of nodes to sabotage: "))
percentEdgesSabotage = int(input("Enter the percentage (in normal integer) of edges to sabotage: "))

graph2 = simulateBreakdown(graph, percentEdgesSabotage, percentNodesSabotage)
shortestPathNodes2 = Dijkstra(graph2, startNode, endNode)

if not shortestPathNodes2: print("No shortest path found after sabotage.")
else: 
    plt.figure("network after sabotage")
    shortestPathEdges2 = tuple(zip(shortestPathNodes2[:-1], shortestPathNodes2[1:]))
    edge_colors2 = ['r' if edge in shortestPathEdges2 or (edge[1], edge[0]) in shortestPathEdges2 else 'b' for edge in graph2.edges]
    nx.draw(graph2, pos=nx.circular_layout(graph2), with_labels=True, edge_color=edge_colors2)

# plt.axis=("equal")
plt.show()


#random code snippet
print("Hello World")
