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
class ElementSpace1D(NodeSpace1D):

    # Element array:
    elements = numpy.array([])

    # Number of Elements:
    n_elements = 0

    # Number of Nodes per Element:
    nodes_per_element = 2


    def __init__(self, elements, dimension=1, nodes_per_element=2):
        # If elements is a number, it specifies the number of elements
        if isinstance(elements, int):
            self.elements = numpy.zeros((elements, nodes_per_element))
            self.n_elements = elements
            self.nodes_per_element = nodes_per_element

            # Calculate the number of nodes
            number_of_nodes = elements * nodes_per_element - ()
            
        
        elif isinstance(elements, NodeSpace1D):
            self.elements = numpy.array((elements.n_nodes, nodes_per_element))
            self.nodes_per_element = nodes_per_element
            self.n_elements = elements.n_nodes - (self.nodes_per_element - 1)

            # Generate Elements from NodeSpace
            for i in range(self.n_elements):
                for j in range(self.nodes_per_element):
                    self.elements[i, j] = i + j + (self.nodes_per_element - 2)

        elif isinstance(elements, ElementSpace1D):
            self = elements

        # Generate Elements from NodeSpace
        for i in range(self.n_elements):
            for j in range(self.nodes_per_element):
                self.elements[i, j] = i + j + (self.nodes_per_element - 2)

    def __str__(self) -> str:
        ret_str = format(self.n_elements)
        ret_str += "\n"
        for i in range(self.n_elements):
            for j in range(self.nodes_per_element):
                ret_str += format(i) + "," + format(j) + ":"
                ret_str += format(self.elements[i,j])
                if j != (self.nodes_per_element - 1):
                    ret_str += ";"
            ret_str += "\n"
        return ret_str
        
    def __getitem__(self, key):
        return self.elements[key]
    def __setitem__(self, key, value):
        self.elements[key] = value
        

def main():
    print("Test ElementSpace:")
    # - create a NodeSpace of 16 Nodes over a size of 4 length
    e_space = ElementSpace1D(16)
    print(e_space)

    print("Nodes_Per_Element:", e_space.nodes_per_element)

if __name__ == "__main__":
    main()