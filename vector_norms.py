def one_norm(vector) -> float:
    """
    Calculate the 1-norm of a vector (list or tuple).

    The 1-norm of a vector is defined as the sum of the absolute values of its elements.

    Parameters:
    -----------
    vector : list or tuple
        A collection of numerical elements (either integers or floats) for which the 1-norm
        needs to be computed. The function accepts a list or a tuple of numbers as input.

    Returns:
    --------
    float
        The 1-norm of the input vector, which is the sum of the absolute values of the elements
        in the vector.

    Algorithm:
    ----------
    1. Iterate through each element in the input `vector`.
    2. For each element, compute its absolute value using Python's built-in `abs()` function.
    3. Sum all the absolute values.
    4. Return the final sum, which represents the 1-norm of the vector.

    Example:
    --------
    >>> list_vector = [1, -2, 3, -4]
    >>> one_norm(list_vector)
    10.0

    >>> tuple_vector = (1, -2, 3, -4)
    >>> one_norm(tuple_vector)
    10.0
    """
    return float(sum(abs(x) for x in vector))


def max_norm(vector) -> float:
    """
    Calculate the max norm (infinity norm) of a vector (list or tuple).

    The max norm (also called the infinity norm) of a vector is defined as the maximum
    absolute value of its elements. This gives a measure of the largest magnitude in the vector.

    Parameters:
    -----------
    vector : list or tuple
        A collection of numerical elements (either integers or floats). The function accepts
        a list or tuple of numbers as input.

    Returns:
    --------
    float
        The max norm of the input vector, which is the maximum value among the absolute values
        of the elements in the vector, returned as a float.

    Algorithm:
    ----------
    1. Iterate through the elements of the vector.
    2. Compute the maximum absolute value of the elements.
    3. Return the result as a float.

    Example:
    --------
    >>> list_vector = [1, -2, 3, -4]
    >>> max_norm(list_vector)
    4.0

    >>> tuple_vector = (1, -2, 3, -4)
    >>> max_norm(tuple_vector)
    4.0
    """
    return float(max(abs(x) for x in vector))


def p_norm(vector, p) -> float:
    """
    Calculate the p-norm (L-p norm) of a vector (list or tuple).

    The p-norm of a vector is defined as the p-th root of the sum of the absolute values of its
    elements raised to the power of `p`. This is a generalization of norms:
      - For p=1, it is the 1-norm (sum of absolute values).
      - For p=2, it is the Euclidean norm (2-norm or L2 norm).
      - As p approaches infinity, it becomes the max norm (infinity norm).

    Parameters:
    -----------
    vector : list or tuple
        A collection of numerical elements (either integers or floats) for which the p-norm
        needs to be computed. The function accepts a list or tuple of numbers as input.

    p : int or float
        The order of the norm to compute. Must be a positive value greater than or equal to 1.
        Common values of `p` include 1, 2, and infinity.

    Returns:
    --------
    float
        The p-norm of the input vector, calculated as the p-th root of the sum of the absolute
        values of the elements raised to the power `p`.

    Algorithm:
    ----------
    1. Iterate through the elements of the vector.
    2. Compute the absolute value of each element, raise it to the power of `p`.
    3. Sum these powered values.
    4. Take the p-th root of the sum (equivalent to raising the sum to the power of 1/p).
    5. Return the result as a float.

    Example:
    --------
    >>> list_vector = [3, 4, -5]
    >>> p_value = 2
    >>> p_norm(list_vector, p_value)
    7.0710678118654755

    >>> tuple_vector = (1, -2, 3, -4)
    >>> p_value = 3
    >>> p_norm(tuple_vector, p_value)
    4.641588833612778
    """
    return sum(abs(x) ** p for x in vector) ** (1 / p)


def two_norm(vector) -> float:
    """
    Calculate the 2-norm (Euclidean norm) of a vector (list or tuple).

    The 2-norm, also known as the Euclidean norm or L2 norm, is defined as the square root of the sum of the
    squares of the elements in the vector. It represents the standard distance from the origin to the point
    represented by the vector in Euclidean space.

    Mathematically, for a vector `v = [v1, v2, ..., vn]`, the 2-norm is given by:

    \|v\|_2 = sqrt(v1^2 + v2^2 + ... + vn^2)

    This function is a specific case of the p-norm with `p=2`.

    Parameters:
    -----------
    vector : list or tuple
        A collection of numerical elements (either integers or floats) for which the 2-norm is to be computed.
        The function accepts a list or tuple of numbers as input.

    Returns:
    --------
    float
        The 2-norm (Euclidean norm) of the input vector.

    Algorithm:
    ----------
    1. The function uses the general `p_norm` function, passing `p=2`.
    2. This computes the sum of the squares of the absolute values of the vector's elements.
    3. The square root of this sum is taken to return the Euclidean norm.

    Example:
    --------
    >>> list_vector = [3, 4]
    >>> two_norm(list_vector)
    5.0

    >>> tuple_vector = (2, -2, 2, -2)
    >>> two_norm(tuple_vector)
    4.0
    """
    return p_norm(vector, 2)


def previous_difference_norm(vector) -> float:
    """
    Calculate the previous difference norm of a vector, where the norm is defined as the sum of the
    absolute values of the first element and the absolute differences between consecutive elements.

    The norm is mathematically represented as:

    \|x\| = |x_1| + |x_2 - x_1| + |x_3 - x_2| + ... + |x_n - x_{n-1}|

    This norm first takes the absolute value of the first element and then adds the absolute differences
    between each consecutive pair of elements.

    Parameters:
    -----------
    vector : list or tuple
        A collection of numerical elements (either integers or floats) for which the previous difference
        norm is to be computed. The function accepts a list or tuple of numbers as input.

    Returns:
    --------
    float
        The computed previous difference norm of the input vector.

    Algorithm:
    ----------
    1. The function begins by checking if the vector is empty. If it is, the norm is zero.
    2. The norm starts with the absolute value of the first element in the vector.
    3. It then iterates through the vector from the second element onward, summing the absolute differences
       between consecutive elements.
    4. The final sum is returned as the result.

    Example:
    --------
    >>> vector = [2, 5, 1, -3]
    >>> previous_difference_norm(vector)
    13.0

    >>> vector = [-4, -2, 7]
    >>> previous_difference_norm(vector)
    15.0
    """
    if not vector:
        return 0.0

    norm_value = abs(vector[0])

    for i in range(1, len(vector)):
        norm_value += abs(vector[i] - vector[i - 1])

    return float(norm_value)


print(previous_difference_norm.__doc__)