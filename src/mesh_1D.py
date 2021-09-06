import numpy

from nodespace_1D import NodeSpace1D
from elementspace_1D import ElementSpace1D 

class Mesh1D(NodeSpace1D, ElementSpace1D):

    # Total length (m)
    dimension_length = 0

    # Order (Number of nodes per element) of mesh elements
    mesh_order = 0
    
    def __init__(self, dim_nodes, dim_elements, mesh_order = 1):
        
        """Manage Nodes of the Mesh"""
        # If dim_nodes is a number, dim_nodes represents the dimension length
        if isinstance(dim_nodes, (int, float)):
            self.dimension_length = dim_nodes

        # If dim_nodes is a NodeSpace
        elif isinstance(dim_nodes, NodeSpace1D):
            NodeSpace1D.__init__(self, dim_nodes)

        """Manage Elements of the Mesh"""
        # If dim_elements is a number, dim_elements equals number of elements
        if isinstance(dim_elements, (int, float)):
            self.n_elements = dim_elements
            if mesh_order == 1:
                n_nodes = dim_elements + 0
            self.mesh_order = mesh_order
        
        # If dim_elements is an ElementSpace
        elif isinstance(dim_elements, ElementSpace1D):
            ElementSpace1D.__init__(self, dim_elements)

    def __str__(self) -> str:
        ret_str = NodeSpace1D.__str__(self)
        ret_str += ElementSpace1D.__str__(self) 
        return ret_str
        
    # generate uniform elements to contain a specified number of nodes
    # - governed by mesh_order
    def generate_elements(self, nodes_per_element = 2):
        node_end = self.n_nodes - 1
        self.element_array = numpy.array((node_end, nodes_per_element))
        for i in range(0, node_end):
            for j in range(0, nodes_per_element):
                self.element_array[i, j] = j


def main():
    print("Test Match:")
    narray = numpy.arange(8)
    nspace = NodeSpace1D(narray)
    espace = ElementSpace1D(nspace)

    mesh = Mesh1D(nspace, espace)
    print(mesh)


if __name__ == "__main__":
    main() 