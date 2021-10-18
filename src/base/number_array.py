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

    # Define method to randomise existing array entries
    def shuffle(self):
        np.random.shuffle(self.numArray)

    # Define method to remove element from array,
    #   - index: specify index to remove element from
    #   - num: specify component data to remove
    def remove_num(self, index=None, num=None):
        if index != None:
            self.numArray = np.delete(self.numArray, index)
        else:
            self.numArray = self.numArray[~np.isin(self.numArray, num)]

    

def main():
    # Test Functions
    t1_n = 10
    t1 = NumberArray(t1_n)
    print(t1)
    t1.shuffle()
    print(t1)


if __name__ == "__main__":
    main()