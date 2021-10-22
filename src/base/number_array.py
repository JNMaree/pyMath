import copy
import numpy as np
from numpy import random
from copy import deepcopy

import numpy

class NumberArray:
    
    # Define the Number array
    nums = []

    # Define the number of array entries
    n = 0

    # Create std class methods
    def __init__(self, setup) -> None:
        if isinstance(setup, np.ndarray):
            self.nums = setup
            self.n = setup.size
        elif isinstance(setup, int):
            self.nums = np.arange(setup)
            self.n = setup
        else:
            raise TypeError("Unknown Type specified as 'setup' parameter")
    def __str__(self) -> str:
        rstr = format(self.n)
        rstr += self.nums.__str__()
        return rstr

    # Define method to randomise the order of existing array entries
    def shuffle(self):
        #"""
        # Numpy Implementation
        #np.random.shuffle(self.numArray)    # Numpy function
        #"""
        # Fisher-Yates Implementation
        for i in range(self.n - 1):
            endint = self.n-1-i
            randint = random.randint(0, endint)
            # Swap
            self.nums[endint], self.nums[randint] = self.nums[randint], self.nums[endint]

    # Remove element from array,
    #   - index: specify index to remove element from
    #   - num: specify component data to remove
    def remove(self, index=None, num=None):
        if index != None:
            self.nums = np.delete(self.nums, index)
        else:
            self.nums = self.nums[~np.isin(self.nums, num)]
        self.n = self.nums.size
    
    # Add element to array
    def add(self, num):
        if isinstance(num, (list, numpy.ndarray)):
            for i in num:
                self.nums.append(i)
                self.n += 1
        else:
            self.nums = np.append(self.nums, num)
            self.n += 1

    def calculate_expected_sum(self):
        n = self.n
        return n * (n + 1)//2

    def calculate_actual_sum(self):
        return np.sum(self.nums)

    def find_missing_entity(self):
        return self.calculate_expected_sum() - self.calculate_actual_sum()

    # SORTING ALGORITHMS
    #   - implemented to favour ascending order

    # 1. Selection Sort:
    #   - find minimum element, move to start
    def sort_selection(self):
        for i in range(self.n):
            min_i = i
            for j in range(i + 1, self.n):
                if self.nums[j] < self.nums[min_i]:
                    min_i = j
            self.nums[i], self.nums[min_i] = self.nums[min_i], self.nums[i]

    # 2. Bubble Sort:
    #   - find min of 2 adjacent elements, swap if larger value precedes
    def sort_bubble(self):
        not_sorted = True
        c = 0
        swaps = 0
        while not_sorted:
            if self.nums[c] > self.nums[c + 1]:
                self.nums[c], self.nums[c + 1] = self.nums[c + 1], self.nums[c]
                swaps += 1
            c += 1
            if c == (self.n - 1):
                c = 0
                if swaps != 0:
                    swaps = 0
                else:
                    not_sorted = False

    # 3. Recursive Bubble Sort:
    #   - Same swapping practive as bubble sort, implemented recursively
    def sort_bubble_recursive(self, n=0):
        for i in range(self.n -1 -n):
            if self.nums[i] > self.nums[i + 1]:
                self.nums[i], self.nums[i + 1] = self.nums[i + 1], self.nums[i]
        if n != (self.n - 2):
            self.sort_bubble_recursive(n + 1)

    # 4. Insertion Sort:
    #   - Array is split into sorted & unsorted partitions
    #   - First term of the unsorted side is selected and
    #       placed into correct position in sorted array
    def sort_insertion(self):
        for i in range(1, self.n):
            if self.nums[i] < self.nums[i - 1]:
                j = 0
                while self.nums[i] < self.nums[i - 1 - j]:
                    j += 1
                if j >= i:
                    j = i
                for k in range(j):
                    self.nums[i - k], self.nums[i - k - 1] = self.nums[i - k - 1], self.nums[i - k]

    # 5. Recursive Insertion Sort
    #   - Same process as insertion sort, applied recursively
    def sort_insertion_recursive(self, index=1):
        j = 1
        while self.nums[index - j + 1] < self.nums[index - j]:
            self.nums[index - j + 1], self.nums[index - j] = self.nums[index - j], self.nums[index - j + 1]
            if (index - j) > 0:
                j += 1
        if index < (self.n - 1):
            self.sort_insertion_recursive(index + 1)
        else:
            return

    # 6. Merge Sort
    #   - Partition the array into 2 parts
    #   - Sort each partition independently
    #   - Merge Sorted arrays back into a single array
    def sort_merge(self, arr=nums):
        if arr.size > 1:
            split = arr.size//2
            l = self.sort_merge(self.nums[:split])
            r = self.sort_merge(self.nums[split:])

            
        else:
            return arr


    def sort_merge_iterative(self):
        pass

def main():
    # Test Functions
    t1_n = 16
    t1 = NumberArray(t1_n)
    print(t1)
    t1.shuffle()
    print(t1)

    # Test remove, add & sum methods
    t1_rem = 10
    t1.remove(num=t1_rem)
    print(f"remove:{t1_rem}, new_series:{t1}") 
    print(f"expected_sum_of_series:{t1.calculate_expected_sum()}")
    print(f"actual_sum_of_series:{t1.calculate_actual_sum()}")
    print(f"find_difference:{t1.find_missing_entity()}")
    t1.add(t1.find_missing_entity())
    print(f"add_missing_entity:{t1}")

    # Test Sorting Methods
    dashes = '-'*(t1.n * 4)
    print(dashes)
    print("Unsorted:", t1)
    print(dashes)

    t_sel = copy.deepcopy(t1)
    t_sel.sort_selection()
    print("sort_sel:", t_sel, "\n")

    t_bub = copy.deepcopy(t1)
    t_bub.sort_bubble()
    print("sort_bub:", t_bub, "\n")

    t_brc = copy.deepcopy(t1)
    t_brc.sort_bubble_recursive()
    print("sort_brc:", t_brc, "\n")

    t_ins = copy.deepcopy(t1)
    t_ins.sort_insertion()
    print("sort_ins:", t_ins, "\n")

    t_irc = copy.deepcopy(t1)
    t_irc.sort_insertion_recursive()
    print("sort_irc:", t_irc, "\n")

    t_mrg = copy.deepcopy(t1)
    t_mrg.sort_merge()
    print("sort_mrg:", t_mrg, "\n")

if __name__ == "__main__":
    main()