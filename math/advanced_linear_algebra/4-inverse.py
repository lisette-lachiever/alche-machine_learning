
#!/usr/bin/env python3
"""Calculate the inverse of a matrix."""

import importlib

determinant = importlib.import_module("0-determinant").determinant
adjugate = importlib.import_module("3-adjugate").adjugate


def inverse(matrix):
    """Calculate the inverse of a square matrix."""

    if (not isinstance(matrix, list) or
            not matrix or
            not all(isinstance(row, list) for row in matrix)):
        raise TypeError("matrix must be a list of lists")

    n = len(matrix)

    if any(len(row) != n for row in matrix):
        raise ValueError(
            "matrix must be a non-empty square matrix"
        )

    det = determinant(matrix)

    if det == 0:
        return None

    adj = adjugate(matrix)

    inverse_matrix = [
        [element / det for element in row]
        for row in adj
    ]

    return inverse_matrix
