class Cave:
    def __init__(self, name, paths=None):
        self.name = name.strip()
        self.big = name.isupper()
        self.paths = []
        if paths is not None:
            if isinstance(paths, list):
                for i in paths:
                    self.add_path(i)
            elif isinstance(paths, str):
                self.add_path(paths)
            else:
                raise TypeError(f"Unknown Path Type:{paths}")

    def __str__(self) -> str:
        sret = f"{self.name}"
        if self.big:
            sret += "::"
        else:
            sret += ":"
        sret += f"{self.paths}"
        return sret

    def add_path(self, path_str):
        if isinstance(path_str, str):
            if path_str == self.name:
                return
            for i in self.paths:
                if i == path_str:
                    return
            self.paths.append(path_str)
        elif isinstance(path_str, list):
            for p in path_str:
                exist = False
                for i in self.paths:
                    if p == i or p == self.name:
                        exist = True
                if not exist:
                    self.paths.append(p)

class Route:
    def __init__(self, cave_names) -> None:
        self.hist = []
        if isinstance(cave_names, str):
            self.hist.append(cave_names)
            self.head = cave_names
            self.n = 1
        elif isinstance(cave_names, Route):
            self.hist = cave_names.hist.copy()
            self.head = cave_names.head
            self.n = cave_names.n
        #print(f"CreateRoute:{self.hist} h:{self.head}")

    def __str__(self) -> str:
        hist_size = len(self.hist)
        sret = f'{hist_size}:'
        for i in range(hist_size):
            if i == hist_size - 1:
                sret += f' _{self.hist[i]}'
            else:
                sret += f" {self.hist[i]},"
        return sret

    def in_hist(self, cave_name) -> bool:
        for i in self.hist:
            if i == cave_name:
                return True
        return False
    
    def add(self, cave_name):
        self.hist.append(cave_name)
        self.head = cave_name
        self.n += 1 
    
    def count_in_hist(self, cave_name) -> int:
        ct = 0
        for i in self.hist:
            if i == cave_name:
                ct += 1
        print(f"[{cave_name}] in {self.hist} ct:{ct}")
        return ct

    def get_first_small(self) -> str:
        for i in self.hist:
            if i.islower() and i != 'start':
                s = i
                return s

class Graph:
    def __init__(self, path_list):
        self.caves = []
        self.add_cave(Cave('start'))    # Reserve i=0 for 'start' cave
        self.add_cave(Cave('end'))      # Reserve i=1 for 'end' cave
        for i in path_list:
            pair = i.split('-')
            p1 = Cave(pair[0], pair[1])
            p2 = Cave(pair[1], pair[0])
            self.add_cave(p1)
            self.add_cave(p2)
        self.routes = []

    def __str__(self) -> str:
        sret = f"{len(self.caves)}\n"
        for i in range(len(self.caves)):
            sret += f"{i}|{self.caves[i]}\n"
        return sret

    def add_cave(self, cave):
        for i in self.caves:
            if i.name == cave.name:
                i.add_path(cave.paths)
                return
        self.caves.append(cave)

    def get_routes(self) -> str:
        sret = f"{len(self.routes)}\n"
        for i in range(len(self.routes)):
            sret += f"{i}| {self.routes[i]}\n"
        return sret

    def get_paths(self, cave_name) -> list:
        for i in self.caves:
            if i.name == cave_name:
                tarr = i.paths.copy()
                #print(f"PathsFor[{i.name}]:{tarr}")
                return tarr

    def calc_all_routes(self, route=None):
        if route is not None:
            if route.head == 'end':
                #print(f"AddRoute: {route}")
                self.routes.append(route)
                return
            available_paths = self.get_paths(route.head)

            # Trim available paths
            if 'start' in available_paths: 
                available_paths.remove('start')
            rems = []
            for p in available_paths:
                if p.islower() and route.in_hist(p):
                    #print(f"remove:{p} from {available_paths}")
                    rems.append(p)
            for r in rems:
                available_paths.remove(r)
            #print(f"{route} -> available:{available_paths}")

            # Subsequent paths
            for a in available_paths: 
                troute = Route(route)
                troute.add(a)
                self.calc_all_routes(troute)
        else:
            start_route = Route('start')
            self.calc_all_routes(start_route)

    # Part 2 - Account for a single double visit to a small cave
    def calc_routes_with_first_small(self, route=None):
        if route is not None:
            if route.head == 'end':
                #print(f"AddRoute: {route}")
                self.routes.append(route)
                return
            available_paths = self.get_paths(route.head)

            # Trim available paths
            if 'start' in available_paths: 
                available_paths.remove('start')
            rems = []
            for p in available_paths:
                if p.islower() and route.in_hist(p):
                    #print(f"remove:{p} from {available_paths}")
                    fs = route.get_first_small()
                    if p == fs:
                        if route.count_in_hist(fs) > 1:
                            rems.append(p)
                    else:
                        rems.append(p)
            for r in rems:
                available_paths.remove(r)
            #print(f"{route} -> available:{available_paths}")

            # Subsequent paths
            for a in available_paths: 
                troute = Route(route)
                troute.add(a)
                self.calc_routes_with_first_small(troute)
        else:
            start_route = Route('start')
            self.calc_routes_with_first_small(start_route) 

def main():

    paths = []
    filepath = 'src/tasks/advent_of_code_21/day12_input.txt'
    with open(filepath, 'r') as f:
        for line in f:
            paths.append(line.strip())
    #print(paths)
    #"""
    paths = ['dc-end',
            'HN-start',
            'start-kj',
            'dc-start',
            'dc-HN',
            'LN-dc',
            'HN-end',
            'kj-sa',
            'kj-HN',
            'kj-dc']
    """
    paths = ['fs-end',
            'he-DX',
            'pj-DX',
            'fs-he',
            'start-DX',
            'end-zg',
            'zg-sl',
            'zg-pj',
            'pj-he',
            'RW-he',
            'fs-DX',
            'pj-RW',
            'zg-RW',
            'start-pj',
            'he-WI',
            'zg-he',
            'pj-fs',
            'start-RW']
    """
    
    # Graph instance creation
    #graph = Graph(paths)
    #print(graph)
    # Calculate and print routes
    #graph.calc_all_routes()   # Calculate possible routes
    #print(graph.get_routes())

    # Part 2 ----------------------------------------------------
    
    graph_small = Graph(paths)
    print(graph_small)
    graph_small.calc_routes_with_first_small()
    print(graph_small.get_routes())


if __name__ == "__main__":
    main()