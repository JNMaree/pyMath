
class Probe:
    def __init__(self, specstr) -> None:
        self.x_min = 0
        self.x_range = 0
        self.y_min = 0
        self.y_range = 0
        self.parse_target(specstr)
        
        self.velocity = 0
        self.trajectory = 0

    def parse_target(self, tstr: str) -> list:
        eq = tstr.find('=')
        dt = tstr.find('.', eq)
        xr1 = int (tstr[(eq + 1):dt])
        xr2 = int (tstr[(dt + 2):(tstr.find(',', eq))])

        eq = tstr.find('=', eq + 1)
        dt = tstr.find('.', eq)
        yr1 = int(tstr[(eq + 1):dt])
        yr2 = int(tstr[(dt + 2):])
        #print(f'x[{xr1},{xr2}], y[{yr1},{yr2}]')

        self.x_min = xr1
        self.x_range = xr2 - xr1

        self.y_min = yr1
        self.y_range = yr2 - yr1
        

def main():
    
    targets = ''

    relative_path = 'src/tasks/advent_of_code_21/day17_input.txt'
    with open(relative_path, 'r') as f:
        targets = f.readline().strip()
    #print(f'target:{targets}')

    probe = Probe(targets)
    


if __name__ == '__main__':
    main()