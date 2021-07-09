import numpy
import math

from polynomial import Polynomial
from newtons_method import Newtons_Method

#global array of legendre polynomials
legendre_polynomials = []

def calculate_gauss_legendre_points(num_of_points = 1):
    gaussian_points_weights = numpy.array((num_of_points, 2))
    if num_of_points == 1:
        gaussian_points_weights[0, 0] = 0
        gaussian_points_weights[0, 1] = 2
    else:
        # generate legendre equation polynomial of degree n
        legendrePolynomial = legendre_polynomial_recursive(num_of_points)
        legendreRoots = 
        # use legendre polynomial to 
        for i in range(num_of_points):
            gaussian_points_weights[i, 0] = legendrePolynomial.ca
            gaussian_points_weights[i, 1] = 
    return gaussian_points_weights

#Generate Legendre polynomials using recursion up to the n-th degree.
def legendre_polynomial_recursive(n):
    # Pn(x) = (2n - 1)*x/n * Pn-1(x) - (n - 1)*1/n * Pn-2(x) 
    #see https://en.wikipedia.org/wiki/Legendre_polynomials for details on recurrence relations.
    if n == 0:
        return Polynomial([1])
    elif n == 1:
        return Polynomial([1, 0])
    else:
        coefficient_array = numpy.zeros(n + 1)
        Pn_minOne = (2*n - 1)/n * legendre_polynomial_recursive(n - 1)
        Pn_minTwo = -(n - 1)/n * legendre_polynomial_recursive(n - 2)
        coefficient_array += numpy.append(Pn_minOne, 0.) + numpy.concatenate(([0], [0], Pn_minTwo))
    return Polynomial(coefficient_array)

#Calculate the weights of a set of roots 
def calculate_weight_function(x_i, n):
    # w_i = 2/(1 - (x_i)^2) * 2/(P'n(x_i)^2)
    #see https://en.wikipedia.org/wiki/Gaussian_quadrature for details on formula.
    return 2/(1-x_i**2) * 2/(legendre_polynomials[n].derivative().calculate(x_i)**2)

def main(degree_n):
    # test function for legendre_polynomial + binomial_coefficient
    legendre_polynomials = numpy.zeros((degree_n, degree_n))
    for i in range(degree_n):
        legendre_polynomials += legendre_polynomial_recursive(degree_n)
        

if __name__ == "__main__":
    main(3)
