import numpy

from base.polynomial import Polynomial
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
        Polynomial.__init__(self, self.generate_recursive(degree))
        if degree > 1:
            self.roots = get_roots(Polynomial(self.co_array))
        else:
            roots = [0]
    
    def __str__(self) -> str:
        sret = "{}\n".format(self.degree)
        sret += format(self.co_array)
        return sret

    def __repr__(self):
        return super().__repr__()

    # Generate Legendre polynomial(co-array) up to the n-th degree.
    #   - Uses recursive method
    def generate_recursive(self, order):
        # Pn(x) = (2n + 1)*x/(n+1) * Pn-1(x) - (n)/(n+1) * Pn-2(x) 
        #   - see https://en.wikipedia.org/wiki/Legendre_polynomials
        #     for details on recurrence relations.
        if order == 0:
            return numpy.array([1])
        elif order == 1:
            return numpy.array([0, 1])
        else:
            coefficient_array = numpy.zeros(order + 1)
            
            # Generate First term
            Pn_minOne = self.generate_recursive(order - 1)
            Pn_minOne = Pn_minOne*(2*order - 1)/(order)
            Pn_minOne = numpy.insert(Pn_minOne, [0], 0, axis=0)
            #print(f"Pn_min1:{Pn_minOne}")
            
            # Generate Second Term
            Pn_minTwo = self.generate_recursive(order - 2)
            Pn_minTwo = Pn_minTwo*-(order - 1)/(order)
            Pn_minTwo = numpy.append(Pn_minTwo, [0, 0])
            #print(f"Pn_min2:{Pn_minTwo}")

            # Combine Terms
            coefficient_array += Pn_minOne + Pn_minTwo
            #print(f"coeff_array:{coefficient_array}")

        return coefficient_array

# Define the Test functions and methods
def main():

    # Generate Legendre polynomials for various degrees
    for n in range(11):
        # Test generation for degree i
        legendre = Legendre(n)
        print(f"Test{n}|_Legendre:{repr(legendre)}, roots:{legendre.roots}")

if __name__ == "__main__":
    main()