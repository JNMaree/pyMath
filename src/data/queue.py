import numpy as np

class Queue:
    """
        First In, First Out (FIFO) Data Structure
            - uses numpy array as a simulated queue
    """

    # Define array to hold values
    __elements = np.empty(0)

    # Define an internal counter for tracking the number of elements
    __n = 0

    # Define a maximum capacity for Queue
    MAX_CAP = 1024

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
    # Enqueue: Add item to queue
    def enqueue(self, element):
        if self.__n <= self.MAX_CAP:
            self.__elements = np.append(self.__elements, element)
            self.__n += 1
        else:
            print("Overflow error: Queue at MAX_CAP")

    # Dequeue: Remove item from queue
    def dequeue(self) -> __elements.dtype:
        if self.__n > 0:
            rt = self.__elements[0]
            self.__elements = np.delete(self.__elements, 0)
            self.__n -= 1
            return rt
        else:
            print("Underflow error: Queue empty")
            return None

    # Front: View (peek) first item in Queue
    def front(self) -> __elements.dtype:
        return self.__elements[0]               # Start of Array
    
    # Rear: View (peek) last item in Queue
    def rear(self) -> __elements.dtype:
        return self.__elements[self.__n - 1]    # End of Array

    def isEmpty(self) -> bool:
        return self.__n == 0

    def isFull(self) -> bool:
        return self.__n >= self.MAX_CAP

def main():
    # Test Queue methods
    qarr = np.arange(0, 16)
    q = Queue(qarr)

if __name__ == "__main__":
    main()