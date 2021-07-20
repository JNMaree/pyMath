import numpy

class Mesh1D:

    dimension_x = 0
    n_elements = 0
    n_nodes = 0
    mesh_order = 1
 
    node_array = numpy.array([])
    element_array = numpy.array([])
    
    def __init__(self, x_dimension, num_of_elements, mesh_order = 1):
        self.dimension_x = x_dimension
        self.n_elements = num_of_elements
        if mesh_order == 1:
            self.n_nodes = num_of_elements + 1
        self.mesh_order = mesh_order

    # generate nodes (2 per element) to be equal distances apart, spanning total length of x
    def generate_equidistant_nodes(self):
        self.node_array = numpy.array((self.n_nodes))
        dim_increment = self.dimension_x/self.n_elements
        self.node_array[0] = 0
        for i in range (1, self.n_nodes):
            self.node_array[i] = dim_increment
            dim_increment += dim_increment

    # generate elements to 
    def generate_elements(self, nodes_per_element = 2):
        node_end = self.n_nodes - 1
        self.element_array = numpy.array((node_end, nodes_per_element))
        for i in range(0, node_end):
            for j in range(0, nodes_per_element):
                self.element_array[i, j] = j

class BoundaryCondition1D:

    def __init__(self, n_elements, bc_value, index_array):
        if isinstance(n_elements, int):
            self.n_elements = elements
        elif isinstance(n_elements, Mesh1Dimension):
            self.n_elements = n_elements.n_elements
        
        self.node_array = numpy.zeros(self.n_elements)
        for x in index_array:
            self.node_array[x] = bc_value

class SolutionSpace1D(Mesh1D):

    def __init__(self):