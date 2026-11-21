
# Advanced Linear Algebra

This project covers fundamental concepts in advanced linear algebra using Python. It focuses on matrix operations, including determinants, minors, cofactors, adjugates, matrix inverses, and matrix definiteness.

The implementations use Python's built-in data structures and NumPy for numerical computations.

## Learning Objectives

By completing this project, I explored how to:

- Calculate the determinant of a square matrix.
- Generate the minor matrix of a given matrix.
- Calculate the cofactor matrix.
- Compute the adjugate of a matrix.
- Find the inverse of a non-singular matrix.
- Determine the definiteness of a symmetric matrix using eigenvalues.

## Project Structure

```text
advanced_linear_algebra/
│
├── 0-determinant.py
├── 1-minor.py
├── 2-cofactor.py
├── 3-adjugate.py
├── 4-inverse.py
├── 5-definiteness.py
└── README.md
```

## Requirements

- Python 3
- NumPy
- Pycodestyle (for code style checking)

Install NumPy:

```bash
pip install numpy
```

## Tasks

### 0. Determinant

**File:** `0-determinant.py`

Calculates the determinant of a square matrix using recursive cofactor expansion.

For a 2 × 2 matrix:

\[
A = \begin{bmatrix}a & b\\c & d\end{bmatrix}
\]

The determinant is:

\[
\det(A) = ad - bc
\]

**Example:**

```python
determinant = __import__('0-determinant').determinant

matrix = [[1, 2], [3, 4]]
print(determinant(matrix))
```

Output:

```text
-2
```

The determinant of a 0 × 0 matrix represented by `[[]]` is `1`.

### 1. Minor

**File:** `1-minor.py`

Calculates the minor matrix by removing each row and column and finding the determinant of the resulting submatrix.

**Example:**

```python
minor = __import__('1-minor').minor

matrix = [[1, 2], [3, 4]]
print(minor(matrix))
```

Output:

```text
[[4, 3], [2, 1]]
```

### 2. Cofactor

**File:** `2-cofactor.py`

Calculates the cofactor matrix by applying alternating positive and negative signs to the minor matrix.

The formula is:

\[
C_{ij} = (-1)^{i+j}M_{ij}
\]

**Example:**

```python
cofactor = __import__('2-cofactor').cofactor

matrix = [[1, 2], [3, 4]]
print(cofactor(matrix))
```

Output:

```text
[[4, -3], [-2, 1]]
```

### 3. Adjugate

**File:** `3-adjugate.py`

Calculates the adjugate matrix by transposing the cofactor matrix.

The adjugate is represented as:

\[
\operatorname{adj}(A) = C^T
\]

**Example:**

```python
adjugate = __import__('3-adjugate').adjugate

matrix = [[1, 2], [3, 4]]
print(adjugate(matrix))
```

Output:

```text
[[4, -2], [-3, 1]]
```

### 4. Inverse

**File:** `4-inverse.py`

Calculates the inverse of a square matrix using its determinant and adjugate.

The formula is:

\[
A^{-1} = \frac{1}{\det(A)}\operatorname{adj}(A)
\]

A matrix is singular if its determinant is zero. Singular matrices do not have an inverse, so the function returns `None`.

**Example:**

```python
inverse = __import__('4-inverse').inverse

matrix = [[1, 2], [3, 4]]
print(inverse(matrix))
```

Output:

```text
[[-2.0, 1.0], [1.5, -0.5]]
```

### 5. Definiteness

**File:** `5-definiteness.py`

Determines the definiteness of a NumPy matrix using its eigenvalues.

The function supports five classifications:

| Classification | Condition |
|---|---|
| Positive definite | All eigenvalues are positive |
| Positive semi-definite | All eigenvalues are non-negative |
| Negative definite | All eigenvalues are negative |
| Negative semi-definite | All eigenvalues are non-positive |
| Indefinite | Contains both positive and negative eigenvalues |

The matrix must be a valid, non-empty, square, symmetric NumPy array.

**Example:**

```python
import numpy as np

definiteness = __import__('5-definiteness').definiteness

matrix = np.array([[5, 1], [1, 1]])
print(definiteness(matrix))
```

Output:

```text
Positive definite
```

## Error Handling

The functions validate their inputs and handle invalid matrices according to the task requirements.

| Function | Invalid input | Expected behavior |
|---|---|---|
| `determinant` | Not a list of lists | `TypeError` |
| `determinant` | Non-square matrix | `ValueError` |
| `minor` | Not a list of lists | `TypeError` |
| `minor` | Empty or non-square matrix | `ValueError` |
| `cofactor` | Not a list of lists | `TypeError` |
| `cofactor` | Empty or non-square matrix | `ValueError` |
| `adjugate` | Not a list of lists | `TypeError` |
| `adjugate` | Empty or non-square matrix | `ValueError` |
| `inverse` | Not a list of lists | `TypeError` |
| `inverse` | Empty or non-square matrix | `ValueError` |
| `inverse` | Singular matrix | Returns `None` |
| `definiteness` | Not a NumPy array | `TypeError` |
| `definiteness` | Invalid matrix | Returns `None` |

## Running the Tests

Each task includes a main test file.

Run the tests using:

```bash
python3 0-main.py
python3 1-main.py
python3 2-main.py
python3 3-main.py
python3 4-main.py
python3 5-main.py
```

## Key Concepts

The project brings together several important linear algebra concepts:

1. **Determinants:** Used to determine properties such as whether a matrix is invertible.
2. **Minors and Cofactors:** Used in determinant expansion and matrix calculations.
3. **Adjugates:** Used to calculate matrix inverses.
4. **Matrix Inverses:** Used to reverse matrix transformations.
5. **Eigenvalues:** Used to understand matrix definiteness.

## Author

Lisette Mukiza



