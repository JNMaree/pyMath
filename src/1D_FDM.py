import numpy
import matplotlib.pyplot as plot

from elementspace_1D import NodeSpace1D, ElementSpace1D
from polynomial import Polynomial
from matrix import Matrix

class FiniteDifferenceMethod:

    mesh = []               # ElementSpace

    material_matrix = []    # Matrix(Square)
    force_vector = []       # Matrix(Vector)
    material_function = []  # Polynomial

    solution_space = []     # Matrix(Vector)

    def __init__(self, element_space, material_property, bc_type1, bc_type2):
        self.mesh = element_space
        self.material_matrix = Matrix(numpy.zeros((element_space.n_nodes, element_space.n_nodes)))
        
        # Define the linear material function for constant material properties
        self.material_function = Polynomial([material_property, 0])
        
        # Define the solution space to accomodate the initial type1 boundary conditions
        if isinstance(bc_type1, NodeSpace1D):
            self.solution_space = Matrix(bc_type1.nodes)
        elif isinstance(bc_type1, numpy.ndarray):
            self.solution_space = Matrix(bc_type1)
        elif isinstance(bc_type1, Matrix):
            self.solution_space = bc_type1
        else:
            raise TypeError("bc_type1: Unknown Type")

        # Define the force vector to include the initial type2 boundary conditions
        if isinstance(bc_type2, NodeSpace1D):
            self.force_vector = Matrix(bc_type2.nodes)
        elif isinstance(bc_type2, numpy.ndarray):
            self.force_vector = Matrix(bc_type2)
        elif isinstance(bc_type2, Matrix):
            self.force_vector = bc_type2
        else:
            raise TypeError("bc_type2: Unknown Type")
        
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
        for i in range(1, self.mesh.n_nodes - 1):
            x_i = self.mesh.nodes[i]
            DX = x_i - self.mesh.nodes[i - 1]
            DXdiv2 = DX/2
            DXDX = DX*DX
            #print("{}:, DX:{}, DXdiv2:{}, DXDX:{}", i, DX, DXdiv2, DXDX)
            self.material_matrix[i, i - 1] += -self.material_function.evaluate(x_i - DXdiv2)/DXDX
            self.material_matrix[i, i] += self.material_function.evaluate(x_i - DXdiv2)/DXDX
            self.material_matrix[i, i] += self.material_function.evaluate(x_i + DXdiv2)/DXDX
            self.material_matrix[i, i + 1] += -self.material_function.evaluate(x_i + DXdiv2)/DXDX
            
        self.material_matrix[self.mesh.n_nodes - 1, self.mesh.n_nodes - 1] = 1.0
        #print(self.material_matrix)

    # Solve the matrix equations to generate the solution_space:
    def solve(self):
        self.solution_space = self.material_matrix.get_inverse() * self.force_vector
        #print("Inverse:", self.material_matrix.get_inverse())
        #print("Force_Vector:", self.force_vector)
        #print("Solution_space:", self.solution_space)

    # Plot the nodes at their respective coordinates vs their respective solution values. 
    def plot(self):
        plot.plot(self.mesh.nodes, self.solution_space.matrix)
        plot.xlabel("X coordinates")
        plot.ylabel("Degree-of-Freedom Value")
        plot.show()

# Test Methods and Classes
def main():
    # Heat transfer test method
    # Create mesh using parameters:
    x_dimension = 12        # Distance specification (meters)
    n_elements = 8          # Number of finite elements in mesh
    start_pos = 0           # First Node position
    nodes_per_element = 2   # Number of Nodes per element

    # Create mesh of discrete elements that consist of nodes_per_element
    fdm_espace = ElementSpace1D(n_elements, x_dimension, start_pos, nodes_per_element)
    
    # Analysis Conditions:
    #   - Material properties:
    K = 20      # Constant Stiffness coefficient
    
    #   - Type 1 (Dirichlet) Boundary Conditions(BCs):
    Type1_BC = 24       # Temperature specification
    Type1_Nodes = [0]   # Node indices subject to Type 1 BC
    BC_Type1 = NodeSpace1D( numpy.zeros( fdm_espace.n_nodes ) )
    BC_Type1.assign_values(Type1_BC, Type1_Nodes)
    #print("BC_Type1:", BC_Type1)

    #   - Type 2 (Neumann) Boundary Conditions(BCs):
    Type2_BC = 16                   # Heat Flux specification
    Type2_Nodes = [n_elements]  # Node indices subject to Type 2 BC
    BC_Type2 = NodeSpace1D( numpy.zeros( fdm_espace.n_nodes ) )
    BC_Type2.assign_values(Type2_BC, Type2_Nodes)
    #print("BC_Type2P:", BC_Type2)

    FDM = FiniteDifferenceMethod(fdm_espace, K, BC_Type1, BC_Type2)
    FDM.setup()
    FDM.solve()
    FDM.plot()
    
if __name__ == "__main__":
    main()