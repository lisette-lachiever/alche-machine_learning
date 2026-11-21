#!/usr/bin/env python3

"""Calculate the minor matrix of a square matrix."""


def minor(matrix):
    """Calculate the minor matrix using determinants."""
    if (not isinstance(matrix, list) or not matrix or
            not all(isinstance(row, list) for row in matrix)):
        raise TypeError("matrix must be a list of lists")

    n = len(matrix)

    if any(len(row) != n for row in matrix):
        raise ValueError(
            "matrix must be a non-empty square matrix")

    determinant = __import__('0-determinant').determinant

    minors = []

    for i in range(n):
        row = []

        for j in range(n):
            if n == 1:
                row.append(1)
            else:
                submatrix = [
                    [matrix[r][c] for c in range(n) if c != j]
                    for r in range(n) if r != i
                ]
                row.append(determinant(submatrix))

        minors.append(row)

    return minors
