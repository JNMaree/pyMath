import numpy
import matplotlib.pyplot as pyplot

from mesh_1D import Mesh1D, NodeSpace1D, ElementSpace1D

class FiniteElementMethod(Mesh1D):

    solution_space = []

    material_property = 0

    type1BC = []
    type2BC = []

    def __init__(self, mesh, material_properties, bc_type1, bc_type2):
        self.mesh1D = mesh
        self.solution_space = NodeSpace1D(mesh)
        self.type1BC = bc_type1
        self.type2BC = bc_type2
        
    # 
    def generate_basis_functions(self, element_array, function_order = 1):
        if function_order == 1:
            # linear elements
            pass    
        elif function_order == 2:
            # quadratic elements
            pass
        elif function_order == 3:
            # cubic elements
            pass
        
    def linear_interpolationY(self, x_0, x_1, y_0, y_1, X):
        return y_0 + (X - x_0)*(y_1 - y_0)/(x_1 - x_0)

    # The Partial Differential Equations are solved using ...
    def solve(self):
        pass

    # Plot the solution_space on the node coordinates
    def plot(self):
        pyplot.plot(self.mesh1D.nodes, self.solution_space)


def main():
    # Heat transfer test method:
    
    # Create mesh using parameters:
    X_dimension = 10    # Distance in meters
    N_elements = 8      # Number of finite elements in domain
    fem_mesh = Mesh1D(X_dimension, N_elements)
    
    # Analysis Conditions:
    
    # Material Properties:
    K = 20      # Stiffness Coefficient (Material Property)

    # Type 1 (Dirichlet) boundary conditions:
    Type1_BC = 24       # Temperature specification
    Type1_Nodes = [0]   # Node indices subject to Type 1 BC
    BC_Type1 = NodeSpace1D(fem_mesh.n_nodes)
    BC_Type1.assign_values(Type1_BC, Type1_Nodes)

    # Type 2 (Neumann) boundary condition:
    Type2_BC = 16                   # Heat Flux Specification
    Type2_Nodes = [N_elements]      # Node indices subject to Type 2 BC
    BC_Type2 = NodeSpace1D(fem_mesh.n_nodes)
    BC_Type2.assign_values(Type2_BC, Type2_Nodes)

    FEM = FiniteElementMethod(fem_mesh, K, BC_Type1, BC_Type2)
    FEM.solve()
    FEM.plot()

if __name__ == "__main__":
    main()