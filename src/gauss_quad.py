import numpy
import math


def generate_gauss_legendre_points(point_order):
    gaussian_points_weights = numpy.array((point_order*2 - 1, 2))
    if point_order == 1:
        gaussian_points_weights[0, 0] = 0
        gaussian_points_weights[0, 1] = 2
    elif point_order == 2:
        gaussian_points_weights[0, 0] = -1/math.sqrt(3)
        gaussian_points_weights[0, 1] = 1
        gaussian_points_weights[1, 0] = 1/math.sqrt(3)
        gaussian_points_weights[1, 1] = 1
    return gaussian_points_weights

#Generate Legendre polynomials recursively up to the n-th degree.
def legendre_polynomial_recursive(n):
    # Pn(x) = (2n - 1)*x/n * Pn-1(x) - (n - 1)*1/n * Pn-2(x) 
    #see https://en.wikipedia.org/wiki/Legendre_polynomials for details on recurrence relations

    if n == 0:
        return numpy.array([1])
    elif n == 1:
        return numpy.array([1, 0])
    else:
        coefficient_array = numpy.zeros(n + 1)
        Pn_minOne = (2*n - 1)/n * legendre_polynomial_recursive(n - 1)
        Pn_minTwo = -(n - 1)/n * legendre_polynomial_recursive(n - 2)
        coefficient_array += numpy.append(Pn_minOne, 0.) + numpy.concatenate(([0], [0], Pn_minTwo))
    return coefficient_array

#Calculate x in a homogenous polynomial function represented by an array of coefficents where the index
# represents the degree (power) of x.
def calculate_polynomial(coefficient_array, x):
    poly = 0
    for i in range(coefficient_array):
        poly += coefficient_array[i] * (x**i)
    return poly

def main():
    # test function for legendre_polynomial + binomial_coefficient
    for i in range(11):
        print("Legendre_Polynomial(", i, "):", legendre_polynomial_recursive(i))


if __name__ == "__main__":
    main()
