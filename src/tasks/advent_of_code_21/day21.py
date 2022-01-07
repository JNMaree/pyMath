class DeterministicDice:
    def __init__(self) -> None:
        self.n = 0
        self.out = 0

    def roll(self) -> int:
        self.n += 1
        self.out += 1
        if self.out > 100:
            self.out = 1
        return self.out

    def sum_roll_n(self, n) -> int:
        iret = 0
        for i in range(n):
            iret += self.roll()
        return iret

class CircleBoard:
    
    board_size = 10
    win_score = 1000
    player_rolls = 3
    
    def __init__(self, start_positions) -> None:
        self.players = []
        self.players_scores = []
        self.n_players = 0
        for p in range(len(start_positions)):
            if start_positions[p][-1] == 0:
                self.players.append(10)
            else:
                self.players.append(int(start_positions[p][-1]))
            self.players_scores.append(0)
            self.n_players += 1
            #print(f'{p}|{self.players[p]}')
        self.dice = DeterministicDice()

    def __str__(self) -> str:
        sret = ''
        for i in range(self.n_players):
            sret += f'{i + 1}: {self.players[i]} score:{self.players_scores[i]}\n'
        return sret

    def win_player(self) -> int:
        for i in range(self.n_players):
            if self.players_scores[i] >= self.win_score:
                return i
        return -1

    def play(self):
        win_condition = False
        while not win_condition:
            for p in range(self.n_players):
                self.advance_player(p, self.dice.sum_roll_n(self.player_rolls))
                self.players_scores[p] += self.players[p]
            if self.win_player() > 0:
                win_condition = True

    def advance_player(self, pindex, count):
        advance = int (self.players[pindex] + (count % 10)) % 10
        if advance == 0:
            advance = 10
        self.players[pindex] = advance

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

    cboard.play()

    print(f'play complete!\n{cboard}\n{cboard.dice.n} dice rolls!')
    second_place = sorted(cboard.players_scores)[0]
    print(f'solution: {second_place} * {cboard.dice.n} = {second_place * cboard.dice.n}')

if __name__ == '__main__':
    main()