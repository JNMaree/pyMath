import numpy as np

class Octopi:

    grid = []

    nX = 0
    nY = 0

    # Define counter for number of flashes
    total_flashes = 0 

    # Define grid to store flashes for a step
    flash_grid = []
    def reset_flash_grid(self):
        self.flash_grid = np.zeros_like(self.grid)

    def __init__(self, gridlines) -> None:
        self.nX = len(gridlines[0])
        self.nY = len(gridlines)
        self.grid = np.empty((self.nX, self.nY), dtype=np.uint8)
        for x in range(self.nX):
            for y in range(self.nY):
                self.grid[x][y] = np.uint8 (gridlines[x][y])
        self.reset_flash_grid()

    def __str__(self) -> str:
        sret = f"X:{self.nX}, Y:{self.nY}\n"
        for x in range(self.nX):
            for y in range(self.nY):
                sret += f"{self.grid[x][y]} "
            sret += "\n"
        return sret

    def step(self):
        self.grid += 1  # Increment all values by one
        for x in range(self.nX):
            for y in range(self.nY):
                if self.grid[x][y] > 9 and self.flash_grid[x][y] == 0:
                    self.flash(x, y)
        # Post-Flash operations 
        iret = self.zero_flashed()  # Set all flashed indexes to zero
        return iret

    def flash(self, x, y): 
        self.flash_grid[x][y] = 1   # Set flash tracker to avoid flashing same index twice
        
        x_adj = [-1, 0, 1]          # Set surrounding elements depending on limit boundaries
        if x == 0:
            x_adj.remove(-1)
        elif x == (self.nX - 1):
            x_adj.remove(1)
        
        y_adj = [-1, 0, 1]
        if y == 0:
            y_adj.remove(-1)
        elif y == (self.nY - 1):
            y_adj.remove(1)
        #print(f"flash[{x},{y}]: x{x_adj} y{y_adj}")

        for x_inc in x_adj:     # Loop through grid of adjacents
            for y_inc in y_adj:
                tx = x + x_inc
                ty = y + y_inc
                self.grid[tx][ty] += 1
                if self.grid[tx][ty] > 9 and self.flash_grid[tx][ty] == 0:
                    self.flash(tx, ty)

    # Set flashed back to zero, count the flashes
    def zero_flashed(self) -> int:
        iret = 0
        #print(self.flash_grid)
        for x in range(self.nX):
            for y in range(self.nY):
                if self.flash_grid[x][y] == 1: # Check if flashed
                    self.grid[x][y] = 0
                    iret += 1
        self.total_flashes += iret
        self.reset_flash_grid()     # Reset flash tracker for next step
        return iret
        

def main():
    
    gridlines = []

    path = "src/tasks/advent_of_code_21/day11_input.txt"
    with open(path, 'r') as f:
        for line in f:
            gridlines.append(line.strip())
    #print(f"gridlines:\n{gridlines}")

    """
    test = ['5483143223',
            '2745854711',
            '5264556173',
            '6141336146',
            '6357385478',
            '4167524645',
            '2176841721',
            '6882881134',
            '4846848554',
            '5283751526']
    octopi = Octopi(test) 
    """
    
    octopi = Octopi(gridlines)
    print(octopi)

    # Execute steps 
    max_steps = 100 
    for i in range(max_steps):
        iflash = octopi.step()
        print(f"{i}| flashes:{iflash}, total_flashes:{octopi.total_flashes}")

    # Part 2 ----------------------------------------------------------------

    octopuses = Octopi(gridlines)
    all_flash = False
    ct = 0
    while not all_flash:
        if octopuses.step() == (octopuses.nX * octopuses.nY):
            all_flash = True
        ct += 1
    print(f"All flash occurs at step:{ct}")

if __name__ == "__main__":
    main()