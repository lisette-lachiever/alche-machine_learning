
#!/usr/bin/env python3
"""Calculate the adjugate matrix of a square matrix."""


def adjugate(matrix):
    """Calculate the adjugate by transposing the cofactor."""
    if (not isinstance(matrix, list) or not matrix or
            not all(isinstance(row, list) for row in matrix)):
        raise TypeError("matrix must be a list of lists")

    n = len(matrix)

    if any(len(row) != n for row in matrix):
        raise ValueError(
            "matrix must be a non-empty square matrix")

    cofactor = __import__('2-cofactor').cofactor
    cofactor_matrix = cofactor(matrix)

    return [
        [cofactor_matrix[j][i] for j in range(n)]
        for i in range(n)
    ]
