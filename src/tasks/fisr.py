import math

def InverseSqrt(x):
    """
    Quake Function: Fast Inverse Square Root (FISR) approximation
        - Approximates the inverse root of a float using Newton's method:
            
                x_(n+1) = x_n - f(x_n)/f'(x_n)

        - where the function f(x_n) is = 1/(x_n)^2 - y
    """
    x_d2 = 0.5 * x                  # Half of X
    
    i = x                           # Convert x to integer
    
    i = 0x5F3759DF - (i >> 1)       # Set initial guess

    x_n = float (i)                   # Convert back to float
    
    x_n = x_n * (1.5 - x_d2*x_n*x_n)        # Calculate Newton's Method once       
    return x_n

def main():
    
    x = [1, 3, 11, 101, 4761, 10000]
    n = len(x)

    # Precise Calculation Solutions
    x_def = [0]*n
    for i in range(n):      # Calculate standard definite solution
        x_def[i] = 1/math.sqrt(x[i])

    # Approximation Solutions
    x_inv = [0]*n
    for i in range(n):      # Calculate Inverse Square root using FISR
        x_inv[i] = InverseSqrt(x[i])

    # Comparison of Precise and Approximate Solutions
    x_comp = [0]*n
    for i in range(n):      # Compare the difference between the two methods
        x_comp[i] = abs(x_def[i] - x_inv[i])

    # Printout results
    print("x\tisqrt(x)_calculated\tisqrt(x)_approximated\tisqrt_difference")
    for i in range(n):
        print(f"{ x[i] }", end="\t")
        print(f" { x_def[i] :.9f}", end="\t\t")
        print(f" { x_inv[i] :.6e}", end="\t\t")
        print(f" { x_comp[i] :.6e}")

if __name__ == "__main__":
    main()