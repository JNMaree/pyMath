import numpy as np
from numpy.lib.index_tricks import index_exp
from base.hash import division_knuth

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
    def hash_index(self, key, n):
        return division_knuth(key, n)

    # Search for a value in a hash table
    def search(self, value) -> int:
        index = self.hash_index(value)
        while self.__elements[index] != value:
            index += 1
        return index

    # Insert a value to a hash table
    def insert(self, value):
        index = self.hash_index(value)
        while self.__elements[index] != None:
            index += 1
        self.__elements[index] = value

    # Delete a value from a hash table
    def delete(self, value):
        index = self.hash_index(value)
        while self.__elements[index] != value:
            index += 1
        self.__elements.pop(index)