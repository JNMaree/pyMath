import numpy

class Mesh_1D:

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

# 
def generate_basis_functions(element_array, function_order = 1):
    if function_order == 1:
        # linear elements
        pass    
    elif function_order == 2:
        # quadratic elements
        pass
    elif function_order == 3:
        # cubic elements
        pass
    
def linear_interpolationY(x_0, x_1, y_0, y_1, X):
    return y_0 + (X - x_0)*(y_1 - y_0)/(x_1 - x_0)

def solve_PDE(basis_function_array):
    pass

def print_solution(solution_array):
    for i in solution_array:
        for j in i:
            print("node:{}",i)
            print(", f:{}", j)


def main():
    
    # 'Mesh' parameters
    X_dimension = 10    # distance in meters
    N_elements = 8      # number of elements in domain
    
    # Analysis conditions
    Type1_BC = 40       # Type 1 (Dirichlet) boundary condition
    Type1_Node = 0      # Node position subject to Type 1 BC
    
    Type2_BC = 10       # Type 2 (Neumann) boundary condition
    Type2_Node = 8      # Node position subject to Type 2 BC
    
    K_1 = 20            # Stiffness Coefficient (Material Property)
    
    # Code execution:
    mesh1 = Mesh_1D(X_dimension, N_elements)
    mesh1.generate_equidistant_nodes()
    mesh1.generate_elements()
    

if __name__ == "__main__":
    main()