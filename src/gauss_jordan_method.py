import numpy

def inverse_of(nxn_matrix):
    n = nxn_matrix.size()
    ret_matrix = numpy.array((n, n))
    return ret_matrix

def to_reduced_row_echelon_form(matrix):
    for j in range(matrix):

def main():
    test_matrix = numpy.array(([1, 3, 1, 9],[1, 1, -1, 1],[3, 11, 5, 35]))
    print("TestMatrix:")
    print(test_matrix)
    inv_test_matrix = inverse_of(test_matrix)
    print("Inverse TestMatrix:")
    print(inv_test_matrix)

if __name__ == "__main__":
    main() 