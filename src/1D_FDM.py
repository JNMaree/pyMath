import numpy
import matplotlib.pyplot as plot

from mesh_1D import Mesh1D, NodeSpace1D, ElementSpace1D

class FiniteDifferenceMethod(Mesh1D):

    solution_space = []

    material_properties = 0
    
    def __init__(self, mesh, material_properties, type1bcs, type2bcs):
        self.mesh = mesh
        self.solution_space = NodeSpace1D(mesh)
        self.material_properties = material_properties
        self.type1BC = type1bcs
        self.type2BC = type2bcs

    def solve(self):
        for i in range(self.solution_space):
            pass
        
    def plot(self):
        plot.plot(self.node_array, self.solution_space)


def main():
    # Heat transfer test method:
    
    X_dimension = 12    # Distance specification (meters)
    N_elements = 20     # Number of finite elements in mesh

    # Create mesh using provided parameters
    finiteMesh = Mesh1D(X_dimension, N_elements)

    # - Analysis Conditions:
    #   $ Material properties:
    K = 20      # Constant Stiffness coefficient
    
    #   $ Type 1 (Dirichlet) Boundary Conditions(BCs):
    Type1_BC = 24       # Temperature specification
    Type1_Nodes = [0]   # Node indices subject to Type 1 BC
    BC_Type1 = NodeSpace1D(finiteMesh.n_nodes)
    BC_Type1.assign_values(Type1_BC, Type1_Nodes)
    
    #   $ Type 2 (Neumann) Boundary Conditions(BCs):
    Type2_BC = 16                   # Heat Flux specification
    Type2_Nodes = [N_elements - 1]  # Node indices subject to Type 2 BC
    BC_Type2 = NodeSpace1D(finiteMesh.n_nodes)
    BC_Type2.assign_values(Type2_BC, Type2_Nodes)
    
    FDM = FiniteDifferenceMethod(finiteMesh, K, BC_Type1, BC_Type2)
    FDM.solve()
    FDM.plot()

if __name__ == "__main__":
    main()