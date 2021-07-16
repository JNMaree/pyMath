import numpy

class ODE:

    independent_variables = 0
    derivative_order = 1
    derivative_array = numpy.zeros((derivative_order, independent_variables))

    def __init__(self, parameter):
        if isinstance(parameter, int):
            self.independent_variables = parameter
            self.derivative_order = 1
            self.derivative_array = numpy.zeros((self.derivative_order, parameter))
        
        