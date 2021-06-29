import numpy

class Polynomial:
    '''
    Homogenous, single-variable (x) polynomials are treated as coefficient arrays (co-arrays).
    x^3 -3x^2 + 5x + 10 equates to a co-array of [10, 5, -3,  1]
    - x powers are equivalent to array position: [0,  1,  2,  3]
    - the degree of the polynomial is therefore equivalent to the length of the coefficient array
    '''

    # coefficient array
    degree = 0
    co_array = numpy.zeros(degree)

    def __init__(self, param):
        if isinstance(param, int):
            self.degree = param
            self.co_array = numpy.zeros(param)
        elif isinstance(param, numpy.ndarray):
            self.co_array = param
            self.degree = param.size
        elif isinstance(param, (list)):
            self.co_array = numpy.array(param)
            self.degree = len(param)
        else:
            raise TypeError

    # Overload the array position('[]') operator
    def __getitem__(self, key):
        return self.co_array[key]

    def __setitem__(self, key, value):
        self.co_array[key] = value

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

    # overload the addition('+') arithmetic operator
    def __add__(self, b):
        a_size = self.degree
        b_size = b.degree
        added = []
        add_list = []

        # equal degree equations
        if a_size == b_size:        
            for i in range(a_size):
                add_list.append(self.co_array[i] + b[i])
            added = numpy.array(add_list)
        # self degree > poly_b degree
        elif a_size > b_size:
            for i in range(a_size):
                if i < b_size:
                    add_list.append(self.co_array[i] + b[i])
                else:
                    add_list.append(self.co_array[i])
            added = numpy.array(add_list)
        # poly_b degree > self degree
        else:
            for i in range(b_size):
                if i < a_size:
                    add_list.append(self.co_array[i] + b[i])
                else:
                    add_list.append(b[i])
            added = numpy.array(add_list)
        return added

    # Calculate a polynomial function f(x) by providing x and a co-array
    def calculate(self, x):
        sum = 0
        for i in range(self.co_array.size):
            sum += self.co_array[i]*(x**i)
        return sum

    # Calculate a function's derivative from a co-array
    def derivative(self, derivative_order = 1):
        derivative_poly = Polynomial(derivative_order)
        for i in range(self.co_array.size - 1):
            derivative_poly[i] = self.co_array[i+1]*(i+1)
        if derivative_order > 1:
            derivative_poly.derivative(derivative_order - 1)
        else:
            return derivative_poly

