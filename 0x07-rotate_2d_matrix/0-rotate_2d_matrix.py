#!/usr/bin/python3
""" The  script that rotates a 2D matrix """


def rotate_2d_matrix(matrix):
    """
    Rotate a 2D matrix 90 degrees clockwise.

    Args:
        matrix (list[list]): A 2D matrix of size n x n

    Returns:
        None. The matrix is edited in-place.
    """
    n = len(matrix)
    # Transpose matrix
    for a in range(n):
        for z in range(a, n):
            matrix[a][z], matrix[z][a] = matrix[z][a], matrix[a][z]
    # Reverse rows
    for a in range(n):
        matrix[a] = matrix[a][::-1]
