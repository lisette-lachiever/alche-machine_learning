
#!/usr/bin/env python3
"""Calculate the cofactor matrix of a square matrix."""


def cofactor(matrix):
    """Calculate the cofactor matrix using minors."""
    if (not isinstance(matrix, list) or not matrix or
            not all(isinstance(row, list) for row in matrix)):
        raise TypeError("matrix must be a list of lists")

    n = len(matrix)

    if any(len(row) != n for row in matrix):
        raise ValueError(
            "matrix must be a non-empty square matrix")

    minor = __import__('1-minor').minor
    minor_matrix = minor(matrix)

    return [
        [((-1) ** (i + j)) * minor_matrix[i][j]
         for j in range(n)]
        for i in range(n)
    ]
