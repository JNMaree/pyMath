import numpy

from base.polynomial import Polynomial


def runge_kutta_method(multiVarPolynom, y0, h, time_steps):
    y_n = y0
    y_m = 0
    
    for i in time_steps:
    # Classic Runge-Kutta step method (RK4)
        k_1 = multiVarPolynom.calculate(y_n, i)
        k_2 = multiVarPolynom.calculate(y_n + h*k_1/2, i + h/2)
        k_3 = multiVarPolynom.calculate(y_n + h*k_2/2, i + h/2)
        k_4 = multiVarPolynom.calculate(y_n + h*k_3, i + h)

        y_m = y_n + (1/6) * h * (k_1 + 2*k_2 + 2*k_3 + k_4)
        
    return y_m


if __name__ == "__main__":
    # test function
    pass