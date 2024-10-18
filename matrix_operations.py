import numpy as np


def column_sums(matrix):
    if not matrix or not matrix[0]:
        return []

    rows = len(matrix)
    cols = len(matrix[0])

    column_sums = [0] * cols

    for row in matrix:
        for j in range(cols):
            column_sums[j] += abs(row[j])

    return column_sums

def row_sums(matrix):
    if not matrix or not matrix[0]:
        return []

    rows = len(matrix)
    cols = len(matrix[0])

    row_sums = [0] * rows

    counter = 0
    for row in matrix:
        row_sums[counter] += sum(abs(x) for x in row)
        counter += 1

    return row_sums

def transpose(matrix):
    if not matrix or not matrix[0]:
        return []


    number_of_rows = len(matrix)
    number_of_columns = len(matrix[0])

    transposed_matrix = [[0] * number_of_rows for _ in range(number_of_columns)]

    for i in range(number_of_rows):
        for j in range(number_of_columns):
            transposed_matrix[j][i] = matrix[i][j]


    return transposed_matrix

def matrix_multiply(matrix1, matrix2):
    if not matrix1 or not matrix2:
        return []

    matrix1_rows = len(matrix1)
    matrix1_cols = len(matrix1[0])

    matrix2_rows = len(matrix2)
    matrix2_cols = len(matrix2[0])

    if matrix1_cols != matrix2_rows:
        return []

    result_matrix = [[0 for _ in range(matrix2_cols)] for _ in range(matrix1_rows)]

    for i in range(matrix1_rows):
        for j in range(matrix2_cols):
            result_matrix[i][j] = sum(matrix1[i][k] * matrix2[k][j] for k in range(matrix1_cols))

    return result_matrix

def compute_eigenvalues(matrix):
    """
    Compute the eigenvalues of a given matrix.

    Parameters:
    matrix (list of lists or numpy array): A square matrix

    Returns:
    list: Eigenvalues of the matrix
    """
    # Convert the input matrix to a numpy array
    matrix_np = np.array(matrix)

    # Check if the matrix is square
    if matrix_np.shape[0] != matrix_np.shape[1]:
        raise ValueError("The matrix must be square (same number of rows and columns).")

    # Compute the eigenvalues using numpy
    eigenvalues = np.linalg.eigvals(matrix_np)

    return eigenvalues.tolist()