from os import X_OK


class Pair:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def magnitude(self) -> int:
        if isinstance(self.x, Pair):
            mx = self.x.magnitude
        else:
            mx = self.x
        if isinstance(self.y, Pair):
            my = self.y.magnitude
        else:
            my = self.y
        return 3*mx + 2*my

def main():
    
    numbers = []

    relative_path = 'src/tasks/advent_of_code_21/day18_input.txt'
    with open(relative_path, 'r') as f:
        for line in f:
            numbers.append(line.strip())
    print(f'{numbers}')

    


if __name__ == '__main__':
    main()