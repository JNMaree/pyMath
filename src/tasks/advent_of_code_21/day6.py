import time

class FishArray:

    fish_states = []

    max_state = 9

    start_state = 6
    new_state = 8

    n = 0

    def __init__(self, array) -> None:
        self.fish_states = [0] * self.max_state
        for i in array:
            self.fish_states[i] += 1
            self.n += 1

    def __str__(self) -> str:
        sret = format(self.n)
        sret += format(self.fish_states)
        return sret

    def elapse_day(self):
        new_fish = self.fish_states[0]
        for i in range(self.max_state - 1):
            self.fish_states[i] = self.fish_states[i + 1]
        self.fish_states[self.start_state] += new_fish
        self.fish_states[self.new_state] = new_fish
        self.n += new_fish

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
        print(f"day {d}| {lanternFish}")
    print(f"After {days} days, there are {lanternFish.n} fish.")

    # Part 2 --------------------------------------------------------
    # Increase number of days to 256
    days2 = 256
    for d in range(days + 1, days2 + 1):
        lanternFish.elapse_day()
        print(f"day {d}| {lanternFish}")
    print(f"After {days2} days, there are {lanternFish.n} fish.")

    # Calculate performance by time elapsed
    t1 = time.perf_counter()
    tot = t1 - t0
    print(f"Total Time Elapsed:{tot}")

if __name__ == "__main__":
    main()