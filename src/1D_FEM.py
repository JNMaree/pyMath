import numpy
from mesh_1D import Mesh1Dimension

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
    mesh1 = Mesh1Dimension(X_dimension, N_elements)
    mesh1.generate_equidistant_nodes()
    mesh1.generate_elements()
    

if __name__ == "__main__":
    main()