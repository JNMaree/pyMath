import math
import numpy

from polynomial import Polynomial
# |-----------|
# |           |
# |-----------|
#
errorTolerance = 1e-6
maxIterate = 20

# Newton's Method: An iterative method for finding roots to polynomials
# - an estimate is required to find the closest root
def Newtons_Method(polynomi, estimate = 1):
    x = estimate
    error = 1
    x_n = 0
    iTerate = 0
    while error > errorTolerance or iTerate == maxIterate:
        x_n = approximate_function(x, polynomi)
        error = abs(x - x_n)
        x = x_n
        iTerate += 1
        print("i:",iTerate, ", x=", x, ", x+=", x_n, ", error=", error)
    if iTerate < maxIterate:
        root = x_n
        return root
    else:
        print("Maximum Iterations Reached without convergence @ specified error tolerance")

# x_n+1 = x_n - f(x_n)/f'(x_n)
def approximate_function(x_n, polynomial):
    return x_n - polynomial.calculate(x_n)/polynomial.derivative.calculate(x_n)

# find all real roots of a polynomial over interval [a, b]
def find_roots_over_interval(polynomi, a=-1, b=1):
    roots = []
    estimate_interval = abs(a-b)/polynomi.degree
    for i in range(polynomi.degree - 1):
        potential_root = Newtons_Method(polynomi, a + i*estimate_interval)
        if len(roots) > 0:
            for j in roots:
                if is_approximately_equal(roots[j], potential_root):
                    roots.append(potential_root)
        else:
            roots.append(potential_root)
            
def is_approximately_equal(a, b):
    if abs(a - b) < errorTolerance:
        return True
    else:
        return False

#main function
def main():
    polynom = Polynomial([-3,8,-7,1])
    print("poly:", polynom, "\npolyder:" , polynom.derivative())
    x = 5
    fx = polynom.calculate(x)
    fpx = polynom.derivative().calculate(x)
    print("x:", x, ", f(x):", fx, ", f'(x):", fpx)
    print("Frac:", approximate_function(x, polynom))
    
    root = Newtons_Method(polynom, x)
    print("newton:%6.6f" %root)

if __name__ == "__main__":
    main()

    