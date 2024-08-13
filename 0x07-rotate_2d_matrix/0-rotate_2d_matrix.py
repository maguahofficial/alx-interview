#!/usr/bin/python3
""" A Rotate 2D Matrix """


def rotate_2d_matrix(matrix):
    """ function Given an n x n 2D matrix, rotate it 90 degrees clockwise. """
    _len = len(matrix)
    for rowx in range(int(_len / 2)):
        offset = 0
        i = _len - 1 - rowx
        for column in range(rowx, _len - 1 - rowx):
            top = matrix[rowx][column]
            matrix[rowx][column] = matrix[i - offset][rowx]
            matrix[i - offset][rowx] = matrix[i][i - offset]
            matrix[i][i - offset] = matrix[column][i]
            matrix[column][i] = top
            offset += 1
