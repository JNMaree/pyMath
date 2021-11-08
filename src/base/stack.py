import numpy as np

class Stack:
    """
        Last In, First Out (LIFO) Data Structure
    """

    # Define array to hold values
    __elements = []

    def __init__(self, array):
        if isinstance(array,(int)):
            self.__elements = np.array((array))
        elif isinstance(array, (list)):
            self.__elements = np.array(array)
        elif isinstance(array, np.ndarray):
            self.__elements = array
    def __str__(self) -> str:
        rstr = ""
        for i in range(self.__elements.size, -1, -1):
            rstr += format(self.__elements[i])
        return rstr
        
    # Push:
    #   - add element to stack
    def push(self, value):
        np.append(self.__elements, value)

    # Pop:
    #   - remove and return last element from stack
    def pop(self) -> __elements.dtype:
        rt = self.__elements[self.__elements.size - 1]
        self.__elements = np.delete(self.__elements, self.__elements.size - 1)
        return rt

    # Check whether or not stack is empty
    def empty(self) -> bool:
        if self.__elements.size == 0:
            return True
        else:
            return False