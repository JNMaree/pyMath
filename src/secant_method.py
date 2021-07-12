from polynomial import Polynomial
import numpy

error_tolerance = 1e-6
max_iterations = 30

def secant_method(polynomi, x0_estimate, x1_estimate, iterations = max_iterations):
    i = 0
    diff = 1
    x0 = x0_estimate
    x1 = x1_estimate
    while i < iterations and diff > error_tolerance:
        x2 = x1 - polynomi.calculate(x1) * (x1 - x0) / (polynomi.calculate(x1) - polynomi.calculate(x0))
        x0 = x1
        x1 = x2
        diff = abs(x1 - x0)
        # print("iteration:", i, ", diff:", diff)
        i += 1
    return x1
    
def is_approximately_equal(a, b):
    if abs(a - b) < error_tolerance:
        return True
    else:
        return False

def main():
    #test
    polynom = Polynomial([-612, 0, 1])
    root = secant_method(polynom, 10, 30, 5)
    print("ROot:", root)

if __name__ == "__main__":
    main()