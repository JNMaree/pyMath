import math
import numpy

# |-----------|
# |           |
# |-----------|
#

StefanBoltzmann = 5.670374419e-8

def NewtonMethod(arrCoefficients):
    roots = numpy.empty(arrCoefficients.size);
    
    
    return roots

def calculatePolynomial(arrCoefficients, x):
    sum = 0
    for i in range(arrCoefficients.size):
        sum += arrCoefficients[i]*(x**i)
        print("i:%s\t%s*%s" %(i, arrCoefficients[i], x**i))
    return sum

def derivePolynomial(arrCoefficients, degree = 1):
    deriv = numpy.empty(arrCoefficients.size - 1)
    for i in range(arrCoefficients.size - 1):
        deriv[i] = arrCoefficients[i+1]*i
    
    return deriv

#main function
def main():
    pass

if __name__ == "__main__":
    main()

    