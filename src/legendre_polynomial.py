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
        Polynomial.__init__(self, self.generate_recursive(degree))
        if degree > 1:
            self.roots = get_roots(Polynomial(self.co_array))
        else:
            roots = [1]
    
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
        order -= 1
        if order == -1:
            return numpy.array([1])
        elif order == 0:
            return numpy.array([1, 0])
        else:
            coefficient_array = numpy.zeros(order + 2)
            Pn_minOne = (2*order + 1)/(order + 1) * self.generate_recursive(order)
            #print("Pn_min1:", Pn_minOne)
            Pn_minTwo = -order/(order + 1) * self.generate_recursive(order - 1)
            #print("Pn_min2:", Pn_minTwo)
            coefficient_array += numpy.append(Pn_minOne, 0) + numpy.concatenate(([0], [0], Pn_minTwo))        
        #print("coeff_array:", coefficient_array)
        #print("flipd_array:", numpy.flip(coefficient_array))
        return numpy.flip(coefficient_array)


# Define the Test functions and methods
def main():

    # Generate Legendre polynomials for various degrees
    for n in range(5):
        # Test generation for degree i
        legendre = Legendre(n)
        print(f"Test{n}|_Legendre:{repr(legendre)}, roots:{legendre.roots}")

if __name__ == "__main__":
    main()