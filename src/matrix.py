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
        return format(self.matrix)
    
    """
    Class Methods:
        Basic Matrix Algebra:
            - Append Rows to matrix
            - Append Columns to matrix
                
        Matrix Transformations:
            - Row Echelon form
            - Reduced Row Echelon form
    """
    # ROW METHODS:
    # Add rows to matrix
    def add_rows(self, rows, pos =None):
        if isinstance(rows, numpy.ndarray):
            addRows = rows
        elif isinstance(rows, list):
            addRows = numpy.array(rows)
        else: #not isinstance(rows, numpy.ndarray):
            raise TypeError("list or numpy.ndarray types supported")

        if pos == None:
            # If position not specified, append row to end of matrix
            rowPos = self.rows
        else:
            rowPos = pos

        if addRows.ndim > 1:
            self.rows += addRows.shape[0]
        else:
            self.rows += 1
        
        self.matrix = numpy.insert(self.matrix, rowPos, addRows, axis=0)
    def swap_rows(self, row_A_index, row_B_index):
        temp_row = numpy.array(self.matrix[row_A_index, :])
        self.matrix[row_A_index, :] = self.matrix[row_B_index, :]
        self.matrix[row_B_index, :] = temp_row

    # COL METHODS:
    # Add columns to matrix
    def add_cols(self, cols, pos =None):
        if isinstance(cols, numpy.ndarray):
            addCols = cols
        elif isinstance(cols, list):
            addCols = numpy.array(cols)
        else:
            raise TypeError("list or numpy.ndarray types supported")

        if pos == None:
            # If position not specified, append col to end of matrix
            colPos = self.cols
        else:
            colPos = pos

        if addCols.ndim == 1:
            self.cols += 1
        else:
            self.cols += addCols.shape[0]
        
        self.matrix = numpy.insert(self.matrix, colPos, addCols, axis=1)
    def swap_cols(self, col_A_index, col_B_index):
        temp_row = numpy.array(self.matrix[:, col_A_index])
        self.matrix[:, col_A_index] = self.matrix[:, col_B_index]
        self.matrix[:, col_B_index] = temp_row

    # Remove Full Zero rows from Matrix
    def remove_full_zero_rows(self):
        for r in range(self.rows):
            nonZero = False
            for c in range(self.cols):
                if self.matrix[r, c] != 0:
                    nonZero = True
                    break

            if not nonZero:
                self.swapRows(r, self.rows - 1)
                self.matrix = numpy.delete(self.matrix, self.rows - 1, axis=0)
                self.rows -= 1

    # Reduce matrix to Row Echelon Form (REF)
    def to_row_echelon(self):
        self.removeFullZeroRows
                

    # Reduce matrix to reduced row echelon form (RREF)
    def to_reduced_row_echelon(self):
        lead = 0
        r = 0
        stopCondition = False
        self.matrix
        # matrix loop
        while r <= self.rows and not stopCondition:
            if self.cols <= lead:
                stopCondition = True
            while self.matrix[r, lead] == 0 and not stopCondition:
                i = r + 1
                if self.rows == i:
                    i = r
                    lead += 1
                    if self.rows == lead:
                        stopCondition = True
            if i != r:
                self.matrix[[i, r],:] = self.matrix[[r, i], :]
            self.matrix[r, :] /= self.matrix[r, lead]
            for i in range(self.rows):
                if i != r:
                    self.matrix[i] -= self.matrix[i, lead]*self.matrix[r]
            lead += 1
            r += 1


    # Return the inverse of the matrix
    def get_inverse(self):
        # Check if 2D and nxn (square)
        if self.matrix.ndim == 2 and self.rows == self.cols:
            # Using a numpy function
            return numpy.linalg.inv(self.matrix)
        else:
            raise ArithmeticError

    # Return an identity matrix for the same size
    def get_identity(self, size=0):
        # Check if 2D and square (nxn)
        if self.matrix.ndim >= 2:
            return numpy.eye(self.rows, self.cols)
        elif size > 0:
            return numpy.eye(size)
        else:
            return numpy.eye(self.matrix.shape[0])
            
# Test function
def main():
    #test_matrix = numpy.array(([1, 1, 3], [0, 2, 4], [1, 1, 0], [0, 1, 1]))
    test_matrix = numpy.array(([1, 1, 3], [0, 2, 4]))
    m = Matrix(test_matrix)

    print("Test_Matrix:")
    print(m)
    print("rows:", m.rows)
    print("cols:", m.cols)

    print("Test Add Rows:")
    m_plusRows = [[1, 1, 0], [0, 1, 1]]
    m.addRows(m_plusRows)
    print(m)
    print("rows:", m.rows)
    print("cols:", m.cols)

    print("Test Add Cols:")
    m_plusCols = numpy.array([[4, 3, 2, 1], [1, 2, 3, 5], [3, 6, 9, 12]])
    m.addCols(m_plusCols)
    print(m)
    print("rows:", m.rows)
    print("cols:", m.cols)

    Aindex = 1
    Bindex = 2
    print("Test Swap Rows(", Aindex, "&", Bindex, "):")
    m.swapRows(Aindex, Bindex)
    print(m)
    print("Test Swap Cols(", Aindex, "&", Bindex, "):")
    m.swapCols(Aindex, Bindex)
    print(m)
    
    """
    # Test Row Echelon form
    print("R_Echelon Form:")
    print(m.row_echelon)
    
    # Test Reduced Row Echelon method
    print("RR_Echelon Form:")
    print(m.reduced_row_echelon)
    
    # Test Inverse method
    print("Inv_Matrix:")
    print(m.inverse)
    """

if __name__ == "__main__":
    main()