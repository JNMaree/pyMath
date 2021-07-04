import numpy

class Mesh_1D:

    dimension_x = 0
    n_elements = 0
    n_nodes = 0
    mesh_order = 1
    
    nodes_array = numpy.array([])
    elements_array = numpy.array([])
    
    def __init__(self, x_dimension, num_of_elements, mesh_order = 1):
        self.dimension_x = x_dimension
        self.n_elements = num_of_elements
        if mesh_order == 1:
            self.n_nodes = num_of_elements + 1
        self.mesh_order = mesh_order
        self.generate_nodes()
        self.generate_elements()
    
    def generate_nodes(self):
        self.nodes_array = numpy.array((self.n_nodes))
        dim_increment = self.dimension_x/self.n_elements
        self.nodes_array[0] = 0
        for i in range (1, self.n_nodes):
            self.nodes_array[i] = dim_increment
            dim_increment += dim_increment

    def generate_elements(self):
        node_end = self.n_nodes - 1
        element_array = numpy.array((node_end, 2))
        for i in range(0, node_end):
            element_array[i, 0] = self.nodes_array[i]
            element_array[i, 1] = self.nodes_array[i + 1]
        return element_array

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
    BC_type1 = 40       # Type 1 (Dirichlet) boundary condition
    Node_Type1 = 0      # Node position subject to Type 1 BC
    
    BC_type2 = 10       # Type 2 (Neumann) boundary condition
    Node_Type2 = 8      # Node position subject to Type 2 BC
    
    K_ = 20             # Stiffness Coefficient (Material Property)
    
    # Code execution:
    mesh_test = Mesh_1D(X_dimension, N_elements)
    
    
    

if __name__ == "__main__":
    main()