import numpy

"""
    An Element space is a collection of elements in a single dimension, X.
    The data is stored in a 2-dimensional array.

    The value of the array at i and j represents the element at i, 
    composed of the node j:

        ElementSpace[i,j] = Node_j of Element_i

"""
# This class is a wrapper for a numpy array
class ElementSpace1D:

    # Element array:
    elements = numpy.array([])

    # Number of Elements:
    n_elements = 0

    # Number of Nodes per Element:
    nodes_per_element = 2

    def __init__(self, nodes, nodes_per_element=2):
        if isinstance(nodes, int):
            self.elements = numpy.zeros((nodes, nodes_per_element))
            self.n_elements = nodes
            self.nodes_per_element = nodes_per_element
        elif isinstance(nodes, NodeSpace1D):
            self.elements = numpy.array((nodes.n_nodes, nodes_per_element))
            self.n_elements = nodes.n_nodes
            self.nodes_per_element = nodes_per_element

    @classmethod
    def withNodeSpace(self, nodespace, nodes_per_element=2):
        self.elements = numpy.array((nodespace.n_nodes, nodes_per_element));
        for i in range(nodespace.n_nodes):
            for j in range(nodes_per_element):
                self.elements[i, j] = nodespace.nodes[i + j]
    