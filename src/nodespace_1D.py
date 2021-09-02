import numpy

"""
    A Node space defines a collection of nodes in a single dimension, X.
    This data is stored in a single dimension array.

    The value of the array at i represents the X coordinate of the node at i:
        
        Nodespace[i] = X_i

"""
# This class is a wrapper for a numpy array
class NodeSpace1D:
    
    # Node array:
    nodes = []

    # Number of Nodes:
    n_nodes = 0

    # Node Start & End
    node_start = 0
    node_end = 0

    node_dimension = 0

    def __init__(self, nodes, dimension=1):
        if isinstance(nodes, int):
            self.nodes = numpy.linspace(0, dimension, nodes)
            self.n_nodes = nodes
            
            self.node_start = self.nodes[0]
            self.node_end = self.nodes[self.n_nodes - 1]
            self.node_distance = self.node_end - self.node_start
            
        elif isinstance(nodes, list):
            self.nodes = numpy.array(nodes.sort())
            self.n_nodes = len(nodes)
            
            self.node_start = self.nodes[0]
            self.node_end = self.nodes[self.n_nodes - 1]
            self.node_distance = self.node_end - self.node_start
        
        elif isinstance(nodes, numpy.ndarray):
            self.nodes = numpy.sort(nodes)
            self.n_nodes = nodes.size()
        
            self.node_start = self.nodes[0]
            self.node_end = self.nodes[self.n_nodes - 1]
            self.node_distance = self.node_end - self.node_start
        
        elif isinstance(nodes, NodeSpace1D):
            self = nodes
    
    def __getitem__(self, key):
        return self.nodes[key]
    def __setitem__(self, key, value):
        self.nodes[key] = value
    
    # Assign numerical values to nodes at specified indices
    def assign_values(self, num_value, node_indices):
        for i in node_indices:
            self.nodes[i] = num_value

    # Set the overall dimension for a node space
    def set_dimension(self, dimension):
        self.node_dimension = dimension
