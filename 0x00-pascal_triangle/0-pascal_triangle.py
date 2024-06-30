#!/usr/bin/python3
'''Thsi is module for working with Pascal's triangle.
'''


def pascal_triangle(n):
    '''This Function reates a list of lists of integers representing
    Pascal's triangle of a given integer.
    '''
    trianglevr = []
    if type(n) is not int or n <= 0:
        return trianglevr
    for i in range(n):
        line = []
        for j in range(i + 1):
            if j == 0 or j == i:
                line.append(1)
            elif i > 0 and j > 0:
                line.append(trianglevr[i - 1][j - 1] + trianglevr[i - 1][j])
        trianglevr.append(line)
    return trianglevr
