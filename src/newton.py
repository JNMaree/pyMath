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

#

def Newton_Method(polynomi, estimate = 1):
    x = estimate
    error = 1
    x_ = 0
    iTerate = 0
    while error > errorTolerance or iTerate == maxIterate:
        x_ = funcFraction(x, polynomi)
        error = abs(x - x_)
        x = x_
        iTerate += 1
        print("i:",iTerate, ", x=", x, ", x+=", x_, ", error=", error)
    if iTerate < maxIterate:
        root = x_
        return root
    else:
        print("Maximum Iterations Reached without convergence @ specified error tolerance")

# 
def funcFraction(x, polynom):
    return x - polynom.calculate(x)/polynom.derivative.calculate(x)

#main function
def main():
    polynom = numpy.array([-3,8,-7,1])
    polynomPrime = polynom.derivative(1)
    print("poly:", polynom, "\npolyder:" , polynomPrime)
    x = 5
    fx = polynom.calculate(x)
    fpx = polynomPrime.calculate(x)
    print("x:", x, ", f(x):", fx, ", f'(x):", fpx)
    print("Frac:", funcFraction(x, polynom))
    
    root = Newton_Method(polynom, x)
    print("newton:%6.6f" %root)

if __name__ == "__main__":
    main()

    