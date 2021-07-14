import numpy
from Polynomial import Polynomial

class TimePolynomial(Polynomial):

    
    

def runge_kutta_method():
    

def step(time_poly, y_n, t_n, h):
    k_1 = time_poly.calculate(y_n, t_n)
    k_2 = time_poly.calculate(y_n + h*k_1/2, t_n + h/2)
    k_3 = time_poly.calculate(y_n + h*k_2/2, t_n + h/2)
    k_4 = time_poly.calculate(y_n + h*k_3, t_n + h)

    y_m = y_n + (1/6) * h * (k_1 + 2*k_2 + 2*k_3 + k_4)
    t_m = t_n + h
    return y_m, t_m

def main():
    #test function
    pass

if __name__ == "__main__":
    main()