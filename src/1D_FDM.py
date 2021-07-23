import numpy
import matplotlib.pyplot as pyplot

from mesh_1D import Mesh1D, NodeSpace1D, ElementSpace1D

class FiniteDifferenceMethod(Mesh1D):

    solution_space = []

    material_property = 0

    type1BC = []
    type2BC = []
    
    def __init__(self, mesh, material_properties, bc_type1, bc_type2):
        self.mesh1D = mesh
        self.solution_space = NodeSpace1D(mesh)
        self.material_property = material_properties
        self.type1BC = bc_type1
        self.type2BC = bc_type2

    # The partial differential equations (PDEs) are solved using a Centred-Space, 
    # finite difference scheme:
    # f'(x) = f(x + 1/2*h) - f(x-1/2*h)
    def solve(self):
        temp_solution_space = self.solution_space
        for i in range(self.n_nodes):
            self.solution_space[i] = temp_solution_space[i] + self.material_property
            temp_solution_space[i] = self.solution_space[i]
        
    def plot(self):
        pyplot.plot(self.nodes, self.solution_space)


def main():
    # Heat transfer test method:
    
    X_dimension = 12    # Distance specification (meters)
    N_elements = 20     # Number of finite elements in mesh

    # Create mesh of discrete elements that consist of two nodes per element
    fdm_mesh = Mesh1D(X_dimension, N_elements)

    # - Analysis Conditions:
    #   $ Material properties:
    K = 20      # Constant Stiffness coefficient
    
    #   $ Type 1 (Dirichlet) Boundary Conditions(BCs):
    Type1_BC = 24       # Temperature specification
    Type1_Nodes = [0]   # Node indices subject to Type 1 BC
    BC_Type1 = NodeSpace1D(fdm_mesh.n_nodes)
    BC_Type1.assign_values(Type1_BC, Type1_Nodes)
    
    #   $ Type 2 (Neumann) Boundary Conditions(BCs):
    Type2_BC = 16                   # Heat Flux specification
    Type2_Nodes = [N_elements - 1]  # Node indices subject to Type 2 BC
    BC_Type2 = NodeSpace1D(fdm_mesh.n_nodes)
    BC_Type2.assign_values(Type2_BC, Type2_Nodes)
    
    FDM = FiniteDifferenceMethod(fdm_mesh, K, BC_Type1, BC_Type2)
    FDM.solve()
    FDM.plot()

if __name__ == "__main__":
    main()