import numpy
import matplotlib.pyplot as plot

from mesh_1D import Mesh1D, BoundaryCondition1D, SolutionSpace1D

class FiniteElementMethod:

    def __init__(self, mesh, boundary_conditions, material_properties):
        pass
        
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
    # Heat transfer test method:
    
    # Create mesh using parameters:
    X_dimension = 10    # Distance in meters
    N_elements = 8      # Number of finite elements in domain
    Mesh = Mesh1Dimension(X_dimension, N_elements)
    
    # Analysis Conditions:
    
    # Material Properties:
    K = 20      # Stiffness Coefficient (Material Property)

    # Type 1 (Dirichlet) boundary conditions:
    Type1_BC = 24       # Temperature specification
    Type1_Nodes = [0]   # Node indices subject to Type 1 BC
    BC_Type1 = BoundaryCondition1D(Type1_BC, Type1_Nodes)

    # Type 2 (Neumann) boundary condition:
    Type2_BC = 16                   # Heat Flux Specification
    Type2_Nodes = [N_elements - 1]  # Node indices subject to Type 2 BC
    BC_Type2 = BoundaryCondition1D(Type2_BC, Type2_Nodes)
    
    
    

if __name__ == "__main__":
    main()