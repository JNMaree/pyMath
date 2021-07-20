import numpy
import matplotlib.pyplot as plot

from mesh_1D import Mesh1Dimension, BoundaryCondition1D, SolutionSpace1D

class FiniteDifferenceMethod:

    solution_space = numpy.zeros(0)
    mesh_space = numpy.zeros(0)
    n_nodes = 0
    
    def __init__(self, mesh, material_properties, type1bcs, type2bcs):
        self.solution_space = numpy.zeros(mesh.n_elements)
        self.mesh_space = mesh.node_array()

    def solve(self):
        for i in range(self.n_nodes):
            
        
    def plot(self):
        plot.plot(self.mesh_space, self.solution_space)


def main():
    # Heat transfer test method:
    # - Create mesh using parameters:
    X_dimension = 12    # Distance specification (meters)
    N_elements = 20     # Number of finite elements in mesh
    FiniteMesh = Mesh1Dimension(X_dimension, N_elements)

    # - Analysis Conditions:
    #   $ Material properties:
    K = 20      # Constant Stiffness coefficient
    
    #   $ Type 1 (Dirichlet) Boundary Conditions(BCs):
    Type1_BC = 24       # Temperature specification
    Type1_Nodes = [0]   # Node indices subject to Type 1 BC
    BC_Type1 = BoundaryCondition1D(N_elements, Type1_BC, Type1_Nodes)
    
    #   $ Type 2 (Neumann) Boundary Conditions(BCs):
    Type2_BC = 16                   # Heat Flux specification
    Type2_Nodes = [N_elements - 1]  # Node indices subject to Type 2 BC
    BC_Type2 = BoundaryCondition1D(N_elements, Type2_BC, Type2_Nodes)
    
    FDM = FiniteDifferenceMethod(FiniteMesh, K, BC_Type1, BC_Type2)
    FDM.solve()
    FDM.plot()

if __name__ == "__main__":
    main()