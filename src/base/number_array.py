import copy
import numpy as np
from numpy import random

class NumberArray:
    
    # Define the Number array
    ints = []

    # Define the number of array entries
    n = 0

    # Create std class methods
    def __init__(self, setup) -> None:
        if isinstance(setup, np.ndarray):
            self.ints = setup
            self.n = setup.size
        elif isinstance(setup, list):
            self.ints = np.array(setup)
            self.n = len(setup)
        elif isinstance(setup, int):
            self.ints = np.arange(setup)
            self.n = setup
        else:
            raise TypeError("Unknown Type specified as 'setup' parameter")
    def __str__(self) -> str:
        rstr = format(self.n)
        rstr += self.ints.__str__()
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
            self.ints[endint], self.ints[randint] = self.ints[randint], self.ints[endint]

    # Remove element from array,
    #   - index: specify index to remove element from
    #   - num: specify component data to remove
    def remove(self, index=None, num=None):
        if index != None:
            self.ints = np.delete(self.ints, index)
        else:
            self.ints = self.ints[~np.isin(self.ints, num)]
        self.n = self.ints.size
    
    # Add element to array
    def add(self, num):
        if isinstance(num, (list, np.ndarray)):
            for i in num:
                self.ints.append(i)
                self.n += 1
        else:
            self.ints = np.append(self.ints, num)
            self.n += 1

    def calculate_expected_sum(self):
        n = self.n
        return n * (n + 1)//2

    def calculate_actual_sum(self):
        return np.sum(self.ints)

    def find_missing_entity(self):
        return self.calculate_expected_sum() - self.calculate_actual_sum()

    # Define a function to swap array entries based on index
    def swap(self, i, j):
        self.ints[i], self.ints[j] = self.ints[j], self.ints[i]

    # Return minimum/maximum numbers present in array
    def minimum(self):
        return np.amin(self.ints)
    def maximum(self):
        return np.amax(self.ints)

    # Define a function to reverse the array
    def reverse(self):
        for i in range(self.n//2):          # Reverse array
            self.swap(i, self.n - 1 - i)

    #
    #
    #
    # SORTING ALGORITHMS
    #   - implemented to favour ascending order

    # 1. Selection Sort:
    #   - find minimum element, move to start
    def sort_selection(self):
        for i in range(self.n):
            min_i = i
            for j in range(i + 1, self.n):
                if self.ints[j] < self.ints[min_i]:
                    min_i = j
            self.swap(i, min_i)

    # 2. Bubble Sort:
    #   - find min of 2 adjacent elements, swap if larger value precedes
    def sort_bubble(self):
        not_sorted = True
        c = 0
        swaps = 0
        while not_sorted:
            if self.ints[c] > self.ints[c + 1]:
                self.swap(c, c + 1)
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
            if self.ints[i] > self.ints[i + 1]:
                self.swap(i, i + 1)
        if n != (self.n - 2):
            self.sort_bubble_recursive(n + 1)

    # 4. Insertion Sort:
    #   - Array is split into sorted & unsorted partitions
    #   - First term of the unsorted side is selected and
    #       placed into correct position in sorted array
    def sort_insertion(self):
        for i in range(1, self.n):
            if self.ints[i] < self.ints[i - 1]:
                j = 0
                while self.ints[i] < self.ints[i - 1 - j]:
                    j += 1
                if j >= i:
                    j = i
                for k in range(j):
                    self.swap(i - k, i - k - 1)

    # 5. Recursive Insertion Sort
    #   - Same process as insertion sort, applied recursively
    def sort_insertion_recursive(self, index=1):
        j = 1
        while self.ints[index - j + 1] < self.ints[index - j]:
            self.swap(index - j, index - j + 1)
            if (index - j) > 0:
                j += 1
        if index < (self.n - 1):
            self.sort_insertion_recursive(index + 1)
        else:
            return

    # 6. Merge Sort 
    #   - Partition the provided array into 2 parts
    #   - Sort each partition independently
    #   - Merge Sorted arrays back into a single array
    #   - TOP-DOWN approach
    def sort_merge(self, arr=None):
        if arr is None:
            self.sort_merge(self.ints)
        elif arr.size > 1:
            split = arr.size//2

            # Split array into 2, Sort each side (L & R) independently
            L = np.array(arr[:split])
            R = np.array(arr[split:])
            self.sort_merge(L)
            self.sort_merge(R)

            # Merge L & R sides of array as ordered
            iL = iR = iA = 0
            while iL < L.size and iR < R.size:
                if L[iL] < R[iR]:
                    arr[iA] = L[iL]
                    iL += 1
                else:
                    arr[iA] = R[iR]
                    iR += 1
                iA += 1
            
            # Catch Remainders
            while iL < L.size:
                arr[iA] = L[iL]
                iL += 1
                iA += 1
            while iR < R.size:
                arr[iA] = R[iR]
                iR += 1
                iA += 1
    
    # 7. Merge Sort (Iterative)
    #   - Same implementation as Merge Sort,
    #   - No Recursive function calls
    #   - Implements Merge Sort BOTTOM-UP (from small to large arrays)
    def sort_merge_iterative(self):
        # Set initial block size
        interval = 2
        while interval <= self.n:

            # Partition Array into blocks of specified size (interval)
            blocks = self.n//interval
            #print(f"interval:{interval}\tblocks:{blocks}| {self.nums}")

            # Sort each individual block
            for b in range(blocks):
                # Set starting index for block
                i0 = b * interval
                # Loop through all entries in single block
                for i in range(interval - 1):
                    iMod = i + 1
                    while iMod < interval and self.ints[i0 + i] > self.ints[i0 + iMod]:
                        self.swap(i0 + i, i0 + iMod)
                        iMod += 1
            #print(f"blocksort:{interval}\tblocks:{blocks}| {self.nums}")
 
            # Merge adjacent blocks (A & B)
            for i in range(blocks//2):
                iA = i * 2 * interval       # Start index of block A
                iB = iA + interval          # Start index of block B
                for a in range(iA, iB):
                    b = iB
                    while b < self.n and self.ints[a] > self.ints[b]:
                        self.swap(a, b)
                        b += 1

            # Double block size
            interval *= 2

    # 8. Quick Sort
    #   - Select a pivot (First number used in this case)
    #   - Partition array into two sections based on values:
    #       1. Greater Than Pivot
    #       2. Smaller Than Pivot
    def sort_quick(self, start=0, end=None):
        if end is None:
            end = self.n
        if start < end:
            pivot = self.ints[end - 1]
            low = start - 1

            for i in range(start, end):
                if self.ints[i] < pivot:
                    low += 1
                    self.swap(low, i)

            low += 1
            self.swap(low, end - 1)

            self.sort_quick(start, low)
            self.sort_quick(low + 1, end)

    # 9. Quick Sort (Iterative)
    #   - Same pivot based algorithm as quick sort
    #   - Implemented iteratively
    #   - Use a temporary array to store indices in sorted form
    def sort_quick_iterative(self):
        stack = self.ints
        pivot_pos = 0               # Set pivot as first index
        pivot = stack[pivot_pos]
        pivot_pos += 1

        while pivot_pos < self.n - 1:
            # Position the pivot in correct position in stack array
            for i in range(pivot_pos, self.n):
                if self.ints[i] <= pivot:
                    self.swap(i, i - 1)

            pivot_pos += 1
            pivot = stack[pivot_pos]

            for l in range(pivot_pos):
                if self.ints[l] > self.ints[l + 1]:
                    self.swap(l, l + 1)
            
            for h in range(pivot_pos, self.n):
                if self.ints[h] < self.ints[h - 1]:
                    self.swap(h, h - 1)

    # 10. Heap Sort (Binary Tree)
    #   - Array is converted to a binary tree format
    #   - Smallest values are positioned furthest from the root
    #   - Root assumes value of maximum array value
    def sort_binary_heap(self, index=-1, size=0):
        if index == -1:
            for i in range(self.n//2, -1, -1):
                self.sort_binary_heap(i, self.n)
            for i in range(self.n - 1, 0, -1):
                self.swap(0, i)
                self.sort_binary_heap(0, i)
        else:
            P = index          # Parent node index
            L = 2*P + 1        # Left node index
            R = 2*P + 2        # Right node index

            # Order P, L, R nodes so P is the largest value, followed by R then L       
            if L < size and self.ints[index] < self.ints[L]:
                P = L
            if R < size and self.ints[P] < self.ints[R]:
                P = R
            # If larger number detected
            if P != index:
                self.swap(P, index)
                self.sort_binary_heap(P, size)

        #else:
        #    for i in range(self.n//2):     # Re-Order descending to ascending sorted form
        #        self.swap(i, self.n - i - 1)

    # 11. Counting Sort
    #   - Operates by counting instances of occuring numbers
    #   - Converts count array to the cumulative sum of counts
    #   - Count array describes the index of the 
    def sort_counting(self):
        mini = self.minimum()
        maxi = self.maximum()
        count = np.zeros(maxi - mini + 1)
 
        for i in range(self.n):         # Count the nubmer of unique occurrences
            count[self.ints[i]] += 1
        #print("count_array: \t\t", count)
        for i in range(1, count.size):  # Convert count to cumulative sum
            count[i] += count[i - 1]
        #print("cumulative_array: \t", count)
        
        output = np.zeros(self.n, dtype=self.ints.dtype)
        for i in range(self.n):
            output[int (count[self.ints[i]]) - 1] = self.ints[i]
            count[self.ints[i]] -= 1
        self.ints = output

    # 12. Radix Sort
    #   - An implementation of counting sort that relies on digit values
    #   - Numbers are grouped by shared digits in the same place value
    #   - Digits groups are sorted from least significant to most significant
    def sort_radix(self):
        digits = len(format(abs(self.maximum())))   # Get max number of digits
        for i in range(digits):             # Loop through all digit positions
            dec = 10**(i+1)         # Set decimal digit place to sort
            
            # Implement Counting Sort Algorithm for digit range
            output = np.zeros(self.n, dtype=self.ints.dtype)
            count = np.zeros(10, dtype=int)

            for c in range(self.n):     # Count digit occurences
                count[(self.ints[c] % dec)//(dec//10)] += 1
            for c in range(1, 10):      # Convert to cumulative sum
                count[c] += count[c - 1]
            for j in range(self.n - 1, -1, -1):     # Set Output array
                index = (self.ints[j] % dec)//(dec//10)
                output[count[index] - 1] = self.ints[j]
                count[index] -= 1
            self.ints = output

    # 13. Bucket Sort
    #   - Applies to sorting uniform distributions over a range
    #   - Capable of handling floats
    def sort_bucket(self, n_bins=0):
        if n_bins == 0:
            n_bins = self.n//4
        bins = [[] for n in range(n_bins)]      # Set bin/bucket array
        mini = self.minimum()
        maxi = self.maximum()
        interval = (maxi - mini)//(n_bins) + 1  # Set the interval each bin contains
        
        for i in range(self.n):     # Arrange the array into bins/buckets
            mov = mini
            pos = 0
            while pos < n_bins and self.ints[i] >= mov:
                mov += interval
                pos += 1
            bins[pos - 1].append(self.ints[i])
        #print(f"bins:{bins}\n")
        for b in bins:      # Loop through bins & sort each bin independently
            for i in range(1, len(b)):     # Insertion Sort
                comp = b[i]
                mov = i - 1
                while mov >= 0 and comp < b[mov]:
                    b[mov + 1], b[mov] = b[mov], b[mov + 1]
                    mov -= 1
                    
        i = 0
        for b in bins:      # Extract bins back to array
            for j in b:
                self.ints[i] = j
                i += 1
            
    # 14. Shell Sort
    #   - Operates similarly to insert sort by comparing elements and swapping
    #   - Works with intervals instead by comparing elements an interval apart 
    def sort_shell(self, interval=0):
        if interval == 0:
            interval = self.n//2    # Initial interval size
        while interval > 0:
            #print("interval:", format(interval), end = "  ")
            for i in range(interval, self.n):
                hold = self.ints[i]
                mov = i
                while mov >= interval and self.ints[mov - interval] > hold:
                    self.ints[mov] = self.ints[mov - interval]
                    mov -= interval 
                self.ints[mov] = hold
            #print(self.ints)
            interval = interval//2  # Set next interval value

    # 15. Tim Sort
    #   - A combination of insertion sort and merge sort algorithms
    #   - Array divided into 'runs' (smaller arrays)
    #   - Insertion sort on smaller arrays
    #   - Merge algorithm from merge sort implemented to combine runs
    def sort_tim(self):
        run_size = 4                    # Define run (sub-array) size
        runs = self.n//run_size
        
        # Insertion Sort Function for all runs
        for r in range(runs):
            r_start = r * run_size
            r_end = r_start + run_size
            if r == (runs - 1) and r_end > self.n:    # Sort remainder
                r_end = self.n
            
            for i in range(r_start, r_end):     #
                mov = i
                while mov > r_start and self.ints[mov] < self.ints[mov - 1]:
                    self.swap(mov, mov - 1)
                    mov -= 1
        #print("post_run: ", self.ints)
        
        # Merge Function for all runs
        interval = run_size
        n_interval = runs
        while True:
            for r in range(n_interval//2):
                A = r*2 * interval         # Start index of run A
                B = A + interval          # Start index of run B
                Amax = B
                Bmax = B + interval
                arrTemp = np.zeros(Bmax - A)     # Resultant array
                iT = 0
                iA = A
                iB = B
                #print(f"int:{interval}: \t\t A:{A}|Amax:{Amax}-B:{B}|Bmax:{Bmax} \tTempArr[{Bmax - A}]")
                while iA < Amax and iB < Bmax:
                    if self.ints[iA] < self.ints[iB]:
                        arrTemp[iT] = self.ints[iA]
                        iA += 1
                    else:
                        arrTemp[iT] = self.ints[iB]
                        iB += 1
                    iT += 1
                # Catch remaining numbers
                while iA < Amax:
                    arrTemp[iT] = self.ints[iA]
                    iA += 1
                    iT += 1
                while iB < Bmax:
                    arrTemp[iT] = self.ints[iB]
                    iB += 1
                    iT += 1
                # Feed sorted array back into main array
                self.ints[A:Bmax] = arrTemp

            interval *= 2
            if interval > self.n:
                break
            else:
                n_interval = self.n//interval

def main():
    # Test Functions
    t_n = 16
    t = NumberArray(t_n)
    #print(t1)
    t.shuffle()
    #print(t1)

    # Test remove, add & sum methods
    t_rem = 10
    t.remove(num=t_rem)
    #print(f"remove:{t1_rem}, new_series:{t1}") 
    #print(f"expected_sum_of_series:{t1.calculate_expected_sum()}")
    #print(f"actual_sum_of_series:{t1.calculate_actual_sum()}")
    missing = t.find_missing_entity()
    #print(f"missing:{missing}")
    t.add(missing)
    #print(f"add_missing_entity:{t1}")

    # Test Sorting Methods
    dashes = '-'*(t.n * 4)
    print(dashes)
    print("Unsorted: ", t)
    print(dashes)

    t_sel = copy.deepcopy(t)
    t_sel.sort_selection()
    #print("sort_sel: ", t_sel, "\n")

    t_bub = copy.deepcopy(t)
    t_bub.sort_bubble()
    #print("sort_bub: ", t_bub, "\n")

    t_brc = copy.deepcopy(t)
    t_brc.sort_bubble_recursive()
    #print("sort_brc: ", t_brc, "\n")

    t_ins = copy.deepcopy(t)
    t_ins.sort_insertion()
    #print("sort_ins: ", t_ins, "\n")

    t_irc = copy.deepcopy(t)
    t_irc.sort_insertion_recursive()
    #print("sort_irc: ", t_irc, "\n")

    t_mrg = copy.deepcopy(t)
    t_mrg.sort_merge()
    #print("sort_mrg: ", t_mrg, "\n")

    t_mgi = copy.deepcopy(t)
    t_mgi.sort_merge_iterative()
    #print("sort_mgi: ", t_mgi, "\n")

    t_qui = copy.deepcopy(t)
    t_qui.sort_quick()
    #print("sort_qui: ", t_qui, "\n")

    t_qit = copy.deepcopy(t)
    t_qit.sort_quick_iterative()
    #print("sort_qit: ", t_qit, "\n")

    t_bhp = copy.deepcopy(t) 
    t_bhp.sort_binary_heap()
    #print("sort_bhp: ", t_bhp, "\n")

    t_cnt = copy.deepcopy(t)
    t_cnt.sort_counting()
    #print("sort_cnt: ", t_cnt, "\n")

    t_rad = copy.deepcopy(t)
    t_rad.sort_radix()
    #print("sort_rad: ", t_rad, "\n")

    t_buc = copy.deepcopy(t)
    t_buc.sort_bucket()
    #print("sort_buc: ", t_buc, "\n")

    t_shl = copy.deepcopy(t)
    t_shl.sort_shell()
    print("sort_shl: ", t_shl, "\n")

    t_tim = copy.deepcopy(t)
    t_tim.sort_tim()
    print("sort_tim: ", t_tim, "\n")

if __name__ == "__main__":
    main()