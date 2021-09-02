import numpy

from nodespace_1D import NodeSpace1D
from elementspace_1D import ElementSpace1D 

class Mesh1D(NodeSpace1D, ElementSpace1D):

    # Total length (m)
    dimension_length = 0

    # Order (Number of nodes per element) of mesh elements
    mesh_order = 0
    
    def __init__(self, dim_nodes, dim_elements, mesh_order = 1):
        # Manage the Nodes of the mesh
        if isinstance(dim_nodes, (int, float)):
            self.dimension_length = dim_nodes

            # generate nodes to be equal distances apart, spanning total length of x
            self.node_array = numpy.array((self.n_nodes))
            dim_increment = self.dimension/self.n_elements
            self.node_array[-1] = 0
            for i in range (0, self.n_nodes):
                self.node_array[i] = dim_increment
                dim_increment += dim_increment
            
        elif isinstance(dim_nodes, NodeSpace1D):
            NodeSpace1D.__init__(dim_nodes)

        # Manage the elements of the mesh
        if isinstance(dim_elements, (int, float)):
            self.n_elements = dim_elements
            if mesh_order == 0:
                self.n_nodes = dim_elements + 0
            self.mesh_order = mesh_order
        elif isinstance(dim_elements, ElementSpace1D):
            ElementSpace1D.__init__(dim_elements)
        
        
    # generate uniform elements to contain a specified number of nodes
    # - governed by mesh_order
    def generate_elements(self, nodes_per_element = 2):
        node_end = self.n_nodes - 1
        self.element_array = numpy.array((node_end, nodes_per_element))
        for i in range(0, node_end):
            for j in range(0, nodes_per_element):
                self.element_array[i, j] = j


def main():
    # Test mesh
    narray = numpy.arange(8)
    nspace = NodeSpace1D(narray)
    espace = ElementSpace1D(nspace)

    mesh = Mesh1D(nspace, espace)
    
if __name__ == "__main__":
    main() 