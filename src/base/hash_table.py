import numpy as np

class HashTable:
    """
        Associative Array Data Structure
            - uses native python dictionaries to store key-value pairs
    """

    # Define a dictionary to hold key-value pairs
    __elements = {}

    # Define an internal counter for the number of elements
    __n = 0

    def __init__(self, array) -> None:
        if isinstance(array, (int)):
            self.__elements = dict(None * array) # Create an empty dict of spec size
        elif isinstance(array, (list)):
            for i in range(len(array)):
                self.__elements.update({i, array[i]})
                self.__n += 1
        elif isinstance(array, np.ndarray):
            for i in range(array.size):
                self.__elements.update({i, array[i]})
                self.__n += 1
    
    # STR representation method
    def __str__(self) -> str:
        srt = format(self.__n)
        for i in self.__elements:
            srt += i + "\n"
        return srt
    
    # Hashing function
    def hash(self, key):     
        h = 0
        return h

    def search(self, value):
        pass
    def insert(self):
        pass
    def delete(self):
        pass