import numpy

def to_reduced_row_echelon_form(matrix):
    lead = 0
    for r in range(matrix.shape[0]):
        if matrix.shape[1] <= lead:
            break
        while matrix[r, lead]:
            i = r + 1
            if matrix.shape[0] == i:
                i = r
                lead += 1
                if matrix.shape[1] == lead:
                    break

def inverse_of(matrix):
    # Check if 2D and nxn
    if matrix.ndim == 2 and matrix.shape[0] == matrix.shape[1]:
        # Using a numpy function
        ret_matrix = numpy.linalg.inv(matrix)
        return ret_matrix
    else:
        raise ArithmeticError    
                

def main():
    test_matrix = numpy.array(([1, 1, 3], [0, 2, 4], [-1, 1, 0]))
    print("Test_Matrix:")
    print(test_matrix)
    inverse_matrix = inverse_of(test_matrix)
    print("Inv_Matrix:")
    print(inverse_matrix)
    #inv_test_matrix = inverse_of(test_matrix)
    #print("Inverse TestMatrix:")
    #print(inv_test_matrix)

if __name__ == "__main__":
    main()