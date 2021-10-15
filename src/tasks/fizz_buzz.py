# Define object to contain methods
class FizzBuzz:

    # Define the int to start counting at
    start = 1

    # Define the max number to count to
    maxi = 0

    # Define the multiples and the corresponding descriptor terms
    mNum = [3,5]
    mName = ["Fizz", "Buzz"]

    # Define the array that will hold the designation
    array = []

    def __init__(self, max_int, start = 1) -> None:
        self.start = start
        self.maxi = max_int
        self.init_with_max()
 
    # Generate sequence up to and including maxi
    def init_with_max(self, max_i=0):
        if max_i != 0 :
            self.maxi = max_i
        tmp_array = []
        
        for i in range(self.start, self.maxi + 1):
            tmp_str = ""
            for m in range(len(self.mNum)):
                if i % self.mNum[m] == 0:
                    tmp_str += self.mName[m]
            if tmp_str == "":
                tmp_str += format(i)
            tmp_array.append(tmp_str)
            #print(f"{i}|:{self.array[i-self.start]}")
        self.array = tmp_array

    # Generate class STR for printout
    def __str__(self):
        ret_str = f"FizzBuzz({self.maxi}):"
        for i in self.array:
            ret_str += i + ", "
        return ret_str

    def add_multiple_designation(self, multiple, designation):
        self.mNum.append(multiple)
        self.mName.append(format(designation))


def main():

    # Test FizzBuzz Class Init
    x1 = 42
    x2 = 15

    # Calculate sequence & Print Output to terminal
    print("TEST_1:")
    F1 = FizzBuzz(x1)
    print(F1)
    
    print("TEST_2:")
    F2 = FizzBuzz(x2)
    print(F2)

    # Add "Fuzz" as a designator for a multiple of 7
    F1.add_multiple_designation(7, "Fuzz")
    F1.init_with_max(105)
    print(F1)



if __name__ == "__main__":
    main()