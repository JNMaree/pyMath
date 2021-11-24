import numpy as np

class HashTable:
    """
        Associative Array Data Structure
            - uses numpy arrays to store data
    """

    # Define a dictionary to hold key-value pairs
    __elements = {}

    # Define an internal counter for the number of elements
    __n = 0

    # Define a table capacity 
    #   - power of 2 recommended
    TABLE_CAP = 64

    # Knuth constant
    #   - applies when TABLE_CAP is a power of 2
    random_real_A = 0.5 * (np.sqrt(5) - 1)

    def __init__(self, array) -> None:
        if isinstance(array, (list)):
            self.__elements = np.empty(self.TABLE_CAP)
            self.__elements[:] = np.NaN
            for i in range(len(array)):
                self.insert(array[i])
                self.__n += 1
        elif isinstance(array, np.ndarray):
            self.__elements = np.empty(self.TABLE_CAP)
            self.__elements[:] = np.NaN
            for i in range(array.size):
                self.insert(array[i])
                self.__n += 1
    
    # STR representation method
    def __str__(self) -> str:
        srt = format(self.__n) + "["
        for i in self.__elements:
            if not np.isnan(i):
                srt += f"{i}, "
        srt.removesuffix(", ")
        srt += "]"
        return srt
    
    # Hashing function
    def get_index(self, key) -> int:
        # Simple Hashing function
        #   - using Knuth constant on the multiplication method
        s = key * self.random_real_A
        s = s - np.fix(s)   # Get fraction part of s
        s = int(self.TABLE_CAP * s)  # Get whole part of s as index
        print(f"get_index(key:{key}) -> i:{s}")
        return s

    # Search for a value in a hash table
    #   - return index of value
    def search(self, value) -> int:
        index = self.get_index(value)
        while index < self.TABLE_CAP - 1 and self.__elements[index] != value:
            index += 1
        return index

    # Insert a value to a hash table
    def insert(self, value):
        index = self.get_index(value)
        while index < self.TABLE_CAP - 1 and not np.isnan(self.__elements[index]):
            index += 1
        self.__elements[index] = value

    # Delete a value from a hash table
    def delete(self, value):
        index = self.get_index(value)
        while index < self.TABLE_CAP - 1 and self.__elements[index] != value:
            index += 1
        self.__elements = np.delete(self.__elements, index)

def main():
    # Test Hash_Table
    tarr = np.arange(1, 25)
    ht = HashTable(tarr)
    print("tarr:", tarr)
    print(ht)

if __name__ == "__main__":
    main()