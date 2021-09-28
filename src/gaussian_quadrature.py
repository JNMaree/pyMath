import numpy
import math

from polynomial import Polynomial
from newtons_method import Newtons_method, get_roots
from matrix import Matrix
from legendre_polynomial import Legendre


class GaussianQuad:
    """
    Gaussian Quadrature is a numerical approximation technique to calculate the 
    the definite integral of a function.
     - It utilises a weighted-sum of function values at prescribed points within the
        definitive domain described by the integral
     - To utilise this method, the definite interval needs to be translated to
        the interval: [-1; 1]
    """

    # Define the order of Gaussian Quadrature:
    #   - n_order = number of points / order of gaussian quadrature
    n_order = 1                     # Int (>= 1)
    
    # Define the legendre polynomials up to a point
    legendre = []              # Legendre Polynomial for specified order

    # Define the Quadrature Matrix:
    #   - Size: Order x 2:
    #       [n,0] = node position
    #       [n,1] = node weight value
    quadrature = []                 # Matrix (nx2)


    def __init__(self, n_points) -> None:
        self.n_order = n_points
        self.quadrature = numpy.zeros((n_points, 2))
        
        if n_points == 1:   # If first simple case, avoid generating legendre polynomials
            self.quadrature[0, 0] = 0
            self.quadrature[0, 1] = 2
        else:
            # generate legendre equation polynomial of degree n
            self.legendre_polynom = Legendre(n_points)
            print(f"legendre_polynomial:{self.legendre.co_array}, roots:{self.legendre.roots}")
            
            # use legendre polynomial to 
            for i in range(n_points):
                self.quadrature[i, 0] = self.legendre.roots[i]
                self.quadrature[i, 1] = self.calculate_weight_function(i, self.legendre.roots[i])


    def __str__(self) -> str:
        ret_str = "{}\n".format(self.n_order)
        for i in range(self.n_order):
            ret_str += "{}:{},\n".format(self.quadrature[i,0])
        return ret_str

    # Calculate the weight value correlating to specified root of Legendre polynomial
    def calculate_weight_function(self, i, root_i):
        # w_i = 2/(1 - (x_i)^2) * 2/(P'n(x_i)^2)
        #   - see https://en.wikipedia.org/wiki/Gaussian_quadrature for details on formula.
        deriv_x_i = self.legendre.derive().evaluate(root_i)
        print(f"i:{i}|root_i:{root_i}, dx_i{deriv_x_i}")
        return 2/(1-root_i**2) * 2/(deriv_x_i**2)

# Tests for the Gaussian Quadrature method
def main():
    # test function for legendre_polynomial + binomial_coefficient
    n_test = 3
    gquad = GaussianQuad(n_test)
    print("n_test:", gquad)


if __name__ == "__main__":
    main()
