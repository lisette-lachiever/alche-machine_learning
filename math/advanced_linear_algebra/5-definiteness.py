
#!/usr/bin/env python3
"""Determine the definiteness of a symmetric matrix."""

import numpy as np


def definiteness(matrix):
    """Classify a matrix using its eigenvalues."""
    if not isinstance(matrix, np.ndarray):
        raise TypeError("matrix must be a numpy.ndarray")

    if (matrix.ndim != 2 or matrix.shape[0] == 0 or
            matrix.shape[0] != matrix.shape[1]):
        return None

    try:
        if not np.isrealobj(matrix):
            return None

        if not np.all(np.isfinite(matrix)):
            return None

        if not np.allclose(matrix, matrix.T):
            return None

        eigenvalues = np.linalg.eigvalsh(matrix)
    except (TypeError, ValueError, np.linalg.LinAlgError):
        return None

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
