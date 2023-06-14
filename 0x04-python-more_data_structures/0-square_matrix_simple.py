#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    n_matrix = matrix.copy()
    for a in range(len(matrix)):
        n_matrix[a] = list(map(lambda x: x**2, matrix[a]))
    return (n_matrix)
