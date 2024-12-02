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
