import numpy as np

class Stack:
    """
        Last In, First Out (LIFO) Data Structure
            - uses numpy array as a simulated stack
    """

    # Define array to hold values
    __elements = np.empty(0)

    # Define an internal counter for tracking elements
    __n = 0

    # Define a maximum capacity for stack
    MAX_CAP = 1024

    def __init__(self, array):
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

    # Native Stack Operations: 
    # Push:
    #   - add element to stack
    def push(self, value):
        if self.__n < self.MAX_CAP:
            self.__elements = np.append(self.__elements, value)
            self.__n += 1
        else:
            raise OverflowError("Stack MAX_CAP")

    # Pop:
    #   - remove and return last element from stack
    def pop(self) -> __elements.dtype:
        if self.__n > 0:
            rt = self.__elements[self.__n - 1]
            self.__elements = np.delete(self.__elements, self.__n - 1)
            self.__n -= 1
            return rt

    # Peek:
    #   - return last element from stack without removing it
    def peek(self) -> __elements.dtype:
        if self.__n > 0:
            return self.__elements[self.__n - 1]

    # Check whether stack is empty
    def isEmpty(self) -> bool:
        return self.__n == 0

    # Check whether stack is full
    def isFull(self) -> bool:
        return self.__n >= self.MAX_CAP

    
def main():
    # Stack test functions
    t = np.arange(2,10)
    print(f"t:{t}")
    ts = Stack(t)
    print(f"stack_t:{ts}")

    # Test Push functions
    i1 = 12
    i2 = 16
    i3 = 20
    print(f"push: i1:{i1}, i2:{i2}, i3:{i3}")
    
    ts.push(i1)
    ts.push(i2)
    ts.push(i3)
    print(f"stack_ts:{ts}")

    # Test Pop functions
    countPop = 5 
    print(f"pop: {countPop} elements:")
    for i in range(countPop):
        print(f"pop:{ts.pop()},", end=" ")
    print(f"\nstack_ts:{ts}")

    print("pop: till empty")
    while not ts.isEmpty():
        print(f"{ts.pop()}, ts:{ts}")

if __name__ == "__main__":
    main()