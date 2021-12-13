class Graph:

    # List of lists
    caves = []
    # Index 0: start
    # Index 1: end
    #   - cave index 0: cave name
    #   - cave index 1 - n: cave paths

    routes = []

    def __init__(self, paths) -> None:
        self.caves.append(['start'])
        self.caves.append(['end'])
        for p in paths:
            st_en = p.split('-')
            self.add_cave(st_en[0], st_en[1])
            self.add_cave(st_en[1], st_en[0])

    def add_cave(self, name, path):
        cave_exists = -1 
        for c in range(len(self.caves)):
            if self.caves[c][0] == name:
                cave_exists = c
        if cave_exists >= 0:    # Add path to existing cave
            self.add_path(name, path)
        else:                   # Add new cave
            self.caves.append([name])
            self.add_path(name, path)

    def add_path(self, cave_name, path):
        cave_index = -1
        for c in range(len(self.caves)):
            if self.caves[c][0] == cave_name:
                cave_index = c
        if cave_index >= 0:
            add_path = True
            for p in self.caves[cave_index]:
                if p == path:
                    add_path = False
            if add_path:
                self.caves[cave_index].append(path)
        else:
            raise NameError(f"Add_Path failed!\ncave:{cave_name} not found!\npath:{path}")

    def __str__(self) -> str:
        sret = f"{len(self.caves)}\n"
        for c in range(len(self.caves)):
            sret += f"{c}|{self.caves[c][0]}:{self.caves[c][1:]}\n"
        return sret

    def get_paths(self, name):
        aret = []        
        for c in range(len(self.caves)):
            if self.caves[c][0] == name:
                aret = self.caves[c][1:]
        return aret

    def is_big(self, name):
        return name.isupper()

    def calc_routes(self, route=None) -> int:
        if route is not None:
            node = route[len(route) - 1]  # end of route
            print(f"calc_route:{route}, node:{node}")
            if node == 'end':
                self.routes.append(route)
                return
            
            available_paths = self.get_paths(node)
            print(f"{available_paths} available_paths for [{node}]")

            # Loop through next nodes in graph
            for p in available_paths:
                available = True
                for past in route:
                    if p == past and not self.is_big(p):
                        available = False
                if available:
                    p_route = route
                    p_route.append(p)
                    self.calc_routes(p_route)
                
        else:
            self.calc_routes(['start'])   # start all routes at node 'start'

    def get_routes(self):
        sret = f"{len(self.routes)} routes:\n"
        for r in self.routes:
            sret += format(r)
            sret += '\n'
        return sret

def main():

    routes = []

    filepath = 'src/tasks/advent_of_code_21/day12_input.txt'
    with open(filepath, 'r') as f:
        for line in f:
            routes.append(line.strip())
    #print(routes)
    #"""
    routes = ['dc-end',
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

    graph = Graph(routes)
    print(graph)

    graph.calc_routes()
    print(graph.get_routes())


if __name__ == "__main__":
    main()