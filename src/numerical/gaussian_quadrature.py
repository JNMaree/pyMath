import numpy
import math

from base.polynomial import Polynomial
from base.matrix import Matrix
from newtons_method import Newtons_method, get_roots
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
    order = 1                     # Int (>= 1)
    
    # Define the legendre polynomials up to a point
    legendre = []              # Legendre Polynomial for specified order

    # Define the Quadrature Matrix:
    #   - Size: Order x 2:
    #       [n,0] = node position
    #       [n,1] = node weight value
    quadrature = []                 # Matrix (nx2)


    def __init__(self, n_points) -> None:
        self.order = n_points
        self.quadrature = numpy.zeros((n_points, 2))
        
        if n_points == 1:   # If first simple case, avoid generating legendre polynomials
            self.quadrature[0, 0] = 0
            self.quadrature[0, 1] = 2
        else:
            # generate legendre equation polynomial of degree n
            self.legendre = Legendre(n_points)
            # Print Legendre polynomial info
            #print(f"legendre_polynomial:{self.legendre.co_array}, roots:{self.legendre.roots}")
            
            # use legendre polynomial to 
            for i in range(n_points):
                self.quadrature[i, 0] = self.legendre.roots[i]
                self.quadrature[i, 1] = self.calculate_weight_function(i, self.legendre.roots[i])


    def __str__(self) -> str:
        ret_str = "{}\n".format(self.order)
        for i in range(self.order):
            ret_str += "{}:{},\n".format(self.quadrature[i,0], self.quadrature[i, 1])
        return ret_str

    # Calculate the weight value correlating to specified root of Legendre polynomial
    def calculate_weight_function(self, i, root_i) -> float:
        # w_i = 2/(1 - (x_i)^2) * 2/(P'n(x_i)^2)
        #   - see https://en.wikipedia.org/wiki/Gaussian_quadrature for details on formula.
        derivative = self.legendre.derive()
        deriv_x_i = derivative.evaluate(root_i)
        
        # Print root info used for calculating corresponding weight values
        #print(f"i:{i}|root_i:{root_i}, dx_i:{deriv_x_i}, deriv:{repr(derivative)}")
        return 2/((1-root_i**2)*(deriv_x_i**2))

    # Calulate definite integral (a numerical approximation) of a polynomial function
    #  between limits a and b
    #   - translates [a,b] limits to [-1,1]
    #   - calculate the weighted sum of function values at each Gaussian point
    def calculate_definite_integral(self, polynomial, a, b):
        ba = (b - a)/2
        ab = (a + b)/2
        fret = 0.0
        for p in range(self.gaussian.order):
            val = ba*self.quadrature[p, 0] + ab
            fret += self.quadrature[p, 1]*polynomial.evaluate(val)
        fret *= ba
        return fret

# Tests for the Gaussian Quadrature method
def main():
    # test function for legendre_polynomial + binomial_coefficient
    n_test = 4
    gquad = GaussianQuad(n_test)
    print("n_test:", gquad)


if __name__ == "__main__":
    main()
