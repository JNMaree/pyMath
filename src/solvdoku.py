import numpy as np


class digit:
    def __init__(self, value=0):
        #set digit value (1-9)
        self.val = value
        
        #set potential values
        if value > 0:
            self.pot = np.array([value])
        else:
            self.pot = np.array([1,2,3,4,5,6,7,8,9])
        
        self.potToTrim = True
    
    def setVal(self):
        #Set val if potentials dropped to 1
        if len(self.pot) == 1 and self.val == 0:
            self.val = self.pot[0]
            return True
        else:
            return False


class grid:
    def __init__(self, puzzle):
        self.solved = 0
        self.grid = np.full((9,9), digit())
        for i, x in enumerate(puzzle):
            for j, y in enumerate(x):
                d = digit(puzzle[i][j])
                if d.val > 0:
                    self.solved = self.solved + 1
                    self.grid[i][j] = d


    def printout(self):
        for i, x in enumerate(self.grid):
            for j, y in enumerate(x):
                if j == 3 or j == 6:
                    print('| ', end = '')
                if y == 0:
                    print('-', 'red', end = " ")
                else:
                    print(y.val, end = " ")
            if i == 2 or i == 5:
                print()
                print("------+-------+-------")
            else:
                print()
        print()

    def getBlocID(self, row, col):
        #-Blocs:
        # 1 2 3
        # 4 5 6
        # 7 8 9
        #------
        b = 1
        if col < 6 and col > 2:
            b = 2
        else:
            b = 3
        if row < 3:
            return b
        elif row < 6:
            return b + 3
        else:
            return b + 6

    def getBlocRC(self, blocID):
        #Set Rows
        if blocID < 4:
            row = [0,1,2]
        elif blocID < 7:
            row = [3,4,5]
        else:
            row = [6,7,8]
        #Set Columns
        if blocID == 1 or blocID == 4 or blocID == 7:
            col = [0,1,2]
        elif blocID == 2 or blocID == 5 or blocID == 8:
            col = [3,4,5]
        else:
            col = [6,7,8]
        #Return the local row and columns
        return np.array(row, col)

    def trimPotentials(self, row, col, bloc):
        #loop through grid, removing potential values based around provided indices
        for i, x in enumerate(self.grid):
            for j, y in enumerate(x):
                if self.getBlocID(i,j) == bloc:
                    if self.grid[row][col].val in self.grid[i][j].pot:
                        np.delete(self.grid[i][j].pot, np.where(self.grid[row][col].val))
                if i == row and j != col:
                    if self.grid[row][col].val in self.grid[i][j].pot:
                        np.delete(self.grid[i][j].pot, np.where(self.grid[row][col].val))
                if j == col and i != row:
                    if self.grid[row][col].val in self.grid[i][j].pot:
                        np.delete(self.grid[i][j].pot, np.where(self.grid[row][col].val))

        #Set False to not trim pots using digit again
        self.grid[row][col].potTrim = False


    def setPotentials(self):
        for i, x in enumerate(self.grid):
            for j, y in enumerate(x):
                if self.grid[i][j].val > 0 and self.grid[i][j].potToTrim:
                    self.trimPotentials(i,j, self.getBlocID(i,j))
                if self.grid[i][j].setVal():
                    self.solved += 1
                    

    def setBloc(self):

        for b in range(1, 10):  #Loop through blocs 1-9
            rc = self.getBlocRC(b)
            for i, x  in enumerate(rc): #Loop through digits in bloc
                for j, y in enumerate(x):
                    pass
        

    def solve(self):
        timeout = 100
        ctr = 0
        while self.solved < 81 and ctr < timeout:
            temp = self.solved
            self.setPotentials()
            self.setBloc()


            if self.solved == temp:
                ctr += 1
            
        
        self.printout()
        if ctr < timeout:
            print("Solved:" + str(self.solved))
        else:
            print("T/O Counter:" + str(ctr))

#
#
#Execution
if __name__ == '__main__':
    print("Sepoku:", end = " ")
    print("numPy:" + np.__version__)

    puzzleTest1 = np.array([[7,4,0, 0,8,0, 0,2,0],
                            [6,0,2, 4,3,7, 5,8,9],
                            [3,5,0, 0,0,0, 7,0,0],

                            [1,9,0, 8,6,0, 4,7,0],
                            [0,6,0, 0,0,3, 9,0,0],
                            [0,0,4, 0,0,1, 0,0,8],

                            [0,3,0, 6,0,0, 0,1,0],
                            [2,0,6, 0,0,0, 3,0,4],
                            [0,0,0, 0,7,4, 2,0,5]])

    s = grid(puzzleTest1)
    s.printout()
    s.solve()


    





