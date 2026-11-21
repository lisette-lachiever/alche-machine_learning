
#!/usr/bin/env python3
"""Calculate the minor matrix of a matrix."""

import importlib

determinant = importlib.import_module("0-determinant").determinant


def minor(matrix):
    """Calculate the minor matrix of a square matrix."""

    if (not isinstance(matrix, list) or
            not matrix or
            not all(isinstance(row, list) for row in matrix)):
        raise TypeError("matrix must be a list of lists")

    n = len(matrix)

    if n == 0 or any(len(row) != n for row in matrix):
        raise ValueError(
            "matrix must be a non-empty square matrix"
        )

    minors = []

    for i in range(n):
        row_minors = []

        for j in range(n):
            submatrix = [
                [matrix[r][c] for c in range(n) if c != j]
                for r in range(n) if r != i
            ]

            row_minors.append(determinant(submatrix))

        minors.append(row_minors)

    return minors
