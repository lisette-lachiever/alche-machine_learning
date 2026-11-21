
#!/usr/bin/env python3
"""Calculate the definiteness of a matrix."""

import numpy as np


def definiteness(matrix):
    """Calculate the definiteness of a NumPy matrix."""

    if not isinstance(matrix, np.ndarray):
        raise TypeError("matrix must be a numpy.ndarray")

    # Check that the matrix is 2D, square and non-empty
    if (matrix.ndim != 2 or
            matrix.shape[0] == 0 or
            matrix.shape[0] != matrix.shape[1]):
        return None

    # Check that all values are finite
    if not np.all(np.isfinite(matrix)):
        return None

    # Definiteness requires a symmetric matrix
    if not np.allclose(matrix, matrix.T):
        return None

    try:
        eigenvalues = np.linalg.eigvalsh(matrix)
    except (np.linalg.LinAlgError, TypeError, ValueError):
        return None

    # Numerical tolerance for floating-point calculations
    tol = 1e-10

    if np.all(eigenvalues > tol):
        return "Positive definite"

    if np.all(eigenvalues >= -tol):
        return "Positive semi-definite"

    if np.all(eigenvalues < -tol):
        return "Negative definite"

    if np.all(eigenvalues <= tol):
        return "Negative semi-definite"

    return "Indefinite"
