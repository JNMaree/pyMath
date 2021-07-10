from polynomial import Polynomial
import numpy

error_tolerance = 1e-3
max_iterations = 30

def secant_method(polynomi, x0_estimate, x1_estimate):
    i = 0
    diff = 1
    x0 = x0_estimate
    x1 = x1_estimate
    while i < max_iterations and diff > error_tolerance:
        x2 = x1 - polynomi.calculate(x1)*(x1 - x0)/(polynomi.calculate(x1) - polynomi.calculate(x0))
        diff = x2 - x1
        x0 = x1
        x1 = x2
    return x1
    
def is_approximately_equal(a, b):
    if abs(a - b) < error_tolerance:
        return True
    else:
        return False