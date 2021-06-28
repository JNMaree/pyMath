import numpy

class Polynomial:
# Homogenous, single-variable (x) polynomials are treated as coefficient arrays (co-arrays).
#   x^3 -3x^2 + 5x + 10 equates to a co-array of [10, 5, -3,  1]
#   - x powers are equivalent to array position: [0,  1,  2,  3]
#   - the degree of the polynomial is therefore equivalent to the length of the coefficient array

    # coefficient array
    co_array = numpy.array([])
    degree = 0

    def __init__(self, coefficient_array):
        self.co_array = numpy.array(coefficient_array)
        self.degree = len(coefficient_array)

    # represent polynomial in format: ax^i + bx^(i-1) + cx^(i-2) + ...
    def __str__(self):
        ret = ""
        for i in range(self.degree):
            if i > 0:
                ret += self.co_array[i]
                ret += "x^"
                ret += i
            else:
                ret += self.co_array[i]
            ret += " + "
        return ret

    def __add__(self, b):
        a_size = self.degree
        b_size = b.degree
        added = []
        add_list = []

        # equal degree equations
        if a_size == b_size:        
            for i in range(a_size):
                add_list.append(self.co_array[i] + poly_b[i])
            added = numpy.array(add_list)
        # self degree > poly_b degree
        elif a_size > b_size:
            for i in range(a_size):
                if i < b_size:
                    add_list.append(self.co_array[i] + poly_b[i])
                else:
                    add_list.append(self.co_array[i])
            added = numpy.array(add_list)
        # poly_b degree > self degree
        else:
            for i in range(b_size):
                if i < a_size:
                    add_list.append(self.co_array[i] + poly_b[i])
                else:
                    add_list.append(poly_b[i])
            added = numpy.array(add_list)
        return added

    # Calculate a polynomial function f(x) by providing x and a co-array
    def calculate(self, x):
        sum = 0
        for i in range(self.co_array.size):
            sum += self.co_array[i]*(x**i)
        return sum

    # Calculate a function's derivative from a co-array
    def derivative(self, degree):
        derivative_poly = numpy.empty(self.co_array.size - 1)
        for i in range(self.co_array.size - 1):
            derivative_poly[i] = self.co_array[i+1]*(i+1)
        return derivative_poly


# Add polynomial co-arrays of equal or different sizes
def polynomials_add(poly_a, poly_b):
    
    