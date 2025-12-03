

class matrix:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.shape = (row, col)
        self.matrix = []

    def __repr__(self):
        return f"{self.matrix}"

    def _instantiate(self):
        for row in range(self.row):
            matrix_row = []
            for col in range(self.col):
                matrix_row.append(int(input(f"Enter the number in the { row+1 }-th row and { col+1 }-th column: ")))
            self.matrix.append( matrix_row )

    def _t(self):
        matrix_invers = matrix(self.col, self.row)
        for i in range(self.col):
            mi_row = []
            for row in self.matrix:
                mi_row.append(row[i])
            matrix_invers.matrix.append(mi_row)
        
        return matrix_invers

    def multiply(self, second_matrix: matrix) -> matrix:
        if self.col == second_matrix.row:
            re_invers = matrix( second_matrix.col, self.row )
            for re_row in second_matrix._t().matrix:
                re_rows = []
                for row in self.matrix:
                    temp = 0
                    for i in range(self.col):
                        value = re_row[i]*row[i]
                        temp += value
                    re_rows.append(temp)
                re_invers.matrix.append(re_rows)
        else:
            print(f"the number of columns in the first matrix ({self.col}) is different to the number of rows in the second matrix ({second_matrix.row})!!!")
            raise SystemExit(1)
        
        return re_invers._t()

if __name__ == "__main__":
    a = matrix( 2, 3 )
    b = matrix( 3, 4 )
    a.instantiate()
    b.instantiate()
    print(a.multiply(b))