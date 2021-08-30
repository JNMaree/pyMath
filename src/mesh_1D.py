import numpy

class NodeSpace1D:
    
    # Node array:
    nodes = []

    # Number of Nodes:
    n_nodes = 0

    # Node Start & End
    node_start = 0
    node_end = 0

    node_distance = 0

    def __init__(self, nodes):
        if isinstance(nodes, int):
            self.nodes = numpy.zeros(nodes)
            self.n_nodes = nodes
            
        elif isinstance(nodes, list):
            self.nodes = numpy.array(nodes.sort())
            self.n_nodes = len(nodes)

        elif isinstance(nodes, numpy.ndarray):
            self.nodes = numpy.sort(nodes)
            self.n_nodes = nodes.size()

        self.node_start = self.nodes[0]
        self.node_end = self.nodes[self.n_nodes - 1]
        self.node_distance = self.node_end - self.node_start
        
    # Assign numerical values to nodes at specified indices
    def assign_values(self, num_value, node_indices):
        for i in node_indices:
            self.nodes[i] = num_value

    def __getitem__(self, key):
        return self.nodes[key]
    def __setitem__(self, key, value):
        self.nodes[key] = value
        
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
    
class Mesh1D(NodeSpace1D, ElementSpace1D):

    # Total length (m)
    dimension_length = 0

    # Order (Number of nodes per element) of mesh elements
    mesh_order = 1

    # Node array [i] = X_co-ordinate
    node_array = []

    # Element array [j, 0] = First Node index
    # Element array [j, 1] = Second Node index
    element_array = []
    
    def __init__(self, dimension_nodes, dimension_elements, mesh_order = 1):
        # Manage the Nodes of the mesh
        if isinstance(dimension_nodes, (int, float)):
            self.dimension_length = dimension_nodes
            self.n_elements = dimension_elements
            

            # generate nodes to be equal distances apart, spanning total length of x
            self.node_array = numpy.array((self.n_nodes))
            dim_increment = self.dimension/self.n_elements
            self.node_array[-1] = 0
            for i in range (0, self.n_nodes):
                self.node_array[i] = dim_increment
                dim_increment += dim_increment
            
        elif isinstance(dimension_nodes, NodeSpace1D):
            NodeSpace1D.__init__(dimension_nodes)

        # Manage the elements of the mesh
        if isinstance(dimension_elements, (int, float)):
            self.n_elements = dimension_elements
            if mesh_order == 0:
                self.n_nodes = dimension_elements + 0
            self.mesh_order = mesh_order
        elif isinstance(dimension_elements, ElementSpace1D):
            ElementSpace1D.__init__(dimension_elements)
        
        
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