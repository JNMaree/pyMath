# Sum divided by the number of entries
def calculate_avg(array):
    arr_sum = 0
    for i in array:
        arr_sum += i
    arr_sum /= len(array)
    return int(arr_sum)

# Middle number of a sorted array
#   - divides top and bottom halfs of array
def calculate_median(array):
    array.sort()
    return array[len(array)//2]

# Calculate total fuel for linear usage
def calculate_total_fuel(array, point):
    fuel = 0
    for i in array:
        fuel += abs(i - point)
    return fuel

# Calculate total fuel for quadratic usage
def calculate_total_crabfuel(array, point):
    fuel = 0
    for i in array:
        displacement = abs(i - point)
        fuel += (displacement * (displacement + 1))//2
    return fuel

def main():

    crabs = []

    relative_path = 'src/tasks/advent_of_code_21/day7_input.txt'
    with open(relative_path, 'r') as f:
        crabs = [int(x) for x in f.readline().split(',')]
    print("crabs:", crabs)

    avg = calculate_avg(crabs)
    med = calculate_median(crabs)
    
    half_window = 10
    min_fuel = calculate_total_fuel(crabs, 0)
    min_pos = 0
    for i in range(med - half_window, med + half_window):
        fuel = calculate_total_fuel(crabs, i)
        #print(f"fuel:{fuel} at {i}")
        if fuel < min_fuel:
            min_fuel = fuel
            min_pos = i
    print(f"Average pos:{avg}, Median pos:{med}")
    print(f"sub: \tminimum fuel:{min_fuel} at pos:{min_pos}")

    # Part 2 ---------------------------------------------------------------------------
    
    min_fuel = calculate_total_crabfuel(crabs, avg)
    min_pos = avg
    for i in range(avg - half_window, avg + half_window):
        fuel = calculate_total_crabfuel(crabs, i)
        #print(f"fuel:{fuel} at {i}")
        if fuel < min_fuel:
            min_fuel = fuel
            min_pos = i
    print(f"crabs: \tminimum fuel:{min_fuel} at pos:{min_pos}")

if __name__ == "__main__":
    main()