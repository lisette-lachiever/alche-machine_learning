#!/usr/bin/env python3

"""Calculate the inverse of a square matrix."""


def inverse(matrix):
    """Calculate the inverse using determinant and adjugate."""
    if (not isinstance(matrix, list) or not matrix or
            not all(isinstance(row, list) for row in matrix)):
        raise TypeError("matrix must be a list of lists")

    n = len(matrix)

    if any(len(row) != n for row in matrix):
        raise ValueError(
            "matrix must be a non-empty square matrix")

    determinant = __import__('0-determinant').determinant
    adjugate = __import__('3-adjugate').adjugate

    det = determinant(matrix)

    if det == 0:
        return None

    adj = adjugate(matrix)

    return [
        [element / det for element in row]
        for row in adj
    ]
