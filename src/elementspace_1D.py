import numpy
from numpy.lib.arraysetops import isin

from nodespace_1D import NodeSpace1D

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

    def __init__(self, elements, nodes_per_element=2):
        if isinstance(elements, int):
            self.elements = numpy.zeros((elements, nodes_per_element))
            self.n_elements = elements
            self.nodes_per_element = nodes_per_element
        
        elif isinstance(elements, NodeSpace1D):
            self.elements = numpy.array((elements.n_nodes, nodes_per_element))
            self.nodes_per_element = nodes_per_element
            self.n_elements = elements.n_nodes - (self.nodes_per_element - 1)
        
        elif isinstance(elements, ElementSpace1D):
            self = elements

    def __str__(self) -> str:
        return format(self.elements)

    def __getitem__(self, key):
        return self.elements[key]
    def __setitem__(self, key, value):
        self.elements[key] = value

def main():
    print("Test ElementSpace:")
    # - create a NodeSpace of 16 Nodes over a size of 4 length
    e_space = ElementSpace1D(16)
    print("n Elements:", e_space.n_elements)
    print(e_space)

    print("Nodes_Per_Element:", e_space.nodes_per_element)

if __name__ == "__main__":
    main()