
class Octopi:

    grid = [[]]

    nX = 0
    nY = 0

    # Define counter for number of flashes
    total_flashes = 0 

    # Define grid to store flashes for a step
    flash_grid = []
    def reset_flash_grid(self):
        self.flash_grid = [[0] * self.nX] * self.nY

    def __init__(self, gridlines) -> None:
        self.nX = len(gridlines[0])
        self.nY = len(gridlines)
        for y in range(self.nY):
            self.grid.append([])
            for x in range(self.nX):
                self.grid[y].append(int (gridlines[y][x]))
        self.reset_flash_grid()        

    def __str__(self) -> str:
        sret = f"X:{self.nX}, Y:{self.nY}\n"
        for y in range(self.nY):
            for x in range(self.nX):
                sret += f"{self.grid[y][x]} "
            sret += "\n"
        return sret

    def step(self):
        for y in range(self.nY):
            for x in range(self.nX):
                self.grid[y][x] += 1 
                if self.grid[y][x] > 9:
                    self.flash_center(y, x)
        # Post-Flash operations 
        iret = self.zero_flashed()  # Set all flashed indexes to zero
        self.reset_flash_grid()     # Reset flash tracker for next step
        return iret

    def flash_center(self, y, x): 
        self.flash_grid[y][x] = 1   # Set flash tracker to avoid flashing same index twice
        
        # Set surrounding elements depending on limit boundaries
        y_adj = [-1, 0, 1]
        if y == 0:
            y_adj.remove(-1)
        elif y == (self.nY - 1):
            y_adj.remove(1)
        
        x_adj = [-1, 0, 1]
        if x == 0:
            x_adj.remove(-1)
        elif x == (self.nX - 1):
            x_adj.remove(1)
        print(f"[{x},{y}]: x_range({x_adj}) y_range({y_adj})")

        for y_inc in y_adj:     # Loop through grid of adjacents
            for x_inc in x_adj:
                ty = y + y_inc
                tx = x + x_inc
                self.grid[ty][tx] += 1
                if self.grid[ty][tx] > 9 and self.flash_grid[ty][tx] == 0:
                    self.flash_center(ty, tx)

    # Set flashed back to zero, count the flashes
    def zero_flashed(self) -> int:
        iret = 0
        for y in range(self.nY):
            for x in range(self.nX):
                if self.grid[y][x] > 9:
                    self.grid[y][x] = 0
                    iret += 1
        self.total_flashes += iret
        return iret

def main():
    
    gridlines = []

    path = "src/tasks/advent_of_code_21/day11_input.txt"
    with open(path, 'r') as f:
        for line in f:
            gridlines.append(line.strip())
    #print(f"gridlines:\n{gridlines}")

    #"""
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
    test = ['11111',
            '19991',
            '19191',
            '19991',
            '11111']
    octopi = Octopi(test) 
    #"""
    
    #octopi = Octopi(gridlines)
    print(octopi) 
    
    max_steps = 2
    for i in range(max_steps):
        iflash = octopi.step()
        print(f"{i}| flashes:{iflash}, total_flashes:{octopi.total_flashes}\n{octopi}")
    

if __name__ == "__main__":
    main()