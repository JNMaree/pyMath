import numpy

from polynomial import Polynomial

class LegendrePolynomial:
    
    n_order = 1

    polynomial = []

    def __init__(self, order) -> None:
        self.n_order = order
        self.generate_legendre_polynomial_recursive()

    # Generate Legendre polynomials up to the n-th degree.
    #   - Uses recursive method
    def generate_legendre_polynomial_recursive(self):
        # Pn(x) = (2n - 1)*x/n * Pn-1(x) - (n - 1)*1/n * Pn-2(x) 
        #see https://en.wikipedia.org/wiki/Legendre_polynomials for details on recurrence relations.
        if self.n_order == 0:
            self.polynomial = Polynomial([1])
        elif self.n_order == 1:
            self.polynomial = Polynomial([1, 0])
        else:
            coefficient_array = numpy.zeros(self.n_order + 1)
            Pn_minOne = (2*self.n_order - 1)/self.n_order * self.legendre_polynomial_recursive(self.n_order - 1)
            Pn_minTwo = -(self.n_order - 1)/self.n_order * self.legendre_polynomial_recursive(self.n_order - 2)
            coefficient_array += numpy.append(Pn_minOne, 0.) + numpy.concatenate(([0], [0], Pn_minTwo))
        self.polynomial = Polynomial(coefficient_array)

    def evaluate(self, x):
        self.polynomial.evaluate(x)