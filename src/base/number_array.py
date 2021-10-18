import numpy as np
from numpy import random

class NumberArray:
    
    # Define the Number array
    numArray = []

    # Define the number of array entries
    n_num = 0

    # Create std class methods
    def __init__(self, setup) -> None:
        if isinstance(setup, np.ndarray):
            self.numArray = setup
            self.n_num = setup.size
        elif isinstance(setup, int):
            self.numArray = np.arange(setup)
            self.n_num = setup
        else:
            raise TypeError("Unknown Type specified as 'setup' parameter")
    def __str__(self) -> str:
        rstr = format(self.n_num)
        rstr += self.numArray.__str__()
        return rstr

    # Define method to randomise the order of existing array entries
    def shuffle(self):
        #"""
        # Numpy Implementation
        #np.random.shuffle(self.numArray)    # Numpy function
        #"""
        # Fisher-Yates Implementation
        for i in range(self.n_num - 1):
            endint = self.n_num-1-i
            randint = random.randint(0, endint)
            # Swap
            self.numArray[endint], self.numArray[randint] = self.numArray[randint], self.numArray[endint]

    # Define method to remove element from array,
    #   - index: specify index to remove element from
    #   - num: specify component data to remove
    def remove_num(self, index=None, num=None):
        if index != None:
            self.numArray = np.delete(self.numArray, index)
        else:
            self.numArray = self.numArray[~np.isin(self.numArray, num)]
        self.n_num = self.numArray.size

    def calculate_expected_sum(self):
        n = self.n_num
        return (int) ( n * (n + 1) )/2

    def calculate_actual_sum(self):
        return np.sum(self.numArray)

def main():
    # Test Functions
    t1_n = 16
    t1 = NumberArray(t1_n)
    print(t1)
    t1.shuffle()
    print(t1)

    # Test remove
    t1_rem = 7
    t1.remove_num(num=t1_rem)
    print(f"remove:{t1_rem}, new_series:{t1}") 
    print(f"expected_sum_of_series:{t1.calculate_expected_sum()}")
    print(f"actual_sum_of_series:{t1.calculate_actual_sum()}")
    print(f"difference:{t1.calculate_expected_sum() - t1.calculate_actual_sum()}")


if __name__ == "__main__":
    main()