import numpy

from polynomial import Polynomial

class Legendre(Polynomial):
    """
    Legendre Polynomials
    """

    def __init__(self, degree) -> None:
        self.degree = degree
        self.co_array = self.generate_recursive(degree)
    
    # Generate Legendre polynomials up to the n-th degree.
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
    
    def __str__(self) -> str:
        sret = "{}\n".format(self.degree)
        sret += format(self.co_array)
        return sret


# Define the Test functions and methods
def main():
    # Test legendre_polynomial for degree 3
    n_poly = 3
    legendre = Legendre(n_poly)
    print("Test1_Legendre:", legendre)

if __name__ == "__main__":
    main()