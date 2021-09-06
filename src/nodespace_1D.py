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

    node_distance = 0

    def __init__(self, nodes, dimension_size=1, start=0):
        if isinstance(nodes, int):
            self.nodes = numpy.linspace(start, start + dimension_size, nodes)
            self.n_nodes = nodes
            
            self.node_start = start
            self.node_distance = dimension_size
            self.node_end = start + dimension_size

        elif isinstance(nodes, list):
            self.nodes = numpy.array(nodes.sort())
            self.n_nodes = len(nodes)
            
            self.node_start = self.nodes[0]
            self.node_end = self.nodes[self.n_nodes - 1]
            self.node_distance = self.node_end - self.node_start
        
        elif isinstance(nodes, numpy.ndarray):
            self.nodes = numpy.sort(nodes)
            self.n_nodes = nodes.size
        
            self.node_start = self.nodes[0]
            self.node_end = self.nodes[self.n_nodes - 1]
            self.node_distance = self.node_end - self.node_start
        
        elif isinstance(nodes, NodeSpace1D):
            self = nodes
    
    def __str__(self) -> str:
        return format(self.nodes)
    
    def __getitem__(self, key):
        return self.nodes[key]
    def __setitem__(self, key, value):
        self.nodes[key] = value
    
    # Assign numerical values to nodes at specified indices
    def assign_values(self, num_value, node_indices):
        for i in node_indices:
            self.nodes[i] = num_value

    # Set the overall dimension for a node space
    def set_distance(self, dimension_size):
        self.__init__(self.nodes, dimension_size)

    # Set the start position for the node
    def set_start(self, start_pos):
        self.__init__(self.nodes, self.node_distance, start_pos)


def main():
    print("Test NodeSpace:")
    # - create a NodeSpace of 16 Nodes over a size of 4 length
    n_space = NodeSpace1D(16, 4, 1)
    print("n Nodes:", n_space.n_nodes)
    print(n_space)

    print("Node_Start:", n_space.node_start)
    print("Node_Distance:", n_space.node_distance)
    print("Node_End:", n_space.node_end)

if __name__ == "__main__":
    main()