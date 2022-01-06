class CircleBoard:
    def __init__(self, start_positions) -> None:
        self.players = []
        for p in range(len(start_positions)):
            if start_positions[p][-1] == 0:
                self.players.append(10)
            else:
                self.players.append(int(start_positions[p][-1]))
            print(f'{p}|{self.players[p]}')

def main():
    
    positions = []

    relative_path = 'src/tasks/advent_of_code_21/day21_input.txt'
    with open(relative_path, 'r') as f:
         for line in f:
             positions.append(line.strip())
    #print(f'positions:{positions}')

    #""" Test Case
    positions = ['Player 1 starting position: 4',
                'Player 2 starting position: 8']
    # """

    cboard = CircleBoard(positions)

if __name__ == '__main__':
    main()