
#!/usr/bin/env python3
"""Calculate the determinant of a matrix."""


def determinant(matrix):
    """Calculate the determinant of a square matrix."""

    if (not isinstance(matrix, list) or
            not matrix or
            not all(isinstance(row, list) for row in matrix)):
        raise TypeError("matrix must be a list of lists")

    n = len(matrix)

    if matrix == [[]]:
        return 1

    if any(len(row) != n for row in matrix):
        raise ValueError("matrix must be a square matrix")

    def calculate_det(mat):
        size = len(mat)

        # A 1x1 matrix
        if size == 1:
            return mat[0][0]

        # A 2x2 matrix
        if size == 2:
            return (mat[0][0] * mat[1][1] -
                    mat[0][1] * mat[1][0])

        det = 0

        # Expand along the first row
        for col in range(size):
            submatrix = [
                [mat[i][j] for j in range(size) if j != col]
                for i in range(1, size)
            ]

            sign = (-1) ** col
            det += sign * mat[0][col] * calculate_det(submatrix)

        return det

    return calculate_det(matrix)
