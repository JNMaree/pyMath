import numpy as np

class TowersOfHanoi:
    # Define the number of disk levels
    n = 0

    # Define the 2D array to hold the disk arrangement
    towers = []

    # Overwrite std class functions
    def __init__(self, n) -> None:
        self.n = n
        self.towers = np.zeros((n, 3), dtype=np.int16)
        self.towers[:,0] = np.arange(1, n + 1)
    def __str__(self):
        rstr = "-----------------\n"
        for i in range(self.n):
            for t in range(3):
                d = (int) (self.towers[i,t])
                if d != 0:
                    rstr += format(d)
                else:
                    rstr += "|"
                rstr += "\t" 
            rstr += "\n"
        rstr += "-----------------\n"
        #rstr += format(self.towers)    # TEST: print tower array
        return rstr

    # Calculate the minimum number of moves to complete the puzzle
    def minimum_moves(self):
        return (2 ** self.n) - 1
    
    # Return the first non-zero value (top-down search) in a tower
    def top(self, tower):
        rint = 0
        ind = 0
        while rint == 0 or ind < self.n:
            rint = self.towers[ind, tower]
            if rint != 0:
                return rint
            else:
                ind += 1
        return rint

    # Simulate moving of a value from from_Tower to to_Tower
    def move(self, tFr, tTo):
        # Get Top diskspace indices from specified towers
        iFr, iTo = -1, -1
        # Set starting indices
        #   - Search top-down for first non-zero value index
        #   - Search bottom-up for first zero value index
        indTop = 0
        indBot = self.n - 1
        while iFr < 0 or iTo < 0:
            if self.towers[indTop, tFr] != 0 and iFr < 0:
                iFr = indTop
            else:
                #print(f"Tower[{indTop},{tFr}]:{self.towers[indTop, tFr]}, iFr:{iFr}")
                indTop += 1
            if self.towers[indBot, tTo] == 0 and iTo < 0:
                iTo = indBot
            else:
                #print(f"Tower[{indBot},{tTo}]:{self.towers[indBot, tTo]}, iTo:{iTo}")
                indBot -= 1
        # Swap values at indices
        # print(f"tFrom:{tFr}|iFrom:{iFr}\t tTo:{tTo}|iTo:{iTo}")
        self.towers[iFr, tFr], self.towers[iTo, tTo] = self.towers[iTo, tTo], self.towers[iFr, tFr]
        print(self.__str__()) # TEST: Print layout post-Move

    # Solve the puzzle iteratively
    def solve_iterative(self):
        c = 0
        while self.top(0) == 0 and self.top(1) == 0:
            if self.top(0) > self.top(2):
                self.move(0, 2)
                c += 1
            if self.top(0) > self.top(1):
                self.move(0, 1)
                c += 1
            if self.top(2) < self.top(1):
                self.move(2, 1)
                c += 1
        print(f"Solved in {c} moves!")

    # Solve the puzzle recursively
    def solve_recursive(self):
        pass
    

def main():
    # Test function
    t3 = TowersOfHanoi(3)
    print(t3)

    #t5 = TowersOfHanoi(5)
    #print(t5)

if __name__ == "__main__":
    main()