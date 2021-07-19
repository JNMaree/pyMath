import numpy
import matplotlib.pyplot as plt

from mesh_1D import Mesh1Dimension, MeshBC

class FiniteDifferenceMethod:

    dirichlet_bc = 0
    neumann_bc = 0
    
    def __init__(self, mesh, material_properties, type1bcs, type2bcs):
        pass


def main():
    # Heat transfer test method:

    # Create mesh using parameters:
    X_dimension = 12    # Distance specification (meters)
    N_elements = 20     # Number of finite elements in mesh
    FiniteMesh = Mesh1Dimension(X_dimension, N_elements)

    # Analysis Conditions:

    # Material properties:
    K = 20      # Constant Stiffness coefficient
    
    # Type 1 (Dirichlet) Boundary Conditions(BCs):
    Type1_BC = 24       # Temperature specification
    Type1_Nodes = [0]   # Node indices subject to Type 1 BC
    BC_Type1 = MeshBC(N_elements, Type1_BC, Type1_Nodes)
    
    # Type 2 (Neumann) Boundary Conditions(BCs):
    Type2_BC = 16                   # Heat Flux specification
    Type2_Nodes = [N_elements - 1]  # Node indices subject to Type 2 BC
    BC_Type2 = MeshBC(N_elements, Type2_BC, Type2_Nodes)
    
    FDM = FiniteDifferenceMethod(FiniteMesh, K, BC_Type1, BC_Type2)
    
    pass

if __name__ == "__main__":
    main()