import numpy

class Polynomial:
    '''
    Univariate (x - single variable) polynomials are treated as coefficient arrays (co-arrays).
    Coefficients are stored in ascending order of degree:
        x^3 -3x^2 + 5x + 10 equates to a co-array of [10, 5, -3,  1]
         - x powers are equivalent to array position: [0,  1,  2,  3]
         - the degree of the polynomial is therefore equivalent to the length of the coefficient array
    '''
    # highest order
    degree = 0

    # coefficient array
    co_array = numpy.zeros(degree)

    def __init__(self, parameter):
        if isinstance(parameter, int):
            self.degree = parameter
            self.co_array = numpy.zeros(parameter + 1)
        elif isinstance(parameter, numpy.ndarray):
            self.co_array = parameter
            self.degree = parameter.size - 1
        elif isinstance(parameter, (list)):
            self.co_array = numpy.array(parameter)
            self.degree = len(parameter) - 1
        else:
            raise TypeError("Incorrect Type Used as Parameter")

    # Overload the array position('[]') operator to refer to co_array
    def __getitem__(self, key):
        return self.co_array[key]

    def __setitem__(self, key, value):
        self.co_array[key] = value

    # Create 'official' string representation for a Polynomial object
    #   - Prints the function form of the polynomial:
    #       f(x) = ax^2 + bx + c
    def __repr__(self):
        sRet = ""
        for i in reversed(range(self.degree + 1)):
            # Set prefix sign(+,- or none)
            coeff = self.co_array[i]
            if i < self.degree:
                if coeff > 0:
                    sRet += f" +{coeff:.3f}"
                elif coeff < 0:
                    sRet += f" {coeff:.3f}"
            else:
                sRet += f"{coeff:.3f}"
            
            # If coefficient is displayed
            if coeff != 0:
                if i > 0:
                    sRet += "x"
                    if i > 1:
                        sRet += f"^{i}"

        return sRet

    # represent polynomial in format: ax^i + bx^(i-1) + cx^(i-2) + ...
    def __str__(self):
        sRet = f"{format(self.degree)}\n"
        sRet += format(self.co_array)
        return sRet

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

    # Evaluate a polynomial f(x) by degrees of powers
    def evaluate(self, x):
        sum = 0
        for i in range(self.co_array.size):
            sum += self.co_array[i]*(x**i)
        return sum

    # Evaluate a polynomial using Horner's method (recursive multiplication)
    def evaluate_horners(self, x, degree=0):
        calc = 0
        if degree <= self.degree:
            calc += self.co_array[degree] + x*(self.evaluate_horners(x, degree + 1))
        return calc
        
    # Calculate a function's derivative from a co-array
    #   - Uses recursion for derivative_order > 1
    def derive(self, derivative_order = 1):
        derivative_poly = Polynomial(self.degree - 1)
        for i in range(self.co_array.size - 1):
            derivative_poly[i] = self.co_array[i+1]*(i+1)
        if derivative_order > 1:
            derivative_poly = derivative_poly.derive(derivative_order - 1)
        return derivative_poly

    # Calculate the number of real roots using Sturm's theorem
    def sturms_roots(self):
        q, r = euclidean_division(self, self.derive())
        while r.degree > 1:
            pass

    # Estimate the number of positive real roots by getting the number of sign changes
    def descartes_rule_of_signs(self):
        # set first sign
        j = 0
        first_nonZero = 0
        while first_nonZero == 0 and j < self.degree:
            first_nonZero = self.co_array[j]
            j += 1

        recent_sign = False # False = Negative first sign
        if first_nonZero > 0:
            recent_sign = True # True = Positive first sign

        # count number of subsequent sign changes
        sign_changes = 0
        for i in range(self.degree):
            if self.co_array[i] != 0:
                if self.co_array[i] > 0:
                    if ~recent_sign:
                        sign_changes += 1
                        recent_sign = True
                else:
                    if recent_sign:
                        sign_changes += 1
                        recent_sign = False
        return sign_changes

class MultivariatePolynomial:

    # Define the number of unique, independent variables stored
    n_variables = 0                 # Int (>= 1)
    
    # Define an array of Polynomial objects
    polynomials = []                # python list

    def __init__(self, parameters):
        if isinstance(parameters, numpy.ndarray):
            for i in range(numpy.size(parameters, 0)):
                self.polynomials.append(Polynomial(parameters[:,i]))
                self.unique_variables += 1
            
        elif isinstance(parameters, (list)):
            for i in parameters:
                self.polynomials.append(i)
                self.unique_variables += 1
        else:
            raise TypeError

    def evaluate(self, values):
        if len(values) != self.n_variables:
            raise ArithmeticError("Missing Variable Values for MultiVariate Polynomial")
        else:
            for i in self.n_variables:
                i.evaluate()

    
 
# Given two univariate polynomials a(x) and b(x) (a,b != 0),
#  there exists another two polynomials (q, r) such that:
#       a = bq + r
#   where q = quotient and r = remainder
#   and deg(r) < deg(b)
# see https://en.wikipedia.org/wiki/Polynomial_greatest_common_divisor#Euclidean_division
def euclidean_division(polynomi_a, polynomi_b):
    q = Polynomial([0])
    r = polynomi_a
    while r.degree > polynomi_b.degree:
        s = ( r[r.degree - 1]/polynomi_b[polynomi_b.degree - 1] )*r.degree - polynomi_b.degree
        q += s
        r -= s*polynomi_b
    return q, r

def main():
    
    #testfunction
    poly1 = Polynomial(numpy.array([8, -2, 1]))
    poly2 = Polynomial(numpy.array([16, 4, 2]))

    print("Polynomial_Test:")
    print("Poly1:", poly1, ", repr:", repr(poly1))
    print("Poly2:", poly2, ", repr:", repr(poly2))

    print("Polynomial_Addition:")
    print("Poly1 + Poly2:", poly1 + poly2)
    print("Poly2 + Poly1:", poly2 + poly1)
    
    print("Polynomial_Subtraction:")
    print("Poly1 - Poly2:", poly1 - poly2)
    print("Poly2 - Poly1:", poly2 - poly1)
    
    print("Polynomial_Differentiation:")
    print("Poly1:", repr(poly1.derive()))
    print("Poly2:", repr(poly2.derive()))

    print("Polynomial_2ndDifferentiation:")
    print("Poly1:", repr(poly1.derive(2)))
    print("Poly2:", repr(poly2.derive(2)))

    x = 10
    print("Polynomial_Evaluation(Exponent_method: x=",x,"):")
    print("Poly1:", poly1.evaluate(x))
    print("Poly2:", poly2.evaluate(x))

    print("Polynomial_Evaluation(Horners_method: x=",x,"):")
    print("Poly1:", poly1.evaluate_horners(x))
    print("Poly2:", poly2.evaluate_horners(x))

    
if __name__ == "__main__":
    main()

