
#!/usr/bin/env python3
"""Calculate the adjugate matrix."""

import importlib

cofactor = importlib.import_module("2-cofactor").cofactor


def adjugate(matrix):
    """Calculate the adjugate matrix."""

    if (not isinstance(matrix, list) or
            not matrix or
            not all(isinstance(row, list) for row in matrix)):
        raise TypeError("matrix must be a list of lists")

    n = len(matrix)

    if any(len(row) != n for row in matrix):
        raise ValueError(
            "matrix must be a non-empty square matrix"
        )

    cofactor_matrix = cofactor(matrix)

    adj = [
        [cofactor_matrix[j][i] for j in range(n)]
        for i in range(n)
    ]

    return adj
