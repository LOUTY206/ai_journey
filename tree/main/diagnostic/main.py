from pprint import pprint


def initiation(matrix: list, rows: int, columns: int):
    for row in range(rows):
        matrix_row = []
        for column in range(columns):
            matrix_row.append(int(input(f"Enter the number in the {row+1}th row and {column+1}th column: ")))
        matrix.append(matrix_row)

# Initiating A
a_shape_row = int(input("Enter the number of row for A: "))
a_shape_column = int(input("Enter the number of column for A: "))
a_shape = (a_shape_row, a_shape_column)
A = []
initiation(A, a_shape_row, a_shape_column)

# Initiating B
b_shape_row = a_shape_column
b_shape_column = int(input("Enter the number of column for B: "))
b_shape = (b_shape_row, b_shape_column)
B = []
initiation(B, b_shape_row, b_shape_column)


# Performing the matrix multiplication
## finding B-invers
def matrix_invers_calculation(matrix: list):
    matrix_invers = []
    for i in range(b_shape_column):
        matrix_invers_row = []
        for row in matrix:
            matrix_invers_row.append(row[i])
        matrix_invers.append(matrix_invers_row)
    return matrix_invers
B_invers = matrix_invers_calculation(B)

## perform the calculation
re_shape_row = a_shape_row
re_shape_column = b_shape_column
re_shape = (re_shape_row, re_shape_column)
result = []
re_invers = []


for b_in_row in B_invers:
    re_rows = []
    for a_row in A:
        temp = 0
        for i in range(a_shape_row):
            value = b_in_row[i]*a_row[i]
            temp += value
        re_rows.append(temp)
    re_invers.append(re_rows)

result = matrix_invers_calculation(re_invers)

        