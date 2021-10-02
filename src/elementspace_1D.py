import numpy
from numpy.lib.arraysetops import isin

from nodespace_1D import NodeSpace1D


class ElementSpace1D(NodeSpace1D):
    """
    An Element space is a collection of elements in a single dimension, X.
    The data is stored in a 2-dimensional array.

    The value of the array at i and j represents the element at i, 
    composed of the node j:

        ElementSpace[i,j] = Node_j of Element_i

    """
    # Element array:
    elements = numpy.array([0,0])       # Numpy array

    # Number of Elements:
    n_elements = 0                      # int (>0)

    # Number of Nodes per Element:
    nodes_per_element = 2               # int (>=2)

    def __init__(self, elements, dimension=1, start=0, nodes_per_element=2):
        # If elements is a number, it specifies the number of elements
        if isinstance(elements, int):
            self.elements = numpy.zeros((elements, nodes_per_element))
            self.n_elements = elements
            self.nodes_per_element = nodes_per_element

            # Calculate the number of nodes
            n_nodes = elements * nodes_per_element - (elements - 1)
            super().__init__(n_nodes, dimension, start)
        
        # If elements is a NodeSpace1D, it defines the Nodes used by the Elements,
        # - disregards dimension & start
        elif isinstance(elements, NodeSpace1D):
            self.elements = numpy.empty([elements.n_nodes, nodes_per_element])
            self.nodes_per_element = nodes_per_element
            self.n_elements = elements.n_nodes - (self.nodes_per_element - 1)
            
            # initialise inherited nodeSpace
            super().__init__(elements)

        elif isinstance(elements, ElementSpace1D):
            self.elements = elements.elements
            self.n_elements = elements.n_elements
            self.nodes_per_element = elements.nodes_per_element

        # Generate Elements from NodeSpace
        for i in range(self.n_elements):
            for j in range(self.nodes_per_element):
                self.elements[i, j] = i * (self.nodes_per_element - 1) + j
            
        # end __init__

    def __str__(self) -> str:
        ret_str = format(self.n_elements)
        ret_str += "\n"
        for i in range(self.n_elements):
            for j in range(self.nodes_per_element):
                ret_str += "[{:n},{:n}]:".format(i,j)
                ret_str += "{:n}".format(self.elements[i,j])
                if j != (self.nodes_per_element - 1):
                    if self.elements[i, j] < 10:    
                        ret_str += "\t"
                        # to get consistent column tabs
                    ret_str += "\t"
            ret_str += "\n"
        return ret_str
        
    def __getitem__(self, key):
        return self.elements[key]
    def __setitem__(self, key, value):
        self.elements[key] = value

    # Return the NodeSpace the ElementSpace is based on
    def nodeSpace_str(self) -> str:
        return super().__str__()
        

def main():
    # Test Classes & Functions
    print("Test ElementSpace:")
    # - Create an ElementSpace of 10 elements 
    #   over a dimension of size 4,
    #   starting at 3, 
    #   with 2 nodes per element:
    e_space2 = ElementSpace1D(10, 4, 3, 2)
    print("Nodes_Per_Element:", e_space2.nodes_per_element)
    print(e_space2)

    # Test get_NodeSpace string
    print("Test ElementSpace_2 Parent NodeSpace:")
    n_space_str2 = e_space2.nodeSpace_str()
    print("N_nodes:", n_space_str2)


    print("Test ElementSpace with 4 nodes per element")
    # - Create an ElementSpace of 8 elements 
    #   over a dimension of size 10,
    #   starting at 0,
    #   with 4 nodes per element:
    e_space4 = ElementSpace1D(8, 10, 0, 4)
    print("Nodes_Per_Element:", e_space4.nodes_per_element)
    print(e_space4)

    # Test get_NodeSpace string
    print("Test ElementSpace_4 Parent NodeSpace:")
    n_space_str4 = e_space4.nodeSpace_str()
    print("N_nodes:", n_space_str4)


if __name__ == "__main__":
    main()