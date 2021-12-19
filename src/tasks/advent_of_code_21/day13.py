import numpy as np

class Origami:

    dots = []

    x = 0   # Max X value in dots[x,y]
    y = 0   # Max Y value in dots[x,y]

    output = []
    def clear_output(self):
        self.output = np.zeros((self.x + 1, self.y + 1)) 
    def dots_to_output(self):
        self.clear_output()
        for i in range(self.dots.shape[0]):
            self.output[self.dots[i, 0], self.dots[i, 1]] = 1

    def __init__(self, coordinates) -> None:
        self.dots = np.array([i.split(',') for i in coordinates], dtype=np.uint16)
        #print(f"DOTS:\n{self.dots}")
        self.x, self.y = np.amax(self.dots, axis=0)
        #print(f"x:{self.x} y:{self.y} n:{self.dots.shape[0]}")
        self.dots_to_output()

    def __str__(self) -> str:
        visible = np.count_nonzero(self.output)
        sret = f"output_points:{visible}\n"
        for y in range(self.y + 1):
            for x in range(self.x + 1):
                if self.output[x][y] == 1:
                    sret += '#'
                else:
                    sret += ' '
            sret += '\n'
        return sret

    def fold(self, instruction):
        self.output_to_dots()       # Create array of new coordinates in output_
        self.clear_output()             # Clear output array
        
        inst = instruction.split()      # Parse instructions
        inst = inst[2].split('=')
        xory = 0
        if inst[0] == 'y':
            xory = 1
        fold = int (inst[1])
        print(f"Fold| {inst[0]}[{xory}]:{fold}")
        
        #print(f"exe fold: {xy} = {axis}")
        for i in range(self.dots.shape[0]):
            #print(f"{i}|dots[{self.dots[i,0]},{self.dots[i,1]}]")
            if self.dots[i, xory] > fold:
                if inst[0] == 'x':
                    self.output[ 2*fold - self.dots[i,0] ][ self.dots[i,1] ] = 1
                elif inst[0] == 'y':
                    self.output[ self.dots[i,0] ][ 2*fold - self.dots[i,1] ] = 1
            else:
                self.output[self.dots[i, 0], self.dots[i, 1]] = 1

    def output_to_dots(self):
        temp_dots = []
        for y in range(self.y + 1):
            for x in range(self.x + 1):
                if self.output[x][y] == 1:
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
                    coordinates.append(line.strip())
            else:
                instructions.append(line.strip())
    #print(f"coordinate_list:{coordinates}\ninstructions:{instructions}")
    
    """ Test Coordinates & Instructions
    coordinates =  ['6,10','0,14',
                    '9,10','0,3',
                    '10,4','4,11',
                    '6,0','6,12',
                    '4,1','0,13',
                    '10,12','3,4',
                    '3,0','8,4',
                    '1,10','2,14',
                    '8,10','9,0']

    instructions = ['fold along y=7',
                    'fold along x=5']
    """

    origami_grid = Origami(coordinates)
    #print(origami_grid)
    origami_grid.fold(instructions[0])
    print(origami_grid)

    # Part 2 ---------------------------------------------------------------
    
    for i in range(1, len(instructions)):
        origami_grid.fold(instructions[i])    
    print(f"{i}|{origami_grid}")
    

if __name__ == "__main__":
    main()