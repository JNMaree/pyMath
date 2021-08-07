import numpy

class Matrix:

    matrix = []
    rows = 0
    cols = 0

    def __init__(self, array):
        if isinstance(array, numpy.ndarray):
            self.matrix = array
            self.rows = array.shape[0]
            self.cols = array.shape[1]
        elif isinstance(array, list):
            self.matrix = numpy.array(array)
            self.rows = len(array)
            self.cols = len(array[0])
            
    # Overload [] operator
    def __getitem__(self, key):
        return self.matrix[key]
    def __setitem__(self, key, value):
        self.matrix[key] = value
    # Overload 'string' method
    def __str__(self):
        ret = ""
        for r in self.matrix:
            ret += "["
            for c in range(len(r)):
                if c < (self.cols - 1):
                    ret += format(r[c]) + ", "
                else:
                    ret += format(r[c])
            ret += "]\n"
        return ret

    # Reduce to Row Echelon Form (REF)
    def row_echelon(self):
        ret_matrix = self.matrix
        
        for r in range(ret_matrix.shape[0]):
            zeros = True
            for c in range(ret_matrix.shape[1]):
                pass

    # Reduce a matrix to its reduced row echelon form (RREF)
    def reduced_row_echelon(self):
        lead = 0
        r = 0
        stopCondition = False
        ret_matrix = self.matrix

        # matrix loop
        while r <= self.rows and not stopCondition:
            if ret_matrix.shape[1] <= lead:
                stopCondition = True
            while ret_matrix[r, lead] == 0 and not stopCondition:
                i = r + 1
                if ret_matrix.shape[0] == i:
                    i = r
                    lead += 1
                    if ret_matrix.shape[1] == lead:
                        stopCondition = True
            if i != r:
                ret_matrix[[i, r],:] = ret_matrix[[r, i], :]
            ret_matrix[r, :] /= ret_matrix[r, lead]
            for i in range(self.rows):
                if i != r:
                    ret_matrix[i] -= ret_matrix[i, lead]*ret_matrix[r]
            lead += 1
            r += 1
        return ret_matrix
            
        
    def inverse(self):
        # Check if 2D and nxn (square)
        if self.matrix.ndim == 2 and self.matrix.shape[0] == self.matrix.shape[1]:
            # Using a numpy function
            ret_matrix = numpy.linalg.inv(self.matrix)
            return ret_matrix
        else:
            raise ArithmeticError    
                
# Test function
def main():
    test_matrix = numpy.array(([1, 1, 3], [0, 2, 4], [-1, 1, 0], [0, 0, 1]))
    #test_matrix = numpy.array(([1, 1, 3], [0, 2, 4]))
    m = Matrix(test_matrix)
    print("Test_Matrix:")
    print(m)
    print("rows:", m.rows)
    print("cols:", m.cols)

    # Test Row Echelon form
    print("R_Echelon Form:")
    print(m.row_echelon)

    # Test Reduced Row Echelon method
    print("RR_Echelon Form:")
    print(m.reduced_row_echelon)

    # Test Inverse method
    print("Inv_Matrix:")
    print(m.inverse)
    

if __name__ == "__main__":
    main()