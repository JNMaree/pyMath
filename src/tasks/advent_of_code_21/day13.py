import numpy as np

class Origami:

    dots = []

    x = 0
    y = 0

    output = []
    def clear_output(self):
        self.output = np.zeros((self.x + 1, self.y + 1)) 

    def __init__(self, coordinates) -> None:
        self.dots = np.array(coordinates, dtype=np.uint16)
        self.x, self.y = np.amax(self.dots, axis=0)
        self.clear_output()
        print(f"x:{self.x} y:{self.y} n:{self.dots.shape[0]}")

    def __str__(self) -> str:
        pass

    def printout(self) -> str:
        sret = f"output_points:{self.count_visible()}"
        for x in range(self.x + 1):
            for y in range(self.y + 1):
                if self.output[x][y] == 1:
                    sret += '#'
                else:
                    sret += ' '
            sret += '\n'
        return sret

    def execute(self, instruction):
        self.output_to_dots()       # Create array of new coordinates in output_
        self.clear_output()             # Clear output array
        
        inst = instruction.split()      # Parse instructions
        inst = inst[2].split('=')
        axis = 0                  # fold axis = x
        if inst[0] == 'y':      
            axis = 1              # fold axis = y
        fold = int (inst[1])
        
        #print(f"exe fold: {xy} = {axis}")
        for i in range(self.n):
            if self.dots[i, axis] > fold:
                if axis == 0:
                    self.output[ 2*fold - self.dots[i, 0], self.dots[i, 1]] = 1
                elif axis == 1:
                    self.output[ fold - self.dots[i, 0], 2*fold - self.dots[i, 1]] = 1
            else:
                self.output[self.dots[i, 0], self.dots[i, 1]] = 1

    def count_visible(self):
        return np.count_nonzero(self.output)

    def output_to_dots(self):
        temp_dots = []
        for x in range(self.x):
            for y in range(self.y):
                if self.output[x,y] == 1:
                    temp_dots.append([x, y])
        # Set new tracking properties
        self.dots = np.array(temp_dots, dtype=np.uint16)
        self.x, self.y = np.amax(self.dots, axis=0)


def main():
    
    coordinates = []
    instructions = []
    line_break = False

    filepath = 'src/tasks/advent_of_code_21/day13_input.txt'
    with open(filepath, 'r') as f:
        for line in f:
            if not line_break:
                if line == "\n":
                    line_break = True
                else:
                    coordinates.append(line.strip().split(','))
            else:
                instructions.append(line.strip())
    #print(f"coordinate_list:{coordinates}\ninstructions:{instructions}")

    origami_grid = Origami(coordinates)

    origami_grid.execute(instructions[0])
    print(f"visible_points:{origami_grid.count_visible()}")

    # Part 2 ---------------------------------------------------------------
    """
    for i in range(1, len(instructions)):
        origami_grid.execute(instructions[i])    
    print(f"{i}|{origami_grid.printout()}")
    """

if __name__ == "__main__":
    main()