import numpy

class Matrix:

    matrix = []

    def __init__(self, array):
        if isinstance(array, numpy.ndarray):
            self.matrix = array
        elif isinstance(array, list):
            self.matrix = numpy.array(array)

    # Overload [] operator
    def __getitem__(self, key):
        return self.matrix[key]
    def __setitem__(self, key, value):
        self.matrix[key] = value

    # Reduce a matrix to its reduced row echelon form
    def reduced_row_echelon(self):
        lead = 0
        stopCondition = False
        ret_matrix = self.matrix

        # matrix loop
        for r in range(self.matrix.shape[0]):
            if self.matrix.shape[1] <= lead:
                break
            while self.matrix[r, lead] == 0 and not stopCondition:
                i = r + 1
                if self.matrix.shape[0] == i:
                    i = r
                    lead += 1
                    if self.matrix.shape[1] == lead:
                        stopCondition = True
            if i != r:
                self.matrix[[i, r],:] = self.matrix[[r, i], :]
            self.matrix[r, :] /= self.matrix[r, lead]

        return ret_matrix
            
        
    def inverse(self):
        # Check if 2D and nxn (square)
        if self.matrix.ndim == 2 and self.matrix.shape[0] == self.matrix.shape[1]:
            # Using a numpy function
            ret_matrix = numpy.linalg.inv(self.matrix)
            return ret_matrix
        else:
            raise ArithmeticError    
                

def main():
    test_matrix = numpy.array(([1, 1, 3], [0, 2, 4], [-1, 1, 0]))
    print("Test_Matrix:")
    m = Matrix(test_matrix)

    # Test Reduced Row Echelon method
    print("RREchelon Form:")
    print(m.reduced_row_echelon)

    # Test Inverse method
    print("Inv_Matrix:")
    print(m.inverse)
    

if __name__ == "__main__":
    main()