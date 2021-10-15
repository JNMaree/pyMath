# Define object to contain methods
class FizzBuzz:

    # Define the int to start counting at
    start = 1

    # Define the max number to count to
    maxi = 0

    # Define the array that will hold the designation
    array = []

    def __init__(self, max_int, start = 1) -> None:
        self.start = start
        self.maxi = max_int
        self.init_with_max()
 
    # Generate sequence up to and including maxi
    def init_with_max(self):
        tmp = []
        for i in range(self.start, self.maxi + 1):
            if i % 3 == 0:
                if i % 5 == 0:
                    tmp.append("FizzBuzz")
                else:
                    tmp.append("Fizz")
            elif i % 5 == 0:
                tmp.append("Buzz")
            else:
                tmp.append(format(i))
            #print(f"{i}|:{self.array[i-self.start]}")
        self.array = tmp

    # Generate class STR for printout
    def __str__(self):
        ret_str = f"FizzBuzz({self.maxi}):"
        for i in self.array:
            ret_str += i + ", "
        return ret_str


def main():

    # Test FizzBuzz Class Init
    x1 = 42
    x2 = 15

    # Calculate sequence & Print Output to terminal
    print("TEST_1:")
    print(FizzBuzz(x1))
    
    print("TEST_2:")
    print(FizzBuzz(x2))


if __name__ == "__main__":
    main()