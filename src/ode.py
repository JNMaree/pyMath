import numpy
from polynomial import MultivariatePolynomial

class ODE(MultivariatePolynomial):

    max_derivative_order = 1
    derivative_array = numpy.zeros((max_derivative_order, MultivariatePolynomial.unique_variables))

    def __init__(self, parameter):
        if isinstance(parameter, int):
            self.independent_variables = parameter
            self.derivative_order = 1
            self.derivative_array = numpy.zeros((self.derivative_order, parameter))
        
    