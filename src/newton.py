import math
import numpy

from polynomial import *
# |-----------|
# |           |
# |-----------|
#
errorTolerance = 1e-6
maxIterate = 20

StefanBoltzmann = 5.670374419e-8

def NewtonMethod(arrCoefficients, estimate = 1):
    x = estimate
    derCoefficients = derive_Polynomial(arrCoefficients)
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

def funcFraction(x, functionCoeff, functionPrimeCoeff):
    return x - calculate_Polynomial(functionCoeff, x)/calculate_Polynomial(functionPrimeCoeff, x)

#main function
def main():
    polynom = numpy.array([-3,8,-7,1])
    polyder = derive_Polynomial(polynom)
    print("poly:", polynom, "\npolyder:" , polyder)
    x = 5
    fx = calculate_Polynomial(polynom, x)
    fpx = calculate_Polynomial(polyder, x)
    print("x:", x, ", f(x):", fx, ", f'(x):", fpx)
    print("Frac:", funcFraction(x, polynom, polyder))
    
    root = NewtonMethod(polynom, x)
    print("newton:%6.6f" %root)

if __name__ == "__main__":
    main()

    