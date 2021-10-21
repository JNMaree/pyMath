import numpy as np

class TowersOfHanoi:
    # Define the number of disk levels
    n = 0

    # Set Default value as bigger than biggest n value
    #   - for comparison purposes; ie:
    #       if disk < zero then ovailable to move there
    zero = n + 1

    # Define the 2D array to hold the disk arrangement
    towers = []

    # Overwrite std class functions
    def __init__(self, n) -> None:
        self.n = n
        self.zero = n + 1
        self.towers = np.ones((n, 3), dtype=np.int16)
        self.towers *= self.zero
        self.towers[:,0] = np.arange(1, n + 1)
    def __str__(self):
        rstr = "-----------------\n"
        for i in range(self.n):
            for t in range(3):
                d = (int) (self.towers[i,t])
                if d != self.zero:
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
        while ind < self.n:
            rint = self.towers[ind, tower]
            if rint != self.zero:
                return rint
            else:
                ind += 1
        return self.zero
    
    # Return the top disk of each tower
    def top_row(self):
        rarr = np.zeros(3)
        for t in range(3):
            rarr[t] = self.top(t)
        return rarr
    
    # Return the tower of the smalled value(1) in top row
    def top_min(self):
        top_row = self.top_row()
        tmin = self.zero
        tm = 0 
        for t in range(top_row.size):
            if top_row[t] < tmin:
                tmin = top_row[t]
                tm = t
        return tm

    # Return the tower of the mid value in the top row
    def top_mid(self):
        top_row = self.top_row()
        tmin = self.top_min()
        tmid = self.zero
        tm = 0
        for t in range(top_row.size):
            if t != tmin:
                if tmid > top_row[t]:
                    tmid = top_row[t]
                    tm = t
        #print(f"top_mid(): top_row:{top_row}, tmin:{tmin}, tMID:{tm}")
        return tm

    # Return the number of disks in tower
    def get_stack_size(self, tower):
        ind = 0
        while ind < self.n:
            if self.towers[ind, tower] != self.zero:
                return self.n - ind
            ind += 1
        return 0

    # Move the top disk from fr_Tower >>>to>>> to_Tower
    def move(self, tFr, tTo):
        print(f"MOVE| tFR:{tFr}, tTo:{tTo}")
        # Get Top diskspace indices from specified towers
        iFr, iTo = -1, -1
        # Set starting indices
        #   - Search top-down for first non-zero value index
        #   - Search bottom-up for first zero value index
        indTop = 0
        indBot = self.n - 1
        while iFr < 0 or iTo < 0:
            if self.towers[indTop, tFr] != self.zero and iFr < 0:
                iFr = indTop
            else:
                #print(f"Tower[{indTop},{tFr}]:{self.towers[indTop, tFr]}, iFr:{iFr}")
                indTop += 1
            if self.towers[indBot, tTo] == self.zero and iTo < 0:
                iTo = indBot
            else:
                #print(f"Tower[{indBot},{tTo}]:{self.towers[indBot, tTo]}, iTo:{iTo}")
                indBot -= 1
        # Swap values at indices
        # print(f"tFrom:{tFr}|iFrom:{iFr}\t tTo:{tTo}|iTo:{iTo}")
        self.towers[iFr, tFr], self.towers[iTo, tTo] = self.towers[iTo, tTo], self.towers[iFr, tFr]
        print(self.__str__()) # TEST: Print layout post-Move

    # Define a function to shift the smallest disk (1) right by NP places
    #   - NP = 1 if n is even
    #   - NP = 2 if n is odd
    def shift_smallest_right(self):
        NP = 0
        if self.n % 2 == 0:
            NP = 1
        else:
            NP = 2
        
        t1 = self.top_min()
        pos_to = NP + t1
        if pos_to > 2:
            pos_to -= 3
        self.move(t1, pos_to)
    
    # Define a function to shift the middle disk (1 < mid < max) right to the
    # first available space
    def shift_middle_right(self):
        tm = self.top_mid()
        t1 = self.top_min()
        pos_to = 3 - tm - t1
        #print(f"tm:{tm}, t1:{t1}, pos_to:{pos_to}")
        self.move(tm, pos_to)

    # Solve the puzzle iteratively
    def solve_iterative(self):
        loops = (int) (self.minimum_moves()/2)
        for i in range(loops):
            self.shift_smallest_right()
            self.shift_middle_right()
        self.shift_smallest_right()
        #print(self)
    
    # Solve the puzzle recursively
    def solve_recursive(self):
        c = 0
        while self.top(0) == self.zero and self.top(1) == self.zero:
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

def main():
    # Test function
    t3 = TowersOfHanoi(3)
    print(t3)
    t3.solve_iterative()

    #t5 = TowersOfHanoi(5)
    #print(t5)

if __name__ == "__main__":
    main()