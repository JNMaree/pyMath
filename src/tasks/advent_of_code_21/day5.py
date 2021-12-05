import numpy as np
from numpy.lib.index_tricks import nd_grid

class LineGrid:

    lines = []

    n_lines = 0

    grid = []

    n_grid = 1000

    def __init__(self, line_list) -> None:
        self.n_lines = len(line_list)
        self.lines = np.zeros((self.n_lines, 2, 2), dtype=np.int16)
        for i in range(self.n_lines):
            coords = line_list[i].strip().split(' -> ')
            p1 = coords[0].split(',')
            self.lines[i][0][0] = int(p1[0]) #x1
            self.lines[i][1][0] = int(p1[1]) #y1
            p2 = coords[1].split(',')
            self.lines[i][0][1] = int(p2[0]) #x2
            self.lines[i][1][1] = int(p2[1]) #y2
            #print(f"{i}|{self.lines[i]}")

    def is_horizontal(self, pos):
        return self.lines[pos][0][0] == self.lines[pos][0][1]
    def is_vertical(self, pos):
        return self.lines[pos][1][0] == self.lines[pos][1][1]

    def generate_orthogonal_grid(self):
        self.grid = np.zeros((self.n_grid,self.n_grid))
        for i in range(self.n_lines):
            if self.is_horizontal(i) or self.is_vertical(i):
                x_range = abs(self.lines[i][0][0] - self.lines[i][0][1])
                y_range = abs(self.lines[i][1][0] - self.lines[i][1][1])
                if x_range > 1: # If horizontal line    
                    x_s = self.lines[i][0][0]
                    if self.lines[i][0][0] > self.lines[i][0][1]:
                        x_s = self.lines[i][0][1]
                    y = self.lines[i][1][0]
                    for x in range(x_range + 1):
                        self.grid[x_s + x][y] += 1
                else:           # If vertical line
                    y_s = self.lines[i][1][0]
                    if self.lines[i][1][0] > self.lines[i][1][1]:
                        y_s = self.lines[i][1][1]
                    x = self.lines[i][0][0]
                    for y in range(y_range + 1):
                        self.grid[x][y_s + y] += 1

    def count_line_overlaps(self) -> int:
        ct = 0
        for x in range(self.n_grid):
            for y in range(self.n_grid):
                if self.grid[x][y] > 1:
                    ct += 1
        return ct

    def clear_grid(self):
        self.grid = np.zeros((self.n_grid, self.n_grid))

    def generate_diagonal_grid(self):
        for i in range(self.n_lines):
            if not self.is_horizontal(i) and not self.is_vertical(i):
                x_start = self.lines[i][0][0]
                x_range = x_start - self.lines[i][0][1]
                y_start = self.lines[i][1][0]
                y_range = y_start - self.lines[i][1][1]

                ct = 0
                x_inc = 1
                y_inc = 1
                if x_range > 0:
                    x_inc = -1
                if y_range > 0:
                    y_inc = -1
                drange = abs(x_range) + 1
                while ct < drange:
                    self.grid[x_start + ct*x_inc][y_start + ct*y_inc] += 1
                    ct += 1
                
        
def main():

    line_list = []

    relative_path = 'src/tasks/advent_of_code_21/day5_input.txt'
    with open(relative_path, 'r') as f:
        line_list = f.readlines()

    # Create LineGrid instance    
    line_grid = LineGrid(line_list)

    # Generate orthogonal (horizontal and vertical only) LineGrid
    line_grid.generate_orthogonal_grid()
    overlaps = line_grid.count_line_overlaps()
    print(f"orthogonal_line_overlaps:{overlaps}")

    # Part 2 ---------------------------------------------------------------
    
    # Generate diagonal LineGrid over orthogonal LineGrid
    line_grid.generate_diagonal_grid()
    overlaps = line_grid.count_line_overlaps()
    print(f"full_line_overlaps:{overlaps}")

if __name__ == "__main__":
    main()