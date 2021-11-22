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

    # Define Front value
    front = None

    # Define Rear value
    rear = None

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
            # Set new Rear to newly added last element
            self.rear = self.__elements[self.__n - 1]
        else:
            print("Overflow error: Queue at MAX_CAP")

    # Dequeue: Remove item from queue
    def dequeue(self) -> __elements.dtype:
        if self.__n > 0:
            rt = self.__elements[0]
            self.__elements = np.delete(self.__elements, 0)
            self.__n -= 1
            if self.__n > 0:
                # Set new Front to first element
                self.front = self.__elements[0]
            else:
                self.front = None
            return rt
        else:
            print("Underflow error: Queue empty")
            return None

    def isEmpty(self) -> bool:
        return self.__n == 0

    def isFull(self) -> bool:
        return self.__n >= self.MAX_CAP

def main():
    # Stack test functions
    qarr = np.arange(2,10)
    print(f"Qarr:{qarr}")
    q = Queue(qarr)
    print(f"Q:{q}")

    # Test Push functions
    i1 = 12
    i2 = 16
    i3 = 20
    print(f"enQ: i1:{i1}, i2:{i2}, i3:{i3}")
    
    q.enqueue(i1)
    q.enqueue(i2)
    q.enqueue(i3)
    print(f"Q:{q}")

    # Test Pop functions
    countPop = 5 
    print(f"deQ: {countPop} elements:")
    for i in range(countPop):
        print(f"deQ:{q.dequeue()},", end=" ")
    print(f"\nQ:{q}")

    print("deQ: till empty")
    while not q.isEmpty():
        print(f"{q.dequeue()}, Q:{q}")

if __name__ == "__main__":
    main()