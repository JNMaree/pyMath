import numpy

class Polynomial:
    '''
    Homogenous, single-variable (x) polynomials are treated as coefficient arrays (co-arrays).
    Coefficients are stored in ascending order of degree:
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

    # Overload the array position('[]') operator to refer to co_array
    def __getitem__(self, key):
        return self.co_array[key]

    def __setitem__(self, key, value):
        self.co_array[key] = value

    # Create 'official' string representation for a Polynomial object 
    def __repr__(self):
        return 'Polynomial({})'.format(self.co_array)

    # represent polynomial in format: ax^i + bx^(i-1) + cx^(i-2) + ...
    def __str__(self):
        ret = ""
        for i in range(self.degree):
            if i > 0 and i < self.degree:
                if self.co_array[i] > 0: 
                    ret += " +"
                else:
                    ret += " "
            if i > 0:
                ret += str(self.co_array[i])
                ret += "x"
                if i > 1:
                    ret += "^"
                    ret += str(i)
            else:
                ret += str(self.co_array[i])
        return ret

    # overload the addition('+') arithmetic operator
    def __add__(self, other):
        a_size = self.degree
        b_size = other.degree
        added = []
        add_list = []

        # equal degree equations
        if a_size == b_size:        
            for i in range(a_size):
                add_list.append(self.co_array[i] + other[i])
            added = numpy.array(add_list)
        # self degree > other degree
        elif a_size > b_size:
            for i in range(a_size):
                if i < b_size:
                    add_list.append(self.co_array[i] + other[i])
                else:
                    add_list.append(self.co_array[i])
            added = numpy.array(add_list)
        # other degree > self degree
        else:
            for i in range(b_size):
                if i < a_size:
                    add_list.append(self.co_array[i] + other[i])
                else:
                    add_list.append(other[i])
            added = numpy.array(add_list)
        return added

    # overload the subtraction('-') arithmetic operator
    def __sub__(self, other):
        #self - other
        a_size = self.degree
        b_size = other.degree
        added = []
        add_list = []

        # equal degree equations
        if a_size == b_size:        
            for i in range(a_size):
                add_list.append(self.co_array[i] - other[i])
            added = numpy.array(add_list)
        # self > other degree
        elif a_size > b_size:
            for i in range(a_size):
                if i < b_size:
                    add_list.append(self.co_array[i] - other[i])
                else:
                    add_list.append(self.co_array[i])
            added = numpy.array(add_list)
        # other degree > self degree
        else:
            for i in range(b_size):
                if i < a_size:
                    add_list.append(self.co_array[i] - other[i])
                else:
                    add_list.append(other[i])
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
        derivative_poly = Polynomial(self.degree - 1)
        for i in range(self.co_array.size - 1):
            derivative_poly[i] = self.co_array[i+1]*(i+1)
        if derivative_order > 1:
            derivative_poly = derivative_poly.derivative(derivative_order - 1)
        return derivative_poly


def main():
    #testfunction
    poly1 = Polynomial(numpy.array([8, -2, 1]))
    poly2 = Polynomial(numpy.array([16, 4, 2]))

    print("Polynomial_Test:")
    print("Poly1:", poly1, ", degree:", poly1.degree)
    print("Poly2:", poly2, ", degree:", poly2.degree)

    print("Polynomial_Addition:")
    print("Poly1 + Poly2:", poly1 + poly2)
    print("Poly2 + Poly1:", poly2 + poly1)
    
    print("Polynomial_Subtraction:")
    print("Poly1 - Poly2:", poly1 - poly2)
    print("Poly2 - Poly1:", poly2 - poly1)
    
    print("Polynomial_Differentiation:")
    print("Poly1:", poly1.derivative())
    print("Poly2:", poly2.derivative())

    print("Polynomial_2ndDifferentiation:")
    print("Poly1:", poly1.derivative(2))
    print("Poly2:", poly2.derivative(2))

    
    
if __name__ == "__main__":
    main()

