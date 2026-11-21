
#!/usr/bin/env python3
"""Calculate the cofactor matrix of a matrix."""

import importlib

minor = importlib.import_module("1-minor").minor


def cofactor(matrix):
    """Calculate the cofactor matrix."""

    if (not isinstance(matrix, list) or
            not matrix or
            not all(isinstance(row, list) for row in matrix)):
        raise TypeError("matrix must be a list of lists")

    n = len(matrix)

    if any(len(row) != n for row in matrix):
        raise ValueError(
            "matrix must be a non-empty square matrix"
        )

    minor_matrix = minor(matrix)

    cofactors = []

    for i in range(n):
        row = []

        for j in range(n):
            sign = (-1) ** (i + j)
            row.append(sign * minor_matrix[i][j])

        cofactors.append(row)

    return cofactors
