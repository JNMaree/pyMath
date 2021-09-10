import numpy
import matplotlib.pyplot as pyplot

from mesh_1D import Mesh1D, NodeSpace1D, ElementSpace1D
from polynomial import Polynomial
from matrix import Matrix

class FiniteDifferenceMethod:

    mesh = []

    material_matrix = []
    force_vector = []
    material_function = Polynomial([0, 0])

    type1BC = []
    type2BC = []
    
    def __init__(self, mesh, material_properties, bc_type1, bc_type2):
        self.mesh = mesh
        self.material_matrix = Matrix(numpy.zeros((mesh.element_space.n_nodes, mesh.element_space.n_nodes)))
        self.material_function = Polynomial([material_properties, 0])
        self.solution_space = bc_type1
        self.type1BC = bc_type1
        self.type2BC = bc_type2
        

    # The partial differential equations (PDEs) are solved using a Centred-Space, 
    # finite difference scheme:
    #       f'(x) = f(x + 1/2*h)/h - f(x-1/2*h)/h
    #
    # When this method is applied to the following differential equation:
    #   -d/dx(K(x) * dU(x)/dx) = F(X)               (Diffusion equation)
    # this results in:
    #
    #   -1/DX * ( K(x_i + DX/2) * ( U(x_i+1) - U(x_i) )/DX
    #           + K(x_i - DX/2) * ( U(x_i) - U(x_i-1) )/DX ) = F(x_i)
    # 
    # Rewriting the above equation in terms of U(x) results in the creation
    # of the matrices required to solve the problem:
    def setup(self):
        self.material_matrix[0,0] = 1.0
        for i in range(1, self.mesh.element_space.n_nodes - 1):
            x_i = self.mesh.element_space.nodes[i]
            DX = x_i - self.mesh.element_space.nodes[i - 1]
            DXdiv2 = DX/2
            DXDX = DX*DX
            #print("{}:, DX:{}, DXdiv2:{}, DXDX:{}", i, DX, DXdiv2, DXDX)
            self.material_matrix[i, i - 1] += -self.material_function.evaluate(x_i - DXdiv2)/DXDX
            self.material_matrix[i, i] += self.material_function.evaluate(x_i - DXdiv2)/DXDX
            self.material_matrix[i, i] += self.material_function.evaluate(x_i + DXdiv2)/DXDX
            self.material_matrix[i, i + 1] += -self.material_function.evaluate(x_i + DXdiv2)/DXDX
            
        self.material_matrix[self.mesh.element_space.n_nodes - 1, self.mesh.element_space.n_nodes - 1] = 1.0
        print(self.material_matrix)

    # Solve the matrix equations to generate the solution_space:
    def solve(self):
        self.mesh.solution_space = self.material_matrix.get_inverse * self.force_vector

    # Plot the nodes at their respective coordinates vs their respective solution values. 
    def plot(self):
        pyplot.plot(self.nodes, self.solution_space)

# Test Methods and Classes
def main():
    # Heat transfer test method:
    x_dimension = 12        # Distance specification (meters)
    n_elements = 10         # Number of finite elements in mesh
    start_pos = 0           # First Node position
    nodes_per_element = 2   # Amount of Nodes per element

    # Create mesh of discrete elements that consist of two nodes per element
    fdm_espace = ElementSpace1D(n_elements, x_dimension, start_pos, nodes_per_element)
    fdm_mesh = Mesh1D(fdm_espace)
    #print(fdm_mesh)
    
    # - Analysis Conditions:
    #   $ Material properties:
    K = 20      # Constant Stiffness coefficient
    
    #$  Type 1 (Dirichlet) Boundary Conditions(BCs):
    Type1_BC = 24       # Temperature specification
    Type1_Nodes = [0]   # Node indices subject to Type 1 BC
    BC_Type1 = NodeSpace1D(fdm_mesh.element_space.n_nodes)
    BC_Type1.assign_values(Type1_BC, Type1_Nodes)
    
    #$  Type 2 (Neumann) Boundary Conditions(BCs):
    Type2_BC = 16                   # Heat Flux specification
    Type2_Nodes = [n_elements - 1]  # Node indices subject to Type 2 BC
    BC_Type2 = NodeSpace1D(fdm_mesh.element_space.n_nodes)
    BC_Type2.assign_values(Type2_BC, Type2_Nodes)
    
    FDM = FiniteDifferenceMethod(fdm_mesh, K, BC_Type1, BC_Type2)
    FDM.setup()
    #FDM.solve()
    #FDM.plot()
    
if __name__ == "__main__":
    main()