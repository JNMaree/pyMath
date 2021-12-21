import numpy as np

class HeightMap:

    grid = []

    x = 0
    y = 0

    risk_grid = []

    basin_grid = []

    def __init__(self, strinput) -> None:
        self.x = len(strinput[0].strip())
        self.y = len(strinput)
        self.grid = np.full((self.x + 2, self.y + 2), 9, dtype=np.uint8)
        for i in range(1, self.x + 1):
            stripstr = strinput[i - 1].strip()
            for j in range(1, self.y + 1):
                self.grid[i][j] = np.uint8(stripstr[j - 1])
        print(f"X:{self.x}, Y:{self.y}, Grid:\n{self.grid}")
        self.risk_grid = np.zeros_like(self.grid)
        self.basin_grid = np.zeros_like(self.grid)

    def generate_risk_grid(self):
        for i in range(1, self.x + 1):
            for j in range(1, self.y + 1):
                if self.grid[i][j] <  self.grid[i - 1][j] and self.grid[i][j] < self.grid[i + 1][j]:
                    if self.grid[i][j] < self.grid[i][j - 1] and self.grid[i][j] < self.grid[i][j + 1]:
                        self.risk_grid[i][j] = self.grid[i][j] + 1


    def sum_risk(self):
        risk_sum = 0
        for i in range(1, self.x + 1):
            for j in range(1, self.y + 1):
                risk_sum += self.risk_grid[i][j]
        return risk_sum

    def count_adjacent_notMax(self, x, y):
        if self.grid[x][y] < 9:
            sum_adjecent = 1
            self.basin_grid[x][y] += 1
            if self.basin_grid[x - 1][y] == 0:
                sum_adjecent += self.count_adjacent_notMax(x - 1, y)
            if self.basin_grid[x + 1][y] == 0:
                sum_adjecent += self.count_adjacent_notMax(x + 1, y)
            if self.basin_grid[x][y - 1] == 0:
                sum_adjecent += self.count_adjacent_notMax(x, y - 1)
            if self.basin_grid[x][y + 1] == 0:
                sum_adjecent += self.count_adjacent_notMax(x, y + 1)
            return sum_adjecent
        else:
            return 0

    def get_basin_sizes(self):
        basins = []
        for i in range(1, self.x + 1):
            for j in range(1, self.y + 1):
                if self.risk_grid[i][j] > 0:
                    basin_size = self.count_adjacent_notMax(i, j)
                    print(f"{self.risk_grid[i][j]} risk at [{i},{j}], basin size:{basin_size}")
                    basins.append(basin_size)
        basins = sorted(basins, reverse=True)
        print(f"Basins:{basins}")
        return basins 



def main():

    heights = []

    relative_path = 'src/tasks/advent_of_code_21/day9_input.txt'
    with open(relative_path, 'r') as f:
        heights = f.readlines()

    hmap = HeightMap(heights)
    
    hmap.generate_risk_grid()
    risk_sum = hmap.sum_risk()
    print(f"Risk Sum:{risk_sum}\n")

    # Part 2 -------------------------------------------------------------
    all_basins = hmap.get_basin_sizes()
    multi_basin = 1
    n = 3
    for i in range(n):
        multi_basin *= all_basins[i]
    print(f"Product of {n} largest basins:{multi_basin}\n")


if __name__ == "__main__":
    main()
