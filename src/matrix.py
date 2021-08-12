import numpy

class Matrix:

    matrix = []
    rows = 0
    cols = 0

    # Error Tolerance for floats:
    # if abs( matrix[i, j] ) < epsilon then value = zero 
    epsilon = 1e-14

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
        if row_A_index > (self.rows - 1):
            raise IndexError("row_A_index:", row_A_index, " out of bounds of row_count:", self.rows)
        if row_B_index > (self.rows - 1):
            raise IndexError("row_B_index:", row_B_index, " out of bounds of row_count:", self.rows)
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
        if col_A_index > (self.cols - 1):
            raise IndexError("col_A_index:", col_A_index, " out of bounds of row_count:", self.cols)
        if col_B_index > (self.cols - 1):
            raise IndexError("col_B_index:", col_B_index, " out of bounds of row_count:", self.cols)
        
        temp_row = numpy.array(self.matrix[:, col_A_index])
        self.matrix[:, col_A_index] = self.matrix[:, col_B_index]
        self.matrix[:, col_B_index] = temp_row

    # Remove Full Zero rows from Matrix
    def remove_full_zero_rows(self):
        self.matrix = self.matrix[~numpy.all(self.matrix==0, axis=1)]
        self.rows = self.matrix.shape[0]

    # Return the points at which the matrix's largest absolute value occurs
    def argmax(self, row_index=None, col_index=None):
        if row_index == None and col_index == None:
            # If row or col not specified, return arg max of matrix
            return numpy.argmax(self.matrix)
        elif col_index == None:
            # Return argmax of row_index
            return numpy.argmax(self.matrix, axis=1)
        else:
            # Return argmax of col_index
            return numpy.argmax(self.matrix, axis=0)
        
    # Reduce matrix to Row Echelon Form (REF)
    # see https://en.wikipedia.org/wiki/Row_echelon_form#Reduced_row_echelon_form
    def to_row_echelon(self):
        pivot = 0
        while pivot < self.rows and pivot < self.cols:
            row = 1
            restart_pivot = False
            while self.matrix[pivot, pivot] == 0:
                if (pivot + row) < self.rows:
                    pivot += 1
                    restart_pivot = True
                if ~restart_pivot:
                    self.swap_rows(row, (row + pivot) - 1)
                    row += 1
            
            if ~restart_pivot:
                for r in range(1, self.rows - pivot):
                    if self.matrix[pivot + r, pivot] != 0:
                        X = -self.matrix[pivot + r, pivot]/self.matrix[pivot, pivot]
                        for c in range(pivot, self.cols):
                            self.matrix[pivot + r, c] = self.matrix[pivot, c] * X
                            self.matrix[pivot + r, c] += self.matrix[pivot + r, c]

                pivot += 1
        

    # Reduce matrix to reduced row echelon form (RREF)
    def to_reduced_row_echelon(self):
        lead = 0
        r = 0
        stopCondition = False
        self.matrix
        # matrix loop
        while r <= self.rows and ~stopCondition:
            if self.cols <= lead:
                stopCondition = True
            while self.matrix[r, lead] == 0 and ~stopCondition:
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
    test_matrix = numpy.array(([1, 1, 3], [0, 4, 2]))
    m = Matrix(test_matrix)

    print("Test_Matrix:")
    print(m)
    print("rows:", m.rows)
    print("cols:", m.cols)

    print("Test Add Rows:")
    m_plusRows = [[1, 2, 3], [0, 0, 0]]
    m.add_rows(m_plusRows)
    print(m)
    print("rows:", m.rows)
    print("cols:", m.cols)

    print("Test Add Cols:")
    m_plusCols = numpy.array([[4, 4, 2, 0], [1, 2, 3, 0], [5, 0, 1, 0]])
    m.add_cols(m_plusCols)
    print(m)
    print("rows:", m.rows)
    print("cols:", m.cols)

    Aindex = 1
    Bindex = 2
    print("Test Swap Rows(", Aindex, "&", Bindex, "):")
    m.swap_rows(Aindex, Bindex)
    print(m)
    print("Test Swap Cols(", Aindex, "&", Bindex, "):")
    m.swap_cols(Aindex, Bindex)
    print(m)
    
    print("Test Remove Full Zero Rows:")
    print("rows:", m.rows)
    print("cols:", m.cols)
    m.remove_full_zero_rows()
    print(m)
    print("rows:", m.rows)
    print("cols:", m.cols)

    print("Test Row Echelon Form:")
    mre = m
    mre.to_row_echelon()
    print(mre)
    
    """
    # Test Reduced Row Echelon method
    print("RR_Echelon Form:")
    print(m.reduced_row_echelon)
    
    # Test Inverse method
    print("Inv_Matrix:")
    print(m.inverse)
    """

if __name__ == "__main__":
    main()