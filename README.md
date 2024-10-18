# Numerical Computing Toolbox

A collection of well-documented algorithms and utilities for numerical computing. This repository provides implementations for various vector and matrix norms, as well as other numerical methods frequently used in machine learning, data science, and optimization tasks. Whether you're a student, researcher, or developer, you'll find useful tools here for working with vectors, matrices, and clustering algorithms.

## Features
- **Norm Calculations**: Includes functions to compute 1-norm, 2-norm (Euclidean norm), p-norm, max norm (infinity norm), and custom norms like the previous difference norm.
- **Matrix Operations**: Utilities for operations like matrix multiplication, transposing, computing eigenvalues, and more.
- **Code Readability**: Each function is clearly documented, with examples of usage and explanation of the underlying algorithm.
- **Extensible**: Easy to add new numerical methods or modify existing ones.

## Available Functions

### Vector Norms
- `one_norm(vector)`: Computes the 1-norm (sum of absolute values of elements).
- `max_norm(vector)`: Computes the max norm (largest absolute value).
- `p_norm(vector, p)`: General p-norm calculation (sum of absolute values raised to the power of `p`, and then taking the `p`-th root).
- `two_norm(vector)`: Special case of `p_norm` with `p=2` (Euclidean norm).
- `previous_difference_norm(vector)`: Calculates the sum of the absolute differences between consecutive elements.

### Matrix Operations
- `one_norm(matrix)`: Calculates the one-norm of a matrix (maximum of the column sums).
- `infinity_norm(matrix)`: Calculates the infinity norm (maximum row sum).
- `frobenius_norm(matrix)`: Calculates the Frobenius norm (square root of the sum of squared elements).
- `max_norm(matrix)`: Calculates the max norm (largest absolute value of any element in the matrix).
- `two_norm(matrix)`: Calculates the two-norm (largest singular value of the matrix).
- `column_sums(matrix)`: Computes the sum of absolute values for each column of the matrix.
- `row_sums(matrix)`: Computes the sum of absolute values for each row of the matrix.
- `transpose(matrix)`: Transposes a matrix.
- `matrix_multiply(matrix1, matrix2)`: Multiplies two matrices.
- `compute_eigenvalues(matrix)`: Computes the eigenvalues of a square matrix.

## Example Usage
```python
from matrix_norms import *
from vector_norms import *
# Example: 1-norm calculation
vector = [1, -2, 3, -4]
result = one_norm(vector)
print(result)  # Output: 10.0

# Example: 2-norm calculation
vector = [3, 4]
result = two_norm(vector)
print(result)  # Output: 5.0

# Example: Previous difference norm
vector = [2, 5, 1, -3]
result = previous_difference_norm(vector)
print(result)  # Output: 13.0

# Example: Matrix one-norm
matrix = [[1, -2, 3], [-4, 5, -6]]
result = one_norm(matrix)
print(result)  # Output: 9.0
```
