# COMP177_finalproject

# Dynamic Routing Mechanism Design Using Dijkstra's Algorithm in a Faulty Network


**Team Members**: Loc Nguyen, Richard Hull, Anna Noto

**Course**: COMP/ECPE 177 

**Professor**: Tapadhir Das

**Semester**: Fall 2024


## Table of Contents
1. [Project Overview](#project-overview)
2. [Technologies Used](#technologies-used)
3. [Scripts and Functionality](#scripts-and-functionality)
    - [dynamic_routing.py](#dynamic_routingpy)
    - [dynamic_routing_20_Node.py](#dynamic_routing_20_nodepy)
    - [dynamic_routing_50_node.py](#dynamic_routing_50_nodepy)
    - [dynamic_routing_node_generation.py](#dynamic_routing_node_generationpy)


## Project Overview
This project simulates dynamic routing in network graphs using Python's NetworkX library. The goal is to compute and visualize shortest paths within a network while dynamically adapting to changes, such as node or edge failures. The implementation uses Dijkstra's algorithm to determine paths and showcases resilience in varying network conditions.

The project includes the following scripts:
1. **`dynamic_routing.py`**: Routing in a 9-node network.
2. **`dynamic_routing_20_Node.py`**: Routing in a 20-node network with random node removals.
3. **`dynamic_routing_50_node.py`**: Routing in a 50-node network.
4. **`dynamic_routing_node_generation.py`**: Custom adjacency matrix generation and fault simulation.

---

## Technologies Used
- **NetworkX**: For graph creation and analysis.
- **NumPy**: To define adjacency matrices and randomize network configurations.
- **Matplotlib**: For graph visualization.
- make sure all the required libraries are installed using the following commands:
  **Linux**
      - sudo apt get update
      - sudo apt install numpy
      - sudo apt install matplotlib
      - sudo apt install networkx

  **Windows**
      - pip install numpy
      - pip install matplotlib
      - pip install networkx

---

## Scripts and Functionality

### `dynamic_routing.py`
- **Network Size**: 9 nodes.
- **Objective**: Compute the shortest path between nodes 2 and 8.
- **Key Features**:
  - Creates a graph from a predefined adjacency matrix.
  - Computes and visualizes the shortest path using Dijkstra's algorithm.
  - Highlights the path in red using `matplotlib`.
- **Output**: Graph visualization showing the shortest path.


![Graph Visualization](/images/dynamic_routing.png)

<details>
      <summary>Click to view the code</summary>
    
    ```python
    import numpy as np
    import matplotlib.pyplot as plt
    import networkx as nx
    
    # Adjacency matrix for a simple 9-node network
    nparr = np.array([[0, 1, 1, 0, 0, 0, 0, 0, 0],
                      [1, 0, 0, 1, 0, 1, 0, 0, 0],
                      [1, 0, 0, 1, 0, 0, 0, 0, 0],
                      [0, 1, 1, 0, 1, 0, 1, 0, 0],
                      [0, 0, 0, 1, 0, 1, 0, 1, 1],
                      [0, 1, 0, 0, 1, 0, 0, 0, 1],
                      [0, 0, 0, 1, 0, 0, 0, 1, 0],
                      [0, 0, 0, 0, 1, 0, 1, 0, 1],
                      [0, 0, 0, 0, 1, 1, 0, 1, 0]])
    
    # Create the graph from the adjacency matrix
    graph = nx.from_numpy_array(nparr)
    
    # Compute the shortest path using Dijkstra's algorithm
    shortest_path = nx.dijkstra_path(graph, 2, 8)
    
    # Create an edge list for the shortest path
    shortest_path_edges = list(zip(shortest_path[:-1], shortest_path[1:]))
    
    # Set edge colors: red for the shortest path, blue for others
    edge_colors = ['r' if edge in shortest_path_edges or (edge[1], edge[0]) in shortest_path_edges else 'b' for edge in graph.edges]
    
    # Draw the graph with labels and edge colors
    nx.draw(graph, pos=nx.spring_layout(graph), with_labels=True, edge_color=edge_colors, node_color='lightblue', node_size=500, font_size=10)
    
    # Show the plot
    plt.show()
    ```
</details>


### `dynamic_routing_20_Node.py`
- **Network Size**: 20 nodes.
- **Objective**: Simulate routing under failure conditions (5-node and 7-node removal scenarios).
- **Key Features**:
  - Defines a 20-node adjacency matrix and converts it into a graph.
  - Simulates failures by randomly removing nodes.
  - Computes the shortest path between nodes 0 and 19.
  - Visualizes the graph with the shortest path highlighted, or indicates if no path exists.
- **Output**: Visualizations of the original graph and graphs with failures.


![Graph Visualization](/images/dynamic_routing_20_node_graph.png)

<details> 
      <summary>Click to view the code</summary>
    
    ```python
    import numpy as np
    import matplotlib.pyplot as plt
    import networkx as nx
    import random
    
    # Adjacency matrix for a 20-node network
    nparr = np.random.randint(0, 2, (20, 20))
    np.fill_diagonal(nparr, 0)
    
    # Create the graph
    graph = nx.from_numpy_array(nparr)
    
    # Simulate node failures by randomly removing nodes
    nodes_to_remove = random.sample(range(20), 5)
    graph_removed = graph.copy()
    graph_removed.remove_nodes_from(nodes_to_remove)
    
    # Draw the graph with nodes removed
    nx.draw(graph_removed, pos=nx.spring_layout(graph_removed), with_labels=True, node_color='lightblue', node_size=500, font_size=10)
    
    # Show the plot
    plt.title("Graph with 5 Nodes Removed")
    plt.show()
    ```
</details>


### `dynamic_routing_50_node.py`
- **Network Size**: 50 nodes.
- **Objective**: Scale the simulation to a larger network.
- **Key Features**:
  - Uses a 50-node adjacency matrix.
  - Simulates dynamic failures by removing nodes or edges.
  - Computes and visualizes shortest paths dynamically.
- **Output**: Graph visualizations similar to the 20-node script but applied to a larger network.


![Graph Visualization](/images/dynamic_routing_50_node_graph.png)

<details> 
      <summary>Click to view the code</summary>
   
    ```python
    import numpy as np
    import matplotlib.pyplot as plt
    import networkx as nx
    
    # Generate a random 50-node adjacency matrix
    nparr = np.random.randint(0, 2, (50, 50))
    np.fill_diagonal(nparr, 0)
    
    # Create the graph
    graph = nx.from_numpy_array(nparr)
    
    # Draw the graph
    nx.draw(graph, pos=nx.spring_layout(graph), with_labels=True, node_color='lightblue', node_size=500, font_size=8)
    
    # Show the plot
    plt.title("50-Node Network")
    plt.show()
    ```
</details>



### `dynamic_routing_node_generation.py`
- **Objective**: Generate and simulate custom networks with random adjacency matrices.
- **Key Features**:
  - Allows for flexible network generation with user-defined dimensions.
  - Simulates node and edge failures.
  - Computes and visualizes shortest paths before and after failures.
  - Provides feedback when no path exists.
- **Output**: Dynamic visualizations of generated graphs and their changes.
- **How to run**: 
  - program will follow a user-interaction flow where it will ask for user inputs - requirements for allowed inputs: 
    - in general the program will only take numbers (it will take in floats, but will usually round them up).
    - when entering the percentage of nodes and edges to sabotage, do NOT enter "%" symbol, and do NOT use decimal format - only enter in normal integer format, and the program will convert to percentages or decimal format
    - keep in mind when entering the sender and receiver nodes that you want the program to find the shortest path for: the ordering of nodes starts at 0 instead of 1 and ends at 1 NUMBER BELOW the number of nodes the user entered


![Graph Visualization](/images/dynamic_routing_node_generation.png)

<details> 
      <summary>Click to view the code</summary>
   
    ```python
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
    while startNode not in graph.nodes: startNode = int(input("Invalid node (node does not exist in network). Enter the sender's node: "))
    endNode = int(input("Enter the receiver's node: "))
    while endNode not in graph.nodes: endNode = int(input("Invalid node (node does not exist in network). Enter the receiver's node: "))

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

    ```
</details>





