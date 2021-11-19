import numpy
from numpy.lib.polynomial import roots

from base.polynomial import Polynomial

# The error_tolerance defines the threshold at which numbers are equal:
#   |n1 - n2| < error_tolerance
ERROR_TOLERANCE = 1e-9

# Maximum number of iterations to run if solution does not converge
MAX_ITERATIONS = 50

# Occurences are counted for each estimate:
# - If convergence for a single estimate is not reached, 
#   the estimate is slightly increased and Newton's method is re-run on the new estimate
#   = This counts as an occurrence.
MAX_OCCURENCES = 10

# Newton's Method: An iterative method for finding roots to polynomials
# - an estimate is required to find the closest root
def Newtons_method(polynomi, estimate = 1, occurence=0):
    x = estimate
    error = 1
    x_n = 0
    iteratr = 0
    loop = True
    while loop:
        x_n = approximate_function(x, polynomi)
        error = abs(x - x_n)

        # Check if necessary to iterate
        if error < ERROR_TOLERANCE or iteratr == MAX_ITERATIONS:
            loop = False

        #print("i:",iTerate, ", x=", x, ", x+=", x_n, ", error=", error)
        x = x_n
        iteratr += 1
    
    if iteratr < MAX_ITERATIONS:
        return x_n  # return root
    else:
        print(f"Max_Iterations:{iteratr} reached without convergence.")
        print(f"Error_Tolerance:{ERROR_TOLERANCE:.9f}, error reached:{error:.9f}")
        occurence += 1
        if occurence < MAX_OCCURENCES:
            new_estimate = x_n - occurence*abs(x_n - estimate)
            return Newtons_method(polynomi, new_estimate, occurence)
        else:
            raise RuntimeError("Loop Iteration Ceased & Max Occurrences reached with no roots found!")

# x_n = x - f(x)/f'(x)
def approximate_function(x, polynomial):
    return x - polynomial.evaluate(x)/polynomial.derive().evaluate(x)

# Determine if the difference between numbers falls below a threshold,
# making it effectively zero
def is_equal(a, b):
    ans = abs(a - b)
    if ans < ERROR_TOLERANCE:
        return True
    else:
        return False

# Find all real roots of a polynomial over interval [a, b]
def get_roots(polynomi, n_roots=0, interval_start=-1,interval_end=1):
    if n_roots == 0:
    # if n_roots not specified
        n_estimates = polynomi.degree
    else:
        n_estimates = n_roots

    roots = numpy.zeros(n_estimates)
    if n_estimates > 1:
        estimate_interval = abs(interval_start - interval_end) / (n_estimates - 1)
    else:
        estimate_interval = abs(interval_start - interval_end)
    #print(f"estimate_interval:{estimate_interval}")

    # calculate the roots using Newton's method based on an estimate initial value
    #   - assuming equally spaced within specified interval
    for i in range(n_estimates):
        est = interval_start + i * estimate_interval
        #print(f"{i}_est:{est}")
        potential_root = Newtons_method(polynomi, est)
        for j in range(roots.size):
            if ~is_equal(j, potential_root):
                roots[i] = potential_root

    return roots


# Test function
def main():

    # Test Newton's Method for 1 iteration
    polynom = Polynomial([-3,8,-7,1]) # -3 + 8x -7x^2 + x^3
    print(f"poly:{polynom}\npoly_derive:{polynom.derive()}")
    print(f"poly__REPR__:{repr(polynom)}")

    # Test value evaluation
    x = 5
    fx = polynom.evaluate(x)
    fpx = polynom.derive().evaluate(x)
    print(f"x: {x}, f(x): {fx}, f'(x): {fpx}")
    print("Frac:", approximate_function(x, polynom))
    
    # Test Newton's Method for calculating a root based on an estimate(x)
    root = Newtons_method(polynom, x)
    print(f"newtons_method_root:{root}")
    
    # Test the application of Newton's Method for finding all roots within a given interval
    # Define a Legendre polynomial of degree 3
    legendre3 = Polynomial([0, -1.5, 0, 2.5])
    print(f"leg3_repr: {legendre3.__repr__()}")
    #print(f"leg3_derive: {legendre3.derive().__repr__()}")
    
    # Test root finding methodology
    print(f"leg3_roots:{get_roots(legendre3)}")
    print(f"leg3_numpy_roots:{numpy.roots(numpy.flip(legendre3.co_array))}")

    # Test individual estimates
    print(f"leg_est(-1):{Newtons_method(legendre3, -1)}")
    print(f"leg_est( 0):{Newtons_method(legendre3, 0)}")
    print(f"leg_est(+1):{Newtons_method(legendre3, 1)}")
    
    # Define a Legendre Polynomial of degree 4
    legendre4 = Polynomial([3/8, 0, -30/8, 0, 35/8])
    print(f"leg4: {legendre4.__repr__()}")
    #print(f"leg4_derive: {legendre4.derive().__repr__()}")

    # Test root finding method:
    print(f"leg4_roots:{get_roots(legendre4)}")
    print(f"leg4_numpy_roots:{numpy.roots(numpy.flip(legendre4.co_array))}")

    # Test individual estimates
    print(f"leg_est(  -1):{Newtons_method(legendre4, -1)}")
    print(f"leg_est(-0.3):{Newtons_method(legendre4, -0.3)}")
    print(f"leg_est(+0.3):{Newtons_method(legendre4, 0.3)}")
    print(f"leg_est(  +1):{Newtons_method(legendre4, 1)}")

if __name__ == "__main__":
    main()