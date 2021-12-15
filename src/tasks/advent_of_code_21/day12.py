from os import name


class Cave:
    def __init__(self, name, paths=None):
        self.name = name
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
        sret += f" {self.paths}"
        return sret

    def add_path(self, path_str):
        if isinstance(path_str, str):
            for i in self.paths:
                if i == path_str:
                    return
            self.paths.append(path_str)
        elif isinstance(path_str, list):
            for p in path_str:
                exist = False
                for i in self.paths:
                    if i == p:
                        exist = True
                if not exist:
                    self.paths.append(p)

class Route:
    def __init__(self, cave) -> None:
        self.hist = []
        self.hist.append(cave)
        self.head = cave

    def in_hist(self, cave) -> bool:
        for i in self.hist:
            if cave == i:
                return True
        return False
    
    def add(self, cave):
        self.hist.append(cave)
        self.head = cave

class Graph:

    caves = []
    routes = []

    def __init__(self, path_list):
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
        for i in self.caves:
            sret += f"{i.name}: {i.paths}\n"
        return sret

    def add_cave(self, cave):
        for i in self.caves:
            if i.name == cave.name:
                i.add_path(cave.paths)
                return
        self.caves.append(cave)

    def get_routes(self) -> str:
        sret = f"{len(self.routes)}\n"
        for i in self.routes:
            sret += f"{i}\n"
        return sret

    def get_paths(self, cave_name) -> list:
        for i in self.caves:
            if i.name == cave_name:
                return i.paths

    def is_small(self, cave_name) -> bool:
        for c in self.caves:
            if c.name == cave_name:
                return not c.big

    def calc_all_routes(self, route=None):
        if route:

            available_paths = self.get_paths(route.head)
            try:
                available_paths.remove('start')
                for p in route:
                    if self.is_small(p):
                        available_paths.remove(p)
            except ValueError:
                pass

            for a in available_paths:
                temp_route = route
                temp_route.add(a)
                if a == 'end':
                    self.routes.append(temp_route)
                else: 
                    self.calc_all_routes(temp_route)
        else:
            self.calc_all_routes(Route('start'))



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
    #"""
    # Graph instance creation
    graph = Graph(paths)
    print(graph)
    
    # Calculate and print routes
    graph.calc_all_routes()   # Calculate possible routes
    print(graph.get_routes())


if __name__ == "__main__":
    main()