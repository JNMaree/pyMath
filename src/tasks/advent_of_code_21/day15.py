import numpy as np

class Path:
    def __init__(self, start_coords) -> None:
        self.coords = start_coords
        self.risks = [0]
        self.head = None
        self.n = 1
    def add(self, coords, risk):
        self.coords.append(coords)
        self.risks.append(risk)
        self.head = coords
        self.n += 1
    def in_hist(self, coords) -> bool:
        for i in self.coords:
            if i[0] == coords[0] and i[1] == coords[1]:
                return True
        return False
    def sum_risk(self) -> int:
        return sum(self.risks)

class Risk:
    def __init__(self, risks) -> None:
        self.y = len(risks[0].strip())
        self.x = len(risks)
        self.start = [0,0]
        self.end = [self.x-1, self.y-1]
        self.grid = np.empty((self.x, self.y), dtype=np.uint8)
        for x in range(self.x):
            for y in range(self.y):
                self.grid[x][y] = risks[x][y]
        #print(self.grid)

    def map(self, path :Path = None):
        if path is None:
            pt = Path(self.start)
            self.map(pt)

        x = path.head[0]
        y = path.head[1]

        


    

def main():

    risks = []

    relative_path = 'src/tasks/advent_of_code_21/day9_input.txt'
    with open(relative_path, 'r') as f:
        for line in f:
            risks.append(line.strip())
    #print(risks)
    #"""
    risks =    ['1163751742',
                '1381373672',
                '2136511328',
                '3694931569',
                '7463417111',
                '1319128137',
                '1359912421',
                '3125421639',
                '1293138521',
                '2311944581']
    #"""
    
    risk = Risk(risks)
    


if __name__ == '__main__':
    main()