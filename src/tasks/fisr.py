import math
import numpy as np

def FastInverseSqrt(x):
    """
    Quake III Function: Fast Inverse Square Root (FISR) approximation
        - Approximates the inverse root of a float using Newton's method:
            
                x_(n+1) = x_n - f(x_n)/f'(x_n)

        - where the function f(x_n) is = 1/(x_n)^2 - y
    """
    x_d2 = 0.5 * x                          # Half of x
    
    i = np.float32(x)                       # Convert x to integer
    i = i.view(np.int32)

    j = np.int32(0x5f3759df - (i >> 1))     # Set initial guess
    x_n = j.view(np.float32)                # Convert back to float

    x_n = x_n * (1.5 - (x_d2 * x_n * x_n))  # One run of Newton's Method 
    return x_n

def main():
    
    x = [1, 3, 11, 256, 4761, 10000]
    n = len(x)

    # Precise Calculation Solutions
    x_def = [0]*n
    for i in range(n):      # Calculate standard definite solution
        x_def[i] = 1/math.sqrt(x[i])

    # Approximation Solutions
    x_inv = [0]*n
    for i in range(n):      # Calculate Inverse Square root using FISR
        x_inv[i] = FastInverseSqrt(x[i])

    # Comparison of Precise and Approximate Solutions
    x_compare = [0]*n
    for i in range(n):      # Compare the difference between the two methods
        x_compare[i] = abs(x_def[i] - x_inv[i])

    # Printout results
    print("x\tisqrt(x)_calculated\tisqrt(x)_approximated\tisqrt_difference")
    for i in range(n):
        print(f"{ x[i] }", end="\t")
        print(f" { x_def[i] :.9f}", end="\t\t")
        print(f" { x_inv[i] :.6e}", end="\t\t")
        print(f" { x_compare[i] :.6e}")

if __name__ == "__main__":
    main()