import numpy as np

# Read input file of ints & store in numpy array
def read_int_input(fname):
    with open(fname, 'r') as f:
        arr = np.array(np.uint16 (f.read().splitlines()))
    return arr

# Count increases
def count_inc(arr):
    inc = 0
    for i in range(1, arr.size):
        if arr[i] > arr[i - 1]:
            inc += 1
    return inc

# Count sum( of ints in specified window) increases
def count_window_inc(wsize, arr):
    inc = 0
    wst = 0
    for i in range(arr.size - wsize):
        wsum = 0
        for w in range(wsize):
            wsum += arr[i + w]
        if wsum > wst:
            inc += 1
        wst = wsum
    return inc
        

def main():
    # Read the measured depths from input file
    relative_path = 'src/tasks/advent_of_code_21/'
    depths = read_int_input(relative_path + 'day1_input.txt')
    print(depths)

    # Define a window size
    window = 3

    # Use test array to test methods
    test_arr = np.array([199,200,208,210,200,207,240,269,260,263])
    #print(test_arr)
    #print(f"testc_increases:{count_inc(test_arr)}")
    #print(f"testc_window[{window}]_inc:{count_window_inc(window, test_arr)}")

    # Print data outputs 
    print(f"count_increases:{count_inc(depths)}")
    print(f"count_window[{window}]_inc:{count_window_inc(window, depths)}")


if __name__ == "__main__":
    main()