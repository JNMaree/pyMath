import time
from datetime import timedelta

class sieve:

    def __init__(self, max):
        self.max = max
        self.pcount = 0
        self.primes = list(range(max/2))

        for i in range(1, max, 2):
            self.primes.append(i)

    def run(self):
        pass        


if __name__ == "__main__":
    start_time = time.monotonic()
    
    end_time = time.monotonic()
    print( timedelta(seconds=end_time - start_time))