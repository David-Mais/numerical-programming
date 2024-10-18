from matrix_operations import column_sums
from matrix_operations import row_sums
from matrix_operations import transpose
from matrix_operations import matrix_multiply
from matrix_operations import compute_eigenvalues

def one_norm(matrix) -> float:
    """
    Calculate the one-norm of a matrix, where the one-norm is defined as the maximum of the column sums.

    It is also often called column sum norm

    The one-norm is mathematically represented as:

    \|A\|_1 = max(sum(|a_ij|)) for j = 1, 2, ..., n

    This norm first computes the sum of the absolute values of the elements in each column of the matrix,
    and then returns the maximum of these sums.

    Parameters:
    -----------
    matrix : list of lists
        A two-dimensional list (matrix) where each inner list represents a row of the matrix. The elements
        are numerical values (integers or floats).

    Returns:
    --------
    float
        The computed one-norm of the input matrix, which is the maximum sum of absolute values of the elements
        in any column.

    Algorithm:
    ----------
    1. The function begins by checking if the matrix is empty or has no columns. If so, it returns an empty list.
    2. It calculates the number of rows and columns in the matrix.
    3. The `column_sums` function is called to compute the sums of the absolute values of the elements
       in each column.
    4. Finally, the maximum of these column sums is returned as the one-norm.

    Example:
    --------
    >>> matrix = [[1, -2, 3], [-4, 5, -6]]
    >>> one_norm(matrix)
    9.0

    >>> matrix = [[1, 2], [3, 4], [5, 6]]
    >>> one_norm(matrix)
    12.0
    """
    matrix_column_sums = column_sums(matrix)

    return float(max(matrix_column_sums))


def infinity_norm(matrix) -> float:
    """
    Calculates the infinity norm (maximum row sum norm) of a given matrix.

    The infinity norm of a matrix is the maximum absolute row sum. It is
    defined as:

        ||A||_∞ = max(sum(abs(a_ij) for all j in row i))

    where a_ij are the elements of the matrix A.

    Args:
        matrix (list of list of floats): The matrix for which to calculate the infinity norm.

    Returns:
        float: The infinity norm of the matrix.

    Example:
        matrix = [[1, -2, 3],
                  [-4, 5, 6],
                  [7, -8, 9]]
        norm = infinity_norm(matrix)
        print(norm)  # Output will be 24, since the maximum row sum is |7| + |-8| + |9| = 24.
    """
    matrix_row_sums = row_sums(matrix)
    return float(max(matrix_row_sums))


def frobenius_norm(matrix) -> float:
    """
    Calculates the Frobenius norm of a given matrix.

    The Frobenius norm is defined as the square root of the sum of the squares
    of all elements in the matrix:

        ||A||_F = sqrt(sum(a_ij^2 for all i, j))

    where a_ij are the elements of the matrix A.

    Args:
        matrix (list of list of floats): The matrix for which to calculate the Frobenius norm.

    Returns:
        float: The Frobenius norm of the matrix.

    Example:
        >>> matrix = [[1, 2],[3, 4]]
        >>> frobenius_norm(matrix)
        5.477225575051661

        >>> matrix = ((1, 2),(3, 4))
        >>> frobenius_norm(matrix)
        5.477225575051661
    """
    return sum(element ** 2 for row in matrix for element in row) ** 0.5


def max_norm(matrix) -> float:
    """
    Calculates the max norm (also known as the infinity norm or maximum absolute element norm) of a given matrix.

    The max norm is defined as the maximum absolute value of any element in the matrix:

        ||A||_max = max(abs(a_ij) for all i, j)

    where a_ij are the elements of the matrix A.

    Args:
        matrix (list of list of floats): The matrix for which to calculate the max norm.

    Returns:
        float: The max norm of the matrix, i.e., the largest absolute value of any element in the matrix.

    Example:
    --------
    >>> matrix = [[1, -5, 3],
    ...           [2, 4, -6]]
    >>> max_norm(matrix)
    6.0

    >>> matrix = [[-1, -2],
    ...           [0, 2]]
    >>> max_norm(matrix)
    2.0

    >>> matrix = [[0, 0],
    ...           [0, 0]]
    >>> max_norm(matrix)
    0.0
    """
    return float(max(abs(element) for row in matrix for element in row))

def two_norm(matrix) -> float:
    """
    Calculates the two-norm (also known as the spectral norm or the Euclidean norm) of a given matrix.

    The two-norm of a matrix is defined as the largest singular value of the matrix, which is equivalent to the square root
    of the largest eigenvalue of the matrix's Gram matrix (A^T * A), where A^T is the transpose of A.

        ||A||_2 = sqrt(max(eigenvalue of A^T * A))

    The two-norm measures the maximum amount the matrix can stretch a vector when applied to it.

    Args:
        matrix (list of list of floats): The matrix for which to calculate the two-norm. It must be a square matrix.

    Returns:
        float: The two-norm of the matrix, i.e., the largest singular value.

    Steps:
    --------
    1. Compute the transpose of the matrix (A^T).
    2. Multiply the transposed matrix with the original matrix (A^T * A).
    3. Compute the eigenvalues of the resulting matrix.
    4. Return the square root of the maximum absolute eigenvalue, which represents the two-norm.

    Example:
    --------
    >>> test_matrix = [[1, 2],
    ...           [3, 4]]
    >>> two_norm(test_matrix)
    5.464985704219043

    >>> test_matrix = [[-2, 0],
    ...           [0, 1]]
    >>> two_norm(test_matrix)
    2.0

    >>> test_matrix = [[0, 0],
    ...           [0, 0]]
    >>> two_norm(test_matrix)
    0.0
    """
    transposed_matrix = transpose(matrix)
    matrix_product = matrix_multiply(transposed_matrix, matrix)
    eigenvalues = compute_eigenvalues(matrix_product)

    return max(abs(x) for x in eigenvalues) ** 0.5

mat = ((1,2), (-3, -5), (900, -1000))
print(two_norm.__doc__)