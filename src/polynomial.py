import numpy

#Calculate a polynomial function f(x) by providing x and a coefficient array
def calculate_Polynomial(arrCoefficients, x):
    sum = 0
    for i in range(arrCoefficients.size):
        sum += arrCoefficients[i]*(x**i)
    return sum

#Calculate a function's derivative from a coefficient array
def derive_Polynomial(arrCoefficients):
    deriv = numpy.empty(arrCoefficients.size - 1)
    for i in range(deriv.size):
        deriv[i] = arrCoefficients[i+1]*(i+1)
    return deriv