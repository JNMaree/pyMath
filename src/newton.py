import math
import numpy

# |-----------|
# |           |
# |-----------|
#
errorTolerance = 1e-6
maxIterate = 20

StefanBoltzmann = 5.670374419e-8

def NewtonMethod(arrCoefficients, estimate = 1):
    x = estimate
    derCoefficients = derivePolynomial(arrCoefficients)
    error = 1
    x_ = 0
    iTerate = 0
    while error > errorTolerance or iTerate == maxIterate:
        x_ = funcFraction(x, arrCoefficients, derCoefficients)
        error = abs(x - x_)
        x = x_
        iTerate += 1
        print("i:",iTerate, ", x=", x, ", x+=", x_, ", error=", error)
    if iTerate < maxIterate:
        root = x_
        return root
    else:
        print("Maximum Iterations Reached without convergence @ specified error tolerance")

def calculatePolynomial(arrCoefficients, x):
    sum = 0
    for i in range(arrCoefficients.size):
        sum += arrCoefficients[i]*(x**i)
    return sum

def derivePolynomial(arrCoefficients, degree = 1):
    deriv = numpy.empty(arrCoefficients.size - 1)
    for i in range(deriv.size):
        deriv[i] = arrCoefficients[i+1]*(i+1)
    return deriv

def funcFraction(x, functionCoeff, functionPrimeCoeff):
    return x - calculatePolynomial(functionCoeff, x)/calculatePolynomial(functionPrimeCoeff, x)

#main function
def main():
    polynom = numpy.array([-3,8,-7,1])
    polyder = derivePolynomial(polynom)
    print("poly:", polynom, "\npolyder:" , polyder)
    x = 5
    fx = calculatePolynomial(polynom, x)
    fpx = calculatePolynomial(polyder, x)
    print("x:", x, ", f(x):", fx, ", f'(x):", fpx)
    print("Frac:", funcFraction(x, polynom, polyder))
    
    root = NewtonMethod(polynom, x)
    print("newton:%6.6f" %root)

if __name__ == "__main__":
    main()

    