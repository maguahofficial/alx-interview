#!/usr/bin/python3
""" island_perimeter function """


def island_perimeter(grid):
    """ function returns the perimeter of the island described in grid """

    def edges(matrix):
        """ function detect number of edges along horizontal direction """
        count = 0
        for row in matrix:
            row = [0] + row + [0]
            for ix in range(1, len(row)):
                count += row[ix] != row[ix-1]
        return count

    tgrid = [[] for _ in range(len(grid[0]))]
    for row in grid:
        for i, item in enumerate(row):
            tgrid[i].append(item)

    return edges(grid) + edges(tgrid)
