
class Cave:

    name = ''

    big = False

    paths = []
    n_paths = 0

    def __init__(self, name, paths=None) -> None:
        self.name = name
        if name.isupper() and name.isalpha():
            self.big = True
        if paths is not None:
            self.add_paths(paths) 
        
    def add_paths(self, pl):
        if isinstance(pl, Cave):
            for p in pl.paths:
                if not self.path_exists(p):
                    self.paths.append(p)
                    self.n_paths += 1
        elif isinstance(pl, list):
            for p in pl:
                if not self.path_exists(p):
                    self.paths.append(p)
                    self.n_paths += 1
        elif isinstance(pl, str):
            if not self.path_exists(pl):
                self.paths.append(pl)
                self.n_paths += 1

    def path_exists(self, pstr):
        for p in self.paths:
            if pstr == p or p == self.name:
                return True
        return False

    def __str__(self) -> str:
        sret = self.name
        if self.big:
            sret += "::"
        else:
            sret += ":"
        sret += format(self.paths)
        return sret

class Graph:

    caves = []
    
    n_caves = 0

    def __init__(self, paths) -> None:
        for p in paths:
            st_en = p.split('-')
            self.add_cave( Cave(st_en[0], [ st_en[1] ]) )
            self.add_cave( Cave(st_en[1], [ st_en[0] ]) )

    def add_cave(self, addcave):
        cave_exists = -1 
        for c in range(len(self.caves)):
            if self.caves[c].name == addcave.name:
                cave_exists = c
        if cave_exists >= 0:    # Add path to existing cave
            self.caves[c].add_paths(addcave)
        else:                   # Add new cave
            self.caves.append(addcave)
            self.n_caves += 1

    def __str__(self) -> str:
        sret = f"{self.n_caves}\n"
        for c in range(self.n_caves):
            sret += f"{c}|{self.caves[c]}\n"
        return sret

    def calc_n_paths(self) -> int:
        pass


def main():

    routes = []

    filepath = 'src/tasks/advent_of_code_21/day12_input.txt'
    with open(filepath, 'r') as f:
        for line in f:
            routes.append(line.strip())
    #print(routes)

    graph = Graph(routes)
    print(graph)

if __name__ == "__main__":
    main()