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
4. [Results and Analysis](#results-and-analysis)
    - [Original Networks](#original-networks)
    - [Failure Simulations](#failure-simulations)
    - [Network Resilience](#network-resilience)
5. [Conclusion](#conclusion)
6. [Future Work](#future-work)


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

This script lays the groundwork for understanding dynamic routing by simulating a simple 9-node network. It uses an adjacency matrix to define the network's topology and Dijkstra's algorithm to compute the shortest path between two nodes. The output visually highlights the path, making it easy to see how routing decisions are made. This connects directly to what we've learned about routing algorithms in Chapter 5 of Computer Networking: A Top-Down Approach. It reminds me of how routers build and use routing tables to efficiently move data through a network.

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

Scaling up to a 20-node network, this script dives deeper into fault tolerance by simulating scenarios where nodes are randomly removed. Watching how the shortest path adapts (or sometimes fails to exist) really ties into the importance of robust routing protocols like OSPF. It shows how networks stay connected even when parts go offline, which is something we discussed in Chapter 5 about how link-state protocols handle dynamic changes in topology.

![Graph Visualization](/images/dynamic_routing_20_Node.png)

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

This script takes things to another level by simulating a 50-node network. It’s a great way to explore how routing algorithms scale with network size and complexity. Working with a larger network really highlights the challenges of maintaining efficient routing as the system grows, similar to the hierarchical routing concepts we read about in Section 5.5. It’s a good reminder of why we need scalable solutions like BGP in the real world.


![Graph Visualization](/images/dynamic_routing_50_node.png)

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
  - make sure all the required libraries are installed (numpy, matplotlib and networkx)
  - program will follow a user-interaction flow where it will ask for user inputs - requirements for allowed inputs: 
    - in general the program will only take numbers (it will take in floats, but will usually round them up).
    - when entering the percentage of nodes and edges to sabotage, do NOT enter "%" symbol, and do NOT use decimal format - only enter in normal integer format, and the program will convert to percentages or decimal format
    - keep in mind when entering the sender and receiver nodes that you want the program to find the shortest path for: the ordering of nodes starts at 0 instead of 1 and ends at 1 NUMBER BELOW the number of nodes the user entered

This script is the most flexible, allowing me to generate custom networks and simulate both node and edge failures. It’s like stress-testing a network to see how resilient it is under different conditions. Watching paths recalculate dynamically feels a lot like what we see with real-world routing protocols like OSPF or BGP. This ties into Section 4.4 of the textbook, where we talked about fault tolerance and why reliability is such a big deal in networking.


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


---

## Results and Analysis

The results of the dynamic routing simulations demonstrated how network topology and node failures impact the ability to compute the shortest path in a network. In the original 9-node, 20-node, and 50-node networks, the Dijkstra algorithm successfully calculated the shortest paths between the source and destination nodes, as expected. Visualizations of these networks clearly highlighted the edges that were part of the shortest path, providing an intuitive understanding of the routing decisions made by the algorithm. As nodes were randomly removed to simulate network failures, the ability to maintain a valid path was tested. In the 20-node and 50-node networks, removing nodes resulted in certain paths becoming unavailable, showing the importance of fault tolerance in real-world routing protocols. The 50-node network demonstrated the scalability of the algorithm, where routing decisions were still computed, but the complexity increased with the larger network size. Additionally, the impact of node and edge failures on network connectivity was illustrated through side-by-side comparisons of networks before and after failures. These results emphasize the dynamic nature of routing in networks and highlight the need for resilient routing protocols that can adapt to changing network conditions.

<br />
<br />

<ins> **If we break all that down:** </ins>
### Original Networks
- Shortest paths are successfully computed for all original graphs.
- Graph visualizations highlight paths clearly, demonstrating successful routing.

### Failure Simulations
- **9-node network**: Pathfinding is straightforward due to the small network size.
- **20-node and 50-node networks**: Larger networks adapt dynamically to failures, though excessive failures may isolate nodes.
- **Custom networks**: Results depend on topology and failure degree.

### Network Resilience
- Larger networks demonstrate improved resilience to failures due to greater path redundancy.
- Excessive node or edge failures may render some nodes unreachable.

![Graph Visualization](/images/ResultsandAnalysis.png)

<details>
    <summary>Click to view the code</summary>
    
    ```python
    import numpy as np
    import matplotlib.pyplot as plt
    import networkx as nx
    import random
    
    # Create the original 20-node network
    nparr = np.random.randint(0, 2, (20, 20))
    np.fill_diagonal(nparr, 0)
    graph = nx.from_numpy_array(nparr)
    
    # Simulate node failures by removing 5 nodes
    nodes_to_remove = random.sample(range(20), 5)
    graph_removed = graph.copy()
    graph_removed.remove_nodes_from(nodes_to_remove)
    
    # Set up the plot with subplots for comparison
    fig, axs = plt.subplots(1, 2, figsize=(12, 6))
    
    # Original network
    axs[0].set_title("Original Network")
    nx.draw(graph, pos=nx.spring_layout(graph), ax=axs[0], with_labels=True, node_color='lightblue', node_size=500, font_size=8)
    
    # Network with failures
    axs[1].set_title("Network with 5 Nodes Removed")
    nx.draw(graph_removed, pos=nx.spring_layout(graph_removed), ax=axs[1], with_labels=True, node_color='lightblue', node_size=500, font_size=8)
    
    plt.show()
    ```
</details>


---

## Conclusion
This project demonstrates the implementation of dynamic routing and network resilience using Dijkstra's algorithm. Through progressive simulations, it highlights how networks adapt to failures and visualizes the routing paths dynamically. This approach is particularly valuable for studying fault-tolerant network design.

---

## Future Work
There are several potential directions for expanding this project. One area for improvement is to explore alternative routing algorithms, such as the Bellman-Ford algorithm, and compare their performance with Dijkstra’s algorithm, especially in terms of handling negative edge weights and slower convergence in larger networks. Additionally, incorporating edge weights to reflect network link costs would make the simulation more realistic, as real-world networks often prioritize certain paths over others. Below is an example of how the graph can be visualized with weighted edges. Further work could also include implementing dynamic routing protocols like OSPF or BGP, which adjust routes based on real-time network changes. Another extension would be to simulate more complex failure scenarios, such as simultaneous node and edge failures, to better mimic the challenges faced in large-scale distributed networks. Finally, integrating machine learning techniques to predict and optimize routing decisions based on network traffic patterns and conditions could be an exciting avenue for future development.


![Graph Visualization](/images/FutureWork.png)


<details> 
    <summary>Click to view the code</summary>
    
    ```python
    import numpy as np
    import matplotlib.pyplot as plt
    import networkx as nx
    
    # Generate a random 9-node network with weighted edges
    nparr = np.random.randint(0, 10, (9, 9))  # Random weights between 0 and 10
    np.fill_diagonal(nparr, 0)
    
    # Create the graph with weights
    graph = nx.from_numpy_array(nparr)
    
    # Draw the graph with edge weights displayed
    pos = nx.spring_layout(graph)
    nx.draw(graph, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10)
    labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)
    
    # Show the plot
    plt.title("Graph with Weighted Edges")
    plt.show()
    ```
</details>




