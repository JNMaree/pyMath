import numpy as np

class Path:
    def __init__(self, start_coords) -> None:
        if isinstance(start_coords, list):
            self.n = 1
            self.coords_list = [start_coords]
            self.risks = [0]
            self.head = start_coords
            self.prev = None
        elif isinstance(start_coords, Path):
            self.n = start_coords.n
            self.coords_list = start_coords.coords_list.copy()
            self.risks = start_coords.risks.copy()
            self.head = start_coords.head.copy()
            if start_coords.prev is not None:
                self.prev = start_coords.prev.copy()
            else:
                self.prev = None

    def add(self, coords, risk):
        self.coords_list.append(coords)
        self.risks.append(risk)
        self.prev = self.head.copy()
        self.head = coords
        self.n += 1
    def in_hist(self, coords) -> bool:
        for i in self.coords_list:
            if i[0] == coords[0] and i[1] == coords[1]:
                return True
        return False
    def sum_risk(self) -> int:
        return sum(self.risks)

    def __str__(self) -> str:
        sret = f'{self.n}\n'
        sret = '0'
        for i in range(1, len(self.coords_list)):
            if self.coords_list[i][0] > self.coords_list[i-1][0]:   # Move X
                sret += f'{self.risks[i]}'
            else:                                                   # Move Y
                lstr = len(sret.rfind('\n'))
                sret += ' '*lstr + self.risks[i]
        return sret

class Priority:
    # Define scale factors for heuristic rating
    #   - lower factors mean higher priority
    risk_scale_factor = 2
    dist_scale_factor = 1
    def __init__(self, end_coords) -> None:
        self.Q = []
        self.end = end_coords
    def __str__(self) -> str:
        sret = f'{len(self.Q)}'
        for i in self.Q:
            sret += f'{i[1]},{i[1]}:{i[3]}\n'
        return sret

    def add(self, coords, risk):
        h = risk * self.risk_scale_factor
        d = self.get_distance(coords)
        h += d * self.dist_scale_factor
        h = int(h)
        for i in range(len(self.Q)):
            if self.Q[i][2] > h:
                self.Q.insert(i, [coords[0], coords[1], h])

    def get_distance(self, coords) -> int:
        dx = self.end[0] - coords[0]
        dy = self.end[1] - coords[1]
        return abs(dx - dy)


class Risk:
    def __init__(self, risks) -> None:
        self.y = len(risks[0].strip())
        self.x = len(risks)
        self.start = [0,0]
        self.end = [self.x-1, self.y-1]
        self.priority = Priority(self.end)

        self.grid = np.empty((self.x, self.y), dtype=np.uint8)
        for x in range(self.x):
            for y in range(self.y):
                self.grid[x][y] = risks[x][y]
                self.priority.add([x, y], self.get_risk([x, y]))
        #print(self.grid)

    def get_shortest_path(self):
        pass

    # Map possible routes between start and end nodes
    #   - brute force all posssible routes
    def map_to(self, to_coords, path :Path) -> Path:
        if path.head == to_coords:
            return path

        adj = self.get_adjacent_nodes(path.head, path.prev)
        adj_paths = []
        for a in adj:
            t_path = Path(path)
            if not t_path.in_hist(a):
                t_path.add(a, self.get_risk(a))
                t_path = self.map_to(to_coords, t_path)
                if t_path is not None:
                    adj_paths.append(t_path)
                
        if adj_paths:
            path_risks = []
            print(f'adj_paths:{adj_paths}', end=' ')
            for ap in adj_paths:
                path_risks.append(ap.sum_risk())
            print(f'path_risks:{path_risks}')
            return adj_paths[path_risks.index(min(path_risks))]
        else:
            return None

    # Return risk level for given coordinates
    def get_risk(self, coords) -> np.uint8:
        return self.grid[coords[0], coords[1]]

    # Return adjacent node coordinates to path, except previous node if specified
    def get_adjacent_nodes(self, coords, prev_coords=None) -> list:
        x_adj = [-1, 1]
        y_adj = [-1, 1]

        if prev_coords is not None:
            if prev_coords[0] == coords[0]:     # If X of prev and current is equal
                y_diff = prev_coords[1] - coords[1]
                y_adj.remove(y_diff)
            elif prev_coords[1] == coords[1]:   # If Y of prev and current is equal
                x_diff = prev_coords[0] - coords[0]
                x_adj.remove(x_diff)
        
        if coords[0] == 0:              # If X on boundary
            if -1 in x_adj: x_adj.remove(-1)
        elif coords[0] == (self.x - 1):
            if 1 in x_adj: x_adj.remove(1)

        if coords[1] == 0:              # If Y on boundary
            if -1 in y_adj: y_adj.remove(-1)
        elif coords[1] == (self.y - 1):
            if 1 in y_adj: y_adj.remove(1)

        adj = []
        for xa in x_adj:    # Adjacent in X directions
            adj.append([coords[0] + xa,coords[1]])
        for ya in y_adj:    # Adjacent in Y directions
            adj.append([coords[0], coords[1] + ya])

        print(f'AdjNodes for {prev_coords} -> {coords}: {adj}')
        return adj
    
        

def main():

    risks = []

    relative_path = 'src/tasks/advent_of_code_21/day9_input.txt'
    with open(relative_path, 'r') as f:
        for line in f:
            risks.append(line.strip())
    #print(risks)
    #"""
    risks = ['1163751742',
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
    least_risky_path = risk.get_shortest_path()
    print(least_risky_path)



if __name__ == '__main__':
    main()