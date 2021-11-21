import numpy as np

class Queue:
    """
        First In, First Out (FIFO) Data Structure

    """

    # Define array to hold values
    __elements = np.empty(0)

    # Define an internal counter for tracking the number of elements
    __n = 0

    def __init__(self, array) -> None:
        if isinstance(array,(int)):
            self.__elements = np.array((array))
            self.__n = array
        elif isinstance(array, (list)):
            self.__elements = np.array(array)
            self.__n = len(array)
        elif isinstance(array, np.ndarray):
            self.__elements = array
            self.__n = array.size
    
    def __str__(self) -> str:
        rstr = format(self.__n) + ":[ "
        for i in range(self.__n - 1, -1, -1):
            rstr += format(self.__elements[i])
            rstr += ", "
        rstr.removesuffix(", ")
        rstr += "]"
        return rstr

    # Native Queue operations
    