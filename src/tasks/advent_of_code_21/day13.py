import numpy as np

class Origami:

    dots = []

    x = 0
    y = 0
    n = 0

    output = []
    def reset_output(self):
        self.output = np.zeros((self.x + 1, self.y + 1))

    def __init__(self, coordinates) -> None:
        self.dots = np.array(coordinates, dtype=np.uint16)
        self.x, self.y = np.amax(self.dots, axis=0)
        self.n = self.dots.size//2
        self.reset_output()
        #print(f"x:{self.x} y:{self.y} n:{self.n}")

    def __str__(self) -> str:
        pass

    def output(self) -> str:
        pass

    def execute(self, instruction):
        self.reset_output()         # Clear output array
        inst = instruction.split()
        inst = inst[2].split('=')
        xy = 0
        if inst[0] == 'y':
            xy = 1
        axis = int (inst[1])
        #print(f"exe fold: {xy} = {axis}")
        for i in range(self.n):
            if self.dots[i, xy] > axis:
                self.output[self.dots[axis - i, 0], self.dots[axis - i, 1]] = 1
            else:
                self.output[self.dots[i, 0], self.dots[i, 1]] = 1

    def count_visible(self):
        return np.count_nonzero(self.output)



def main():
    
    coordinates = []
    instructions = []
    line_break= False

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

if __name__ == "__main__":
    main()