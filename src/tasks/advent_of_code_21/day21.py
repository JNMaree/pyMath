class DeterministicDice:
    def __init__(self) -> None:
        self.n = 0

    def roll(self) -> int:
        self.n += 1
        return self.n

class CircleBoard:
    
    board_size = 10
    win_score = 1000
    
    def __init__(self, start_positions) -> None:
        self.players = []
        self.players_scores = []
        self.n = 0
        for p in range(len(start_positions)):
            if start_positions[p][-1] == 0:
                self.players.append(10)
            else:
                self.players.append(int(start_positions[p][-1]))
            self.players_scores.append(0)
            self.n += 1
            print(f'{p}|{self.players[p]}')
    
    def win_condition(self) -> int:
        for i in range(self.n):
            if self.players_scores[i] >= 1000:
                return i
        return -1

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