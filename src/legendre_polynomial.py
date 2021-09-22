import numpy

from polynomial import Polynomial
from newtons_method import get_roots

class Legendre(Polynomial):
    """
    Legendre Polynomials are a set of polynomials of increasing order that
    have various use cases in numerical mathematics.
    
    These Polynomials are defined on the interval [-1,1] and the roots of 
    the polynomial are used in the numerical approximation of definite integrals.

    """

    # Define a list of the roots of the Legendre Polynomials
    roots = []

    def __init__(self, degree) -> None:
        self.degree = degree
        self.co_array = self.generate_recursive(degree)
        self.roots = get_roots(Polynomial(self.co_array))
    
    def __str__(self) -> str:
        sret = "{}\n".format(self.degree)
        sret += format(self.co_array)
        return sret

    def __repr__(self):
        return super().__repr__()

    # Generate Legendre polynomial(co-array) up to the n-th degree.
    #   - Uses recursive method
    def generate_recursive(self, order):
        # Pn(x) = (2n - 1)*x/n * Pn-1(x) - (n - 1)*1/n * Pn-2(x) 
        #   - see https://en.wikipedia.org/wiki/Legendre_polynomials
        #     for details on recurrence relations.
        if order == 0:
            return numpy.array([1])
        elif order == 1:
            return numpy.array([1, 0])
        else:
            coefficient_array = numpy.zeros(order + 1)
            Pn_minOne = (2*order - 1)/order * self.generate_recursive(order - 1)
            Pn_minTwo = -(order - 1)/order * self.generate_recursive(order - 2)
            coefficient_array += numpy.append(Pn_minOne, 0.) + numpy.concatenate(([0], [0], Pn_minTwo))
        return coefficient_array


# Define the Test functions and methods
def main():
    # Test legendre_polynomial for degree 3
    n_poly = 4
    legendre = Legendre(n_poly)
    print("Test1_Legendre(STR):\n", legendre)
    print("Test1_Legendre(REPR):\n", legendre.__repr__())
    print("Test1_Legendre(roots):\n", format(legendre.roots))

if __name__ == "__main__":
    main()