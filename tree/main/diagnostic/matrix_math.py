import math

class Matrix:
    def __init__(self, data):
        """
        Initialize matrix from a 2D list
        Example: Matrix( [[1, 2], [3, 4]] )
        
        :param self: Instance of the matrix
        :param data: the actual matrix
        """

        if not data or not data[0]:
            raise ValueError("Matrix can not be empty!!!")
        self.matrix = [ row[:] for row in data ]    # deep copy
        self.row = len(data)
        self.col = len(data[0])
        if not all(len(row) == self.col for row in data):
            raise ValueError("All rows must have the same length!!!")

    @property
    def shape(self):
        """
        return the shape of the actual matrix
        """
        return ( self.row, self.col )

    @property
    def T(self):
        """
        Return the transpose as a new matrix
        """
        transposed = [[self.matrix[i][j] for i in range(self.row)] for j in range(self.col)]
        return Matrix(transposed)

    def __repr__(self):
        return '\n'.join( str(row) for row in self.matrix )

    def __rmul__(self, other):
        return self.__mul__(other)

    def __mul__(self, other) -> 'Matrix':
        if isinstance(other, (int, float)):
            matrix = []
            for i in range( self.row ):
                new_row = []
                for j in range( self.col ):
                    new_row.append(other*self.matrix[i][j])
                matrix.append( new_row )
            
            return Matrix(matrix)
        
        elif isinstance(other, Matrix):
            if self.col != other.row:
                raise ValueError("The number of column and row are different!!!")
            matrix = []
            for i in range( self.row ):
                new_row = []
                for k in range( other.col ):
                    value = 0
                    for j in range( self.col ):
                        value += self.matrix[i][j]*other.matrix[j][k]
                    new_row.append( value )
                matrix.append( new_row )
            
            return Matrix(matrix)
        else:
            raise TypeError(f"Cannot myltiply <Matrix> by <{type(other).__name__}>")


# def dot_product(v1: Matrix, v2: Matrix):
    # if v1.col != v2.row:
    #     print(f"The number of column in '{v1}'-({v1.col}) is different to the number of row in {v2}-({v2.row})")
    #     raise SystemExit(1)
    
    # else:
    #     result = Matrix(v1.row, v2.col)
    #     result_matrix = []
    #     for v2_row in v2.matrix_t:
    #         rows = []
    #         for v1_row in v1.matrix:
    #             temp = 0
    #             for i in range(v1.col):
    #                 value = v2_row[i]*v1_row[i]
    #                 temp += value
    #             rows.append(temp)
    #         result_matrix.append(rows)
    #     result.matrix = result_matrix
    #     result.matrix_transpose()

    #     return result._t()

def vector_add(v1: Matrix, v2: Matrix) -> Matrix:
    result = Matrix(v1.row, v1.col)
    result_matrix = []
    if v1.shape == v2.shape:
        for i in range(v1.row):
            rows = []
            for j in range(v1.col):
                rows.append( v1.matrix[i][j]+v2.matrix[i][j] )
            result_matrix.append(rows)
        result.matrix = result_matrix
        result.matrix_transpose()
        
        return result
    else:
        print(f"the shape of '{v1}'-{v1.shape} is different to the shape of '{v2}'-{v2.shape}!!!")
        raise SystemExit(1)

def scalar_multiply(s: int, v: Matrix) -> Matrix:
    result = Matrix(v.row, v.col)
    result_matrix = []

    for i in range(v.row):
        rows = []
        for j in range(v.col):
            rows.append( s*v.matrix[i][j] )
        result_matrix.append( rows )
    result.matrix = result_matrix
    result.matrix_transpose()

    return result

def magnitude(v: Matrix) -> Matrix:
    temp = 0
    for i in range(v.row):
        for j in range(v.col):
            temp += (v.matrix[i][j])**2
    
    return math.sqrt(temp)

if __name__ == "__main__":
    A = Matrix([[1, 2, 3], [4, 5, 6]])
    print("Original:")
    print(A)
    print("\nTranspose:")
    print(A.T)