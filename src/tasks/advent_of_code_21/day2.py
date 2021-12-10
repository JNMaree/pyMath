import numpy as np

class Submarine:

    # Define a vertical position
    posVERT = None

    # Define a horizontal position
    posHORZ = None

    # PART 2: add aim variable
    aim = None

    def __init__(self) -> None:
        self.posHORZ = 0
        self.posVERT = 0
        # Part 2
        self.aim = 0

    def simulate(self, instruction):
        direction = instruction[:instruction.find(' ')]
        magnitude = int (instruction[(instruction.find(' ') + 1):])
        if direction == "forward":
            self.posHORZ += magnitude
        elif direction == "down":
            self.posVERT += magnitude
        elif direction == "up":
            self.posVERT -= magnitude
        else:
            raise TypeError("Unkown  direction instruction!")
    
    def execute(self, instruction):
        direction = instruction[:instruction.find(' ')]
        magnitude = int (instruction[(instruction.find(' ') + 1):])
        if direction == "forward":
            #self.posHORZ += magnitude
            # Part2
            self.posHORZ += magnitude
            self.posVERT += (self.aim * magnitude)
        elif direction == "down":
            #self.posVERT += magnitude
            # Part2
            self.aim += magnitude
        elif direction == "up":
            #self.posVERT -= magnitude
            # Part2
            self.aim -= magnitude
        else:
            raise TypeError("Unkown  direction instruction!")

def read_input(fname):
    with open(fname, 'r') as f:
        arr = np.array(f.read().splitlines())
    return arr

def main():
    # Read input instruction set
    relative_path = 'src/tasks/advent_of_code_21/'
    intsructionset = read_input(relative_path + 'day2_input.txt')
    #print(intsructionset)
    print("Part 1:")

    sim = Submarine()

    for i in intsructionset:
        sim.simulate(i)
    print(f"horiztontal_pos:{sim.posHORZ}, depth:{sim.posVERT}")
    print(f"horizontal_pos * depth:{sim.posHORZ * sim.posVERT}")
    
    # Part 2 -----------------------------------------------------------------
    print("Part 2:")

    # Create instance of submarine
    sub = Submarine()
    
    # Follow the instruction set provided
    for i in intsructionset:
        sub.execute(i)
    print(f"horiztontal_pos:{sub.posHORZ}, depth:{sub.posVERT}")
    print(f"horizontal_pos * depth:{sub.posHORZ * sub.posVERT}")

if __name__ == "__main__":
    main()