from os import remove
import numpy as np
from numpy.lib.twodim_base import diag

# Read input file
def read_int_input(fname):
    with open(fname, 'r') as f:
        arr = np.array(f.read().splitlines())
    return arr

# Assembly of most common binary bits in each position 
def read_gamma(diag):
    binret = ''
    for i in range(len(diag[0])):
        ones = 0
        zeros = 0
        for d in range(diag.size):
            if diag[d][i] == '0':
                zeros += 1
            else:
                ones += 1
        if zeros > ones:
            binret += '0'
        else:
            binret += '1'
    return binret

# Convert binary sequence to decimal int
def bin_to_decimal(binput):
    decret = 0
    bits = len(binput) - 1
    for i in range(bits, -1, -1):
        #print(f'i:{i}, bin_i:{binput[i]}')
        if binput[bits - i] == '1':
            decret += 2**(i)
    return decret

# Invert binary sequence
def invert_bin(binput):
    inv = ''
    for i in binput:
        if i == '0':
            inv += '1'
        else:
            inv += '0'
    return inv

# Part 2:

# Filter out array entries if the value is equal to the specified value
#   at the defined bit position
def filter_bits(array, bit_position, value):
    rem = []
    for i in range(array.size):
        if array[i][bit_position] != value:
            rem.append(i)   # Add to removal list
    return np.delete(array, np.array(rem))

# Recursive method to single out most common binary value
def read_oxygen(diags, bit=0):
    if diags.size > 1 and bit < len(diags[0]):
        zeros = 0
        ones = 0
        for d in range(diags.size):
            if diags[d][bit] == '0':
                zeros += 1
            else:
                ones += 1
        new_diags = []
        if zeros > ones:
            new_diags = filter_bits(diags, bit, '0')
        else:
            new_diags = filter_bits(diags, bit, '1')
        return read_oxygen(new_diags, bit+1)
    else:
        return diags

# Recursive method to single out least common binary value
def read_co2(diags, bit=0):
    if diags.size > 1 and bit < len(diags[0]):
        zeros = 0
        ones = 0
        for d in range(diags.size):
            if diags[d][bit] == '0':
                zeros += 1
            else:
                ones += 1
        if zeros > ones:
            diags = filter_bits(diags, bit, '1')
        else:
            diags = filter_bits(diags, bit, '0')
        return read_co2(diags, bit+1)
    else:
        return diags

def main():

    # Part 1 -------------------------------------------------------------
    # Read input file
    relative_path = 'src/tasks/advent_of_code_21/'
    diagnostics = read_int_input(relative_path + 'day3_input.txt')
    #print(diagnostics)

    # Interpret binary diagnostic data
    binrep = read_gamma(diagnostics) 
    gammma = bin_to_decimal(binrep)
    
    # Epsilon equals inv of gamma
    epsilon = bin_to_decimal(invert_bin(binrep))     
    print(f"Gamma:{gammma}, Epsilon:{epsilon}")
    print(f"Power Consumption:{gammma * epsilon}")

    # Part 2 -------------------------------------------------------------
    # Interpret oxygen rating by filtering out values with less common bits
    oxycopy = diagnostics 
    oxy_rating = read_oxygen(oxycopy)
    oxy = bin_to_decimal(oxy_rating[0])
    print(f"oxygen_generator_rating:{oxy_rating}, decimal:{oxy}")
    
    # Interpret co2 rating by filtering out values with more common bits
    carbocopy = diagnostics 
    co2_rating = read_co2(carbocopy)
    co2 = bin_to_decimal(co2_rating[0])
    print(f"co2_scrubber_rating:{co2_rating}, decimal:{co2}")

    # Calculate final life support as product of oxy and co2 ratings
    life_support_rating = oxy * co2
    print(f"life_support_rating:{life_support_rating}")

if __name__ == "__main__":
    main()