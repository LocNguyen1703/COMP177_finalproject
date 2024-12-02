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

This script takes things to another level by simulating a 50-node network. It’s a great way to explore how routing algorithms scale with network size and complexity. Working with a larger network really highlights the challenges of maintaining efficient routing as the system grows, similar to the hierarchical routing concepts we read about in Section 5.5. It’s a good reminder of why we need scalable solutions like BGP in the real world.


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

This script is the most flexible, allowing me to generate custom networks and simulate both node and edge failures. It’s like stress-testing a network to see how resilient it is under different conditions. Watching paths recalculate dynamically feels a lot like what we see with real-world routing protocols like OSPF or BGP. This ties into Section 4.4 of the textbook, where we talked about fault tolerance and why reliability is such a big deal in networking.


![Graph Visualization](/images/dynamic_routing_node_generation.png)

<details> 
      <summary>Click to view the code</summary>
   
    ```python
    import numpy as np
    import matplotlib.pyplot as plt
    import networkx as nx
    import random
    
    def generate_matrix(dimension):
        # Generate a random adjacency matrix for a graph
        nparr = np.random.randint(0, 2, (dimension, dimension))
        np.fill_diagonal(nparr, 0)
        return nparr
    
    # Generate a random 9-node network
    nparr = generate_matrix(9)
    
    # Create the graph
    graph = nx.from_numpy_array(nparr)
    
    # Simulate node failures by removing 20% of the nodes
    nodes_to_remove = random.sample(range(9), int(0.2 * 9))
    graph_removed = graph.copy()
    graph_removed.remove_nodes_from(nodes_to_remove)
    
    # Draw the graph with nodes removed
    nx.draw(graph_removed, pos=nx.spring_layout(graph_removed), with_labels=True, node_color='lightblue', node_size=500, font_size=10)
    
    # Show the plot
    plt.title("Graph with 20% Nodes Removed")
    plt.show()
    ```
</details>





