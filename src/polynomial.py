import numpy

class Polynomial:
# Homogenous polynomials of a single variable (x) are treated as coefficient arrays (co-arrays).
#   x^3 -3x^2 + 5x + 10 equates to a co-array of [10, 5, -3,  1]
#   - x powers are equivalent to array position: [0,  1,  2,  3]

    def __init__(self, co_array):
        pass
    
    # Calculate a polynomial function f(x) by providing x and a co-array
    def calculate(self, co_array, x):
        sum = 0
        for i in range(co_array.size):
            sum += co_array[i]*(x**i)
        return sum

    # Calculate a function's derivative from a co-array
    def derive(self, co_array):
        derivative_poly = numpy.empty(co_array.size - 1)
        for i in range(co_array.size - 1):
            derivative_poly[i] = co_array[i+1]*(i+1)
        return derivative_poly

# Add polynomial co-arrays of equal or different sizes
def add(poly_a, poly_b):
    added = []
    add_list = []
    a_size = poly_a.size
    b_size = poly_b.size
    # poly
    if a_size == b_size:        
        for i in range(a_size):
            add_list.append(poly_a[i] + poly_b[i])
        added = numpy.array(add_list)
    # poly_a degree > poly_b degree
    elif a_size > b_size:
        for i in range(a_size):
            if i < b_size:
                add_list.append(poly_a[i] + poly_b[i])
            else:
                add_list.append(poly_a[i])
        added = numpy.array(add_list)
    # poly_b degree > poly_a degree
    else:
        for i in range(b_size):
            if i < a_size:
                add_list.append(poly_a[i] + poly_b[i])
            else:
                add_list.append(poly_b[i])
        added = numpy.array(add_list)
    return added
    