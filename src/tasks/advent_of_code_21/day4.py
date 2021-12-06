import numpy as np

class BingoBoard:

    array = []

    size = 5

    check = True

    def __init__(self, boardtext) -> None:
        self.array = np.zeros((self.size,self.size,2))
        board = boardtext.split()
        bct = 0
        #print(f"board:{board}")
        for i in range(self.size):
            for j in range(self.size):
                self.array[i][j][0] = int(board[bct])
                bct += 1

    def __str__(self) -> str:
        sret = ""
        for i in range(self.size):
            for j in range(self.size):
                sret += f"{int (self.array[i][j][0]) :2}|{int (self.array[i][j][1]) :1} "
            sret += '\n'
        return sret

    def is_bingo(self) -> bool:
        for i in range(self.size):
            for j in range(self.size):
                if self.array[i][j][1] == 1:
                    row_match_count = 0
                    col_match_count = 0
                    for x in range(self.size):
                        if self.array[x][j][1] == 1:
                            row_match_count += 1
                    for y in range(self.size):
                        if self.array[i][y][1] == 1:
                            col_match_count += 1
                    if row_match_count == 5 or col_match_count == 5:
                        self.check = False
                        return True
        return False
    
    def draw_number(self, number):
        for i in range(self.size):
            for j in range(self.size):
                if self.array[i][j][0] == number:
                    self.array[i][j][1] = 1
                    return

    def sum_unmarked(self) -> int:
        unmarked = 0
        for i in range(self.size):
            for j in range(self.size):
                if self.array[i][j][1] == 0:
                    unmarked += self.array[i][j][0]
        return unmarked

def main():

    # Part 1 ----------------------------------------------------------
    draw_list = []
    board_list = []
    
    # Read file input
    relative_path = 'src/tasks/advent_of_code_21/day4_input.txt'
    with open(relative_path, 'r') as f:
        draw_list = f.readline().strip()
        draw_list = draw_list.split(',')
        line = f.readline()
        line = f.readline()
        board = ''
        ct = 0
        while line:
            if line != "\n":
                board += line.strip() + " "
            else:
                board_list.append(BingoBoard(board))
                board = ''
            line = f.readline()
            ct += 1
    print(f"{len(draw_list)} draws:{draw_list}")        

    # Work through draw list checking for win conditions
    win_number = 0
    unmarked_sum = 0
    win_board = None 
    win_condition = False
    for i in range(len(draw_list)):
        #print(f"draw[{i}]:{draw_list[i]}")
        for b in board_list:
            b.draw_number(int (draw_list[i]))
            if b.is_bingo():
                win_number = int (draw_list[i])
                unmarked_sum = b.sum_unmarked()
                win_board = b 
                win_condition = True
                break
        if win_condition:
            break
    
    # Calculate score of first winning bingo board
    score = unmarked_sum * win_number
    print(f"winning board:\n{win_board}")
    print(f"unmarked_sum:{int (unmarked_sum)}")
    print(f"winning_number:{int (win_number)}")
    print(f"score:{int (score)}")

    # Part 2 ----------------------------------------------------------
    print("\nPart2:")

    number_of_boards = len(board_list)
    win_count = 0
    draw = 0
    while win_count < (number_of_boards) and draw < len(draw_list):
        #print(f"draw[{i}]:{draw_list[i]}")
        for b in board_list:
            if b.check: # If board not yet complete
                b.draw_number(int (draw_list[draw]))
                if b.is_bingo():
                    win_number = int (draw_list[draw])
                    unmarked_sum = b.sum_unmarked()
                    win_board = b 
                    win_count += 1
        draw += 1
    
    score = unmarked_sum * win_number
    print(f"winning board:\n{win_board}")
    print(f"unmarked_sum:{int (unmarked_sum)}")
    print(f"winning_number:{int (win_number)}")
    print(f"score:{int (score)}")
    

if __name__ == "__main__":
    main()
