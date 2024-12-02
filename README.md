# COMP177_finalproject

# Dynamic Routing Mechanism Design Using Dijkstra's Algorithm in a Faulty Network


**Course**: COMP/ECPE 177 

**Team Members**: Loc Nguyen, Richard Hull, Anna Noto

**Semester**: Fall 2024

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


### `dynamic_routing_20_Node.py`
- **Network Size**: 20 nodes.
- **Objective**: Simulate routing under failure conditions (5-node and 7-node removal scenarios).
- **Key Features**:
  - Defines a 20-node adjacency matrix and converts it into a graph.
  - Simulates failures by randomly removing nodes.
  - Computes the shortest path between nodes 0 and 19.
  - Visualizes the graph with the shortest path highlighted, or indicates if no path exists.
- **Output**: Visualizations of the original graph and graphs with failures.


### `dynamic_routing_50_node.py`
- **Network Size**: 50 nodes.
- **Objective**: Scale the simulation to a larger network.
- **Key Features**:
  - Uses a 50-node adjacency matrix.
  - Simulates dynamic failures by removing nodes or edges.
  - Computes and visualizes shortest paths dynamically.
- **Output**: Graph visualizations similar to the 20-node script but applied to a larger network.


### `dynamic_routing_node_generation.py`
- **Objective**: Generate and simulate custom networks with random adjacency matrices.
- **Key Features**:
  - Allows for flexible network generation with user-defined dimensions.
  - Simulates node and edge failures.
  - Computes and visualizes shortest paths before and after failures.
  - Provides feedback when no path exists.
- **Output**: Dynamic visualizations of generated graphs and their changes.

---

## Results and Analysis

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

---

## Conclusion
This project demonstrates the implementation of dynamic routing and network resilience using Dijkstra's algorithm. Through progressive simulations, it highlights how networks adapt to failures and visualizes the routing paths dynamically. This approach is particularly valuable for studying fault-tolerant network design.

---

## Future Work
- Implement alternative algorithms (e.g., Bellman-Ford) for comparison.
- Analyze edge-weighted graphs for more realistic simulations.
- Expand failure simulations to include simultaneous node and edge removals.




