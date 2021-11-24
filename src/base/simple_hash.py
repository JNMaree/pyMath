import numpy as np

# Collect & compare the hashes for collisions
#   - using the specified array of keys and hash function
def collision_detection(array, hash_function):
    n = array.size
    hashes = np.zeros((n, 2))
    unique_hash_ctr = 0
    list_collisions = {}    # Document the keys causing hash collisions
    collision_ctr = 0
    for i in array:
        t = hash_function(i, n)

        # Test if key hash exists as one of the existing hashes
        unique = True
        ctr = 0
        while ctr < unique_hash_ctr: # Check with every existing hash 
            if t == hashes[ctr, 0]:
                unique = False
                break
            ctr += 1
        if not unique:  # If previous equivalent hash found
            hashes[ctr, 1] += 1
            if t in list_collisions:
                list_collisions[t].append(i)
            else:
                list_collisions[t] = [i]
            collision_ctr += 1
        else:
            hashes[unique_hash_ctr, 0] = t
            unique_hash_ctr += 1
    # Print Output
    print(f"\t>> {collision_ctr} collisions detected on {unique_hash_ctr} unique hashes:")
    if collision_ctr > 0:
        print("\t>>", list_collisions)

# Simple Hash Functions
# 1. Division Method 
#   - n represents the number of desired entries in output hash table
def division(key, n):
    return key % n

# 2. Knuth Division Method
#   - a variation on the traditional division method,
#   - using Knuth's 
def division_knuth(key, n):
    return key * (key + 3) % n

# 3. Multiplication Method
def multiplication(key, n):
    A = 0.5 * (np.sqrt(5) - 1)
    s = key * A 
    s = s - np.fix(s)       # s = fraction part of (key * A)
    return np.fix(n * s)

def main():
    # Create test array
    tarr = np.arange(0, 100)
    print("Test_Array:", tarr)
    
    # Test collisions
    print("division_test:", end=" ")
    collision_detection(tarr, division)
    
    print("division_knuth:", end=" ")
    collision_detection(tarr, division_knuth)

if __name__ == "__main__":
    main()