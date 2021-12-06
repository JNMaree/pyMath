#import numpy as np
import time

class FishArray:

    fish = []

    n = 0

    capc = 0

    def __init__(self, array) -> None:
        self.n = len(array) 
        self.capc = 2*self.n
        self.fish = [0]*self.capc
        self.fish[:self.n] = array

    def __str__(self) -> str:
        sret = format(self.n)
        sret += format(self.fish)
        return sret

    def elapse_day(self):
        new_fish = 0
        for i in range(self.n):
            if self.fish[i] > 0:
                self.fish[i] -= 1
            else:
                self.fish[i] = 6
                new_fish += 1 
        additions = [8] * new_fish 
        new_n = self.n + new_fish
        if new_n > self.capc:
            self.capc *= 2
            new_array = [0]*self.capc 
            new_array[:self.n] = self.fish[:self.n]
            new_array[self.n:new_n] = additions
            self.fish = new_array
            self.n = new_n
        else:
            self.fish[self.n:new_n] = additions
            self.n = new_n

def main():

    fish = []
    
    relative_path = 'src/tasks/advent_of_code_21/day6_input.txt'
    with open(relative_path, 'r') as f:
        fish = [int(x) for x in f.readline().split(',')]
    
    lanternFish = FishArray(fish)

    # Setup timing functions
    t0 = time.perf_counter()

    days = 80
    for d in range(days):
        lanternFish.elapse_day()
        print(f"day {d}| {lanternFish.n}")
    print(f"After {days} days, there are {lanternFish.n} fish.")

    # Part 2 --------------------------------------------------------
    """
    days2 = 256
    for d in range(days + 1, days2 + 1):
        lanternFish.elapse_day()
        print(f"day {d}| {lanternFish}")
    print(f"After {days} days, there are {lanternFish.n} fish.")   
    """

    # Calculate performance by time elapsed
    t1 = time.perf_counter()
    tot = t1 - t0
    print(f"Total Time Elapsed:{tot}")

if __name__ == "__main__":
    main()