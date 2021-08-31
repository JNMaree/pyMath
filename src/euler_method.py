import numpy

from polynomial import Polynomial


def eulers_method(multiVarPolynom, y0, h, time_steps):
    y_n = y0
    y_m = 0

    for i in time_steps:
    	y_m = y_n + h*multiVarPolynom.calculate(y_n, i)
    return y_m

def main():
    # Test Euler's Method:
    
    pass

if __name__ == "__main__":
    # test function
    main()